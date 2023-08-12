"""
https://docs.google.com/document/d/1ObnJqcwzVmcTt8gT12DE8lil8J2LZBI-/edit
"""
#######################################################################
# Known Issues (https://developer.microsoft.com/en-us/graph/known-issues/?search=)
# Getting all items by navigating drive is partially supported, use list instead
#######################################################################
import os
import sys
import json
import logging
import string
import urllib
import traceback
from pathlib import Path
from urllib import request
from urllib.parse import unquote
from collections import defaultdict
from datetime import datetime

import requests

try:
    from ..utils import SafeEncoder
except:
    from enrichsdk.utils import SafeEncoder

logger = logging.getLogger("app")

__all__ = ['AzureSharepointClient']

class AzureSharepointClient():
    """
    Simple azure client that uses GraphQL interface
    """

    def __init__(self, cred):
        self.cred = cred

    def get_access_token(self):

        if hasattr(self, 'token'):
            return self.token

        cred = self.cred
        tenant_id = cred['tenant_id']
        client_id = cred['client_id']
        client_secret = cred['client_secret']

        #Get access token
        token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        token_data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": "https://graph.microsoft.com/.default"
        }

        try:
            token_response = requests.post(token_url, data=token_data)
            access_token = token_response.json()["access_token"]
        except:
            token_data['client_secret'] = token_data['client_secret'][:10]+"..."
            raise Exception("Unable to get token",
                            extra={

                            })

        return access_token

    def list_items(self, folder):

        access_token = self.get_access_token()

        site_id = folder['site_id']
        dirname = folder['name']

        # => List files in the library
        url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{dirname}/items"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }


        # => Walk through the pages to get the items
        all_items = []
        toprocess = [url]

        while len(toprocess) > 0:
            url = toprocess.pop(0)
            graph_result = requests.get(url=url, headers=headers)
            if graph_result and graph_result.text:
                json_resp = json.loads(graph_result.text)

                # There is a 'next page' of results, then include
                # them..
                if '@odata.nextLink' in json_resp:
                    page_url = json_resp['@odata.nextLink']
                    toprocess.append(page_url)

                if 'value' in json_resp:
                    all_items.extend(json_resp['value'])

        return all_items

    def write_item_metadata(self, item, local_path):

        metadatafile = local_path + ".metadata.json"
        with open(metadatafile, 'w') as fd:
            fd.write(json.dumps({
                "details": item,
                "size": os.path.getsize(local_path),
                "timestamp": datetime.now().replace(microsecond=0)
            }, indent=4, cls=SafeEncoder))

    def read_item_metadata(self, item, local_path):

        metadatafile = local_path + ".metadata.json"
        try:
            return json.load(open(metadatafile))
        except:
            pass
        return None

    def should_download(self, item, local_path):

        if not os.path.exists(local_path):
            return True

        metadata = self.read_item_metadata(item, local_path)
        if metadata is None:
            return True

        size          = metadata['size']
        last_modified = metadata['details']['lastModifiedDateTime']
        etag          = metadata['details']['eTag']

        condns = [(size == os.path.getsize(local_path)),
                   (last_modified == item['lastModifiedDateTime']),
                   (etag == item['eTag'])]
        return not all(condns)

    def download_drive_item(self, folder, item, item_id, dir_path, local_path):
        """
        Download one item
        """

        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        site_id = folder['site_id']

        if dir_path is None:
            raise Exception("Invalid drive path")

        download_url = f'https://graph.microsoft.com/v1.0/sites/{site_id}/drive/items/{item_id}/content'

        r = requests.get(download_url, allow_redirects=True, headers=headers)

        if r.status_code >= 400:
            logger.error("Failed to download",
                         extra={
                             "data": f"url: {download_url}\nResponse: {r}"
                         })
            raise Exception("Failed to download")

        with open(local_path, 'wb') as fd:
            fd.write(r.content)

        if not os.path.exists(local_path):
            raise Exception("Error while retrieving")

        self.write_item_metadata(item, local_path)

    def get_etag_id(self, etag) -> str:
        # "eTag": "\"a6c0f692-b303-442c-ad12-1201fc4072b9,1\""
        eid = None
        etag = etag.replace("\"", '')
        ids = etag.split(",")
        if len(ids) > 0:
            eid = ids[0]
        return eid

    def download_items(self, folder, items, metadata_handler=None):
        """
        Download the items into the local_root. Items should be the result of
        """

        local_root = folder['local_root']
        root_url = folder['root_url']
        stats = defaultdict(int)

        msg = ""
        downloaded = []
        for item in items:
            if 'contentType' not in item:
                stats['error_no_content_type'] += 1
                continue
            content_type = item['contentType']['name']
            weburl = item['webUrl']
            dir_path = unquote(weburl.replace(root_url, ''))
            if len(dir_path) == 0:
                stats['error_invalid_url'] += 1
                continue
            if dir_path.startswith("/"):
                dir_path = dir_path[1:]
            full_path = os.path.join(local_root, dir_path)
            if content_type == 'Folder':
                stats['folders'] += 1
                os.makedirs(full_path, exist_ok=True)
            else:
                stats['files'] += 1
                etag = item['eTag']
                if etag is None:
                    stats['error_file'] += 1
                    stats['error_file_no_etag'] += 1
                    continue
                eid = self.get_etag_id(etag)
                if eid is None:
                    stats['error_file'] += 1
                    stats['error_file_no_eid'] += 1
                    continue

                if self.should_download(item, full_path):
                    try:
                        self.download_drive_item(folder,
                                                 item,
                                                 eid,
                                                 dir_path,
                                                 full_path)
                        msg += f"[Download] {full_path}\n"
                        stats['file_downloaded'] += 1

                        # Dump intermittent
                        downloaded.append(dir_path)
                        if len(downloaded) > 5:
                            logger.debug(f"Downloaded {len(downloaded)} files",
                                         extra={
                                             'data': "\n".join(downloaded)
                                         })
                            downloaded = []

                    except:
                        msg += f"[Error] {full_path}\n"
                        stats['error_download_exception'] += 1
                        break
                else:
                    stats['file_no_download_required'] += 1

        return stats, msg


    def create_delta(self):
        headers = {
            'Authorization': self.access_token
        }

        sharepoint_site_id = self.params['sharepoint_site_id']
        delta_url = f'https://graph.microsoft.com/v1.0/sites/{sharepoint_site_id}/drive/root/delta'

        result = requests.get(url=delta_url, headers=headers)

        return result

    def get_latest_changes(self):
        headers = {
            'Authorization': self.access_token
        }

        sharepoint_site_id = self.params['sharepoint_site_id']
        delta_updates_url = f'https://graph.microsoft.com/v1.0/sites/{sharepoint_site_id}/drive/root/delta?token='

        result = requests.get(url=delta_updates_url, headers=headers)

        return result


if __name__ == "__main__":

    # Follow these instructions to get these attributes
    # https://docs.google.com/document/d/1ObnJqcwzVmcTt8gT12DE8lil8J2LZBI-/edit

    logging.basicConfig(level=logging.DEBUG)

    site_id = "aa4ff333-7526-4ad5-bf4b-a35b05007b24"
    site_name = 'testsharepointsite'
    folder = {
        "name": "Documents",
        "site_id": site_id,
        "root_url": f"https://scribbledatainc.sharepoint.com/sites/{site_name}/Shared%20Documents",
        "local_root": "downloads"
    }

    # Client details
    tenant_id = os.environ['TEST_TENANT_ID'] # UUID
    client_id = os.environ['TEST_CLIENT_ID'] # UUID
    client_secret = os.environ['TEST_CLIENT_SECRET']

    credentials = {
        'tenant_id': tenant_id,
        'client_id': client_id,
        'client_secret': client_secret
    }

    azureclient = AzureSharepointClient(credentials)

    items = azureclient.list_items(folder)
    print(json.dumps(items, indent=4))

    stats, msg = azureclient.download_items(folder, items)
    error_keys = [k for k in stats.keys() if k.startswith("error_")]
    logger.debug(f"Completed w/ {len(error_keys)} errors",
                 extra={
                     'data': json.dumps(stats, indent=4) + "\n" + msg
                 })
    sys.exit()
    #
    ## Sharepoint folder & site details
    #sharepoint_site_id = 'scribbledatainc.sharepoint.com,aa4ff333-7526-4ad5-bf4b-a35b05007b24,12ee2a68-7293-41c3-a64f-d87692cdc34b'
    #base_drive_folder_list_id = '12c2236e-1f51-4418-bcb8-ece98a867b3a'

    #base_drive_path = f'https://scribbledatainc.sharepoint.com/sites/{sharepoint_site_name}/Shared%20Documents/'

    ## Fixed query urls
    #default_page_size = 20

    ## Client details
    #tenant_id = os.environ['TEST_TENANT_ID'] # UUID
    #client_id = os.environ['TEST_CLIENT_ID'] # UUID

    #credentials = {
    #    'tenant_id': tenant_id,
    #    'client_id': client_id,
    #}

    #option = 1

    #if option == 1:
    #    # Option 1. Create secret id and value
    #    client_secret = os.environ['TEST_CLIENT_SECRET']
    #    credentials.update({
    #        'client_secret': client_secret
    #    })
    #else:
    #    # Option 2
    #    # https://blog.darrenjrobinson.com/microsoft-graph-using-msal-with-python-and-certificate-authentication/
    #    # openssl genrsa -out aadappcert.pem 2048
    #    # openssl req -new -key aadappcert.pem -out aadappcert.csr
    #    # openssl x509 -req -days 365 -in aadappcert.csr -signkey aadappcert.pem -out aadappcert.crt
    #    #
    #    thumbprint = "B19B6D736968EB6711D04BA449346397CEBA6F8E"
    #    certfile = "aadappcert.pem"
    #    private_key = open(certfile).read()
    #    credentials.update({
    #        "thumbprint": thumbprint,
    #        "private_key": private_key
    #    })


    #azureclient = AzureSharepointClient(params, credentials)
    ##site_list = azureclient.list_sites()
    ##print(json.dumps(site_list, indent=4))
    ##sys.exit()

    #items = azureclient.list_all_subitems(base_drive_folder_list_id, page=default_page_size)
    #print(json.dumps(items, indent=4))
    ##azureclient.download_items(items, "download")

