import json
import time
import string

from langchain import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

from . import agent_events
from llmsdk.agents.basellm import BaseLLMAgent
from ..lib import extractors
from llmsdk.lib import SafeEncoder

__all__ = ['LLMQuerierExtractor']

class LLMQuerierExtractor(BaseLLMAgent):
    """
    Class to do querying of a docset and extracting specific information fields using LLMs
    Query can be run against a specified set of documents that act
    as context to constrain the answers
    """

    def __init__(self,
                 name,
                 cred={},
                 platform="openai",
                 searchapi="serpapi",
                 statestore="redis",
                 topk=3):
        """
        init the LLM query agent
        name: name of the agent
        cred: credentials object
        platform: name of the LLM platform backend to use
                default to OpenAI GPT platform for now, Azure is also supported
                will be extended in the future to suuport other models
        memory_size: how many tokens of memory to use when chatting with the LLM
        """

        start_time = time.time()

        # init the base class
        super().__init__(name=name,
                         cred=cred,
                         platform=platform,
                         agent_type="extract",
                         searchapi=searchapi,
                         statestore=statestore)

        # defaults
        self.chunk_size = 1000
        self.chunk_overlap = 200
        self.index = None
        self.metadata = {}
        self.vdb_client = None
        self.index_name = None
        self.index_store = None
        self.topk = topk
        self.doc_signatures = []
        self.docs = {}

        # LLM params
        self.platform = platform
        self.chaintype = "stuff"

        # init the llm and embeddings objects
        self.llm, self.embeddings = self._get_llm_objs(platform=self.platform,
                                                       cred=self.cred)

        # init the QnA chain for internal queries
        prompt = self._get_query_prompt_internal()
        self.llm_chain_int = load_qa_chain(llm=self.llm,
                                           chain_type=self.chaintype,
                                           prompt=prompt)
        # note metadata for this agent
        self.metadata = {
            "agent": {
                "name": self.agent_name,
                "name": self.agent_type,
                "platform": self.platform,
                "chaintype": self.chaintype,
            },
            "events": []
        }
        # log that the agent is ready
        duration = time.time() - start_time
        event = self._log_event(agent_events._EVNT_READY, duration)

    ## helper functions

    def _get_query_prompt_internal(self):
        """
        generate a prompt for running a query in internal mode
        """
        template = """You are a highly advanced AI program designed to extract specific pieces of information from legal contract documents.
Use the following pieces of context extracted from a legal document to answer the question at the end.
If the question asks you to format your answer in some specific manner, do so.
If you cannot find the answer in the context, just say 'unknown', don't try to make up an answer and do not provide any explanations.

Here is the context:
        {context}

Here is the question:
        {input}

Your response:"""

        prompt = PromptTemplate(
            input_variables=["input", "context"],
            template=template
        )

        return prompt

    ## interfaces


    def read_document(self, source, content, metadata={}, params={}, store="chroma", persist_directory=None):
        """
        wrapper function that takes in the path to a document
        and sets it up for reading by the agent
        this function will create a new index if the agent does not already have one
        else it will use the existing index pointer
        needs the persist_directory that the index will use
        """
        # load the document
        data = self.load_data(source=source, content=content)

        # add the document to index
        if not self.index:
            # we have to init a new index
            self.create_add_index(data=data,
                                   store=store,
                                   persist_directory=persist_directory,
                                   index_name=self.agent_name)
        else:
            # we can use the agent's index pointer
            self.add_to_index(data)

        # extract text from document if it is a pdf
        # so that we have the table data
        if source in ["pdf"]:

            # run through Textract
            extracted_data = extract_text_from_file(content, provider="aws")

            # take the Textract output
            # and add tables and linetext to index
            for block in ["tables", "text"]:
                for extract in extracted_data:
                    # for each page in the document
                    for entry in extract[block]:
                        # for each table in the page
                        if any(f not in entry for f in ['id', 'content']):
                            continue
                        metadata = { "source": entry['id'] }
                        data = self.load_data(source="str",
                                               content=entry['content'],
                                               metadata=metadata)
                        self.add_to_index(data)

            # add the signature details to the agent's knowledge
            for extract in extracted_data:
                signatures = extract["signatures"]
                self.doc_signatures.extend(signatures)

        return

    def run_query_internal(self, query):
        """
        run a query using llm on an internal docset indexed in index
        this is useful when looking for answers using a private source of data
        """
        # get the similar docs
        docs = self.get_similar_docs(query, topk=self.topk)

        # setup the QnA chain object
        response = self.llm_chain_int({"input_documents":docs, "input":query},
                                    return_only_outputs=True)

        # get token count
        context = "\n\n".join([d.page_content for d in docs])
        p = self.llm_chain_int.llm_chain.prompt.format(input=query, context=context)
        r = response.get('output_text', '')
        prompt_response = f"{p}\n{r}"
        num_tokens = self._get_token_count(prompt_response)

        # run the query against the similar docs
        result = {
            "question": query,
            "answer": response.get('output_text', self._err_msg('field')).strip(),
            "sources": [{"content": d.page_content, "metadata": d.metadata, "distance": d.metadata.pop('distance')} for d in docs],
            "num_tokens": num_tokens
        }

        # check if suggest call is needed
        if ('output_text' not in response) or ("i am not sure" in result['answer'].lower()):
            response = self.run_query_suggest(query)
            result['suggest'] = response['suggest']
            # we don't have a usable answer, so no need for sources
            result['sources'] = []

        return result

    def query(self, query, mode="internal"):
        """
        run a query on an index using an llm chain object
        query: query string
        index: index object
        llm: llm object
        mode: 'internal' for querying over docset,
        topk: number of top-K similar docs to matching query to return
        """

        start_time = time.time()

        if mode == 'internal':
            result = self.run_query_internal(query)
        else:
            raise Exception(f"Unsupported mode: {mode}")

        # log the event
        params = {
            "query": query,
            "mode": mode,
            "result": result.copy() if result is not None else None
        }
        duration = time.time() - start_time
        event = self._log_event(agent_events._EVNT_QUERY, duration, params=params)

        # add the event to the result
        result['metadata'] = {
            "timestamp": event['timestamp'],
            "duration": event['duration'],
        }

        return result

    def process_spec_queries(self, spec):
        """
        take a spec containing questions and answer them
        against the docset indexed by the agent
        """

        # get the list of queries
        query_set = spec.get("query_set", [])

        # begin an empty dict
        extracted_info = {}
        grounding = {}

        # foreach query to process
        for one_query in query_set:

            q_name = one_query.get("name")
            query = one_query.get("query")
            query_mod = one_query.get("query_mod")
            query_alts = one_query.get("query_alts", [])
            use_alts = one_query.get("use_alts", "on-fail")
            postprocess = one_query.get("postprocess")
            fill_columns = one_query.get("fill_columns")

            self.logger.debug(f"Running query: {q_name}",
                                 extra={
                                     'source': self.agent_name,
                                     'data': json.dumps(one_query, indent=4)
                                 })


            if not query or not fill_columns:
                continue

            if query_mod:
                # we have to modify our query before passing to the LLM
                mod_handler = query_mod.get("method")
                if callable(mod_handler):
                    cannot_modify = False
                    params = {}
                    for col in query_mod.get("inputs", []):
                        if col not in extracted_info:
                            cannot_modify = True
                            break
                        else:
                            params[col] = extracted_info[col]
                    if cannot_modify:
                        continue

                    # call the handler to modify the query
                    query = mod_handler(query, params)
                else:
                    continue

                # check if we need to modify alt queries also
                apply_to = query_mod.get("apply_to", "first")
                if apply_to == "all":
                    query_alts = [mod_handler(q, params) for q in query_alts]

            # collect all the queries we need to run
            queries = [query] + query_alts


            # run the queries against the LLM
            for query in queries:

                # get the answer
                response = self.query(query, mode="internal")
                answer = response['answer']
                sources = response['sources']
                if answer.translate(str.maketrans('', '', string.punctuation)).lower().strip() == "unknown":
                    continue

                # post-process if needed
                if postprocess and callable(postprocess):
                    answer = postprocess(answer)

                # add the answers to the columns in the extracted dataset
                if len(fill_columns) > 1:
                    i = 0
                    for col in fill_columns:
                        ans_i = answer[i]
                        ans = extracted_info.get(col,[])
                        if answer in ans:
                            # we have found this answer before
                            # no need to collect it again
                            continue
                        ans.append(ans_i)
                        extracted_info[col] = ans
                        i += 1
                else:
                    col = fill_columns[0] # have only one column to fill
                    ans = extracted_info.get(col,[])
                    if answer in ans:
                        # we have found this answer before
                        # no need to collect it again
                        continue
                    ans.append(answer)
                    extracted_info[col] = ans

                # at this point, at least one alt query has response
                # collect the grounding elements
                for col in fill_columns:
                    curr_sources = grounding.get(col, [])
                    curr_sources.append(sources)
                    grounding[col] = curr_sources

                # check if we need to run other alts
                if use_alts == "on-fail":
                    # no need to run an alt query
                    # since we have atleast some response
                    break

        # check if all columns exist
        # and add the collected grounding
        extracts = {}
        for one_query in query_set:
            fill_columns = one_query.get("fill_columns", [])
            for col in fill_columns:
                extracts[col] = {
                    "n_answers": 0 if not extracted_info.get(col) else len(extracted_info[col]),
                    "answer": extracted_info.get(col, []),
                    "sources": grounding.get(col, []),
                }

        return extracts

    def process_spec_signatures(self, spec):
        """
        check if signatures are present
        """
        self.logger.debug("Detecting signatures...",
                             extra={'source': self.agent_name})

        if spec.get("detect_signatures", False) == False:
            return None

        pages = []
        confidence = 0
        if len(self.doc_signatures) > 0:
            for signature in self.doc_signatures:
                pages.append(signature['page'])
                confidence += signature['confidence']
            n_sigs = len(pages) # this is correct
            pages = list(set(pages))
            n_pages = len(pages)
            confidence = round(confidence/n_sigs, 2)

            comment = f"Detected {n_sigs} signatures across {n_pages} pages"

            signatures = {
                "found": True,
                "comment": comment,
                "n_signatures": n_sigs,
                "n_pages": n_pages,
                "pages": pages,
                "confidence": confidence,
            }
        else:
            signatures = {
                "found": False,
                "comment": f"No signatures detected",
            }

        return signatures

    def process_spec(self, spec):
        """
        process a profilespec
        """
        name = spec.get("name")
        self.logger.debug(f"Processing spec: {name}",
                             extra={
                                 'source': self.agent_name,
                                 'data': json.dumps(spec, indent=4)
                             })

        # check for signatures
        signatures = self.process_spec_signatures(spec)

        # process the questions
        extracts = self.process_spec_queries(spec)

        result = {
            "spec": name,
            "timestamp": time.time(),
            "extracts": extracts,
            "signatures": signatures
        }

        return result

    def extracts_to_df(self, info):
        """
        Convert extracts object into dataframe
        """
        extracts = info['extracts']
        entries = []

        for col, details in extracts.items():
            entry = {
                "field": col,
                "answer": details['answer'],
                "grounding": json.dumps(details['sources']),
            }
            entries.append(entry)

        df = pd.DataFrame(entries)

        return df



def get_sample_profilespec():

    # example of how to write methods to modify
    # profilespec queries
    def mod_query_duration(query, params):
        """
        modify the duration query based on the value
        populated in the billing frequency column
        """
        freqs = {
            "daily": "days",
            "weekly": "weeks",
            "monthly": "months",
            "quarterly": "months",
            "semi-annually": "months",
            "annually": "years",
            "yearly": "years",
        }

        # get the inputs we need
        billing_freq = params.get("billing_freq")
        # check if we have them and can proceed
        if not billing_freq:
            return query

        # modify the duration query
        billing_freq = billing_freq.lower()
        freq = freqs.get(billing_freq)
        if freq:
            query = f"{query} in {freq}?"

        return query

    # example of how to write methods to post-process LLM response
    def pp_companies(answer):
        """
        post-process the answer for the
        queries on parties involved
        """
        try:
            answer = json.loads(answer)
        except:
            pass
        return answer

    query_spec = {
        "name": "ecap_contracts",
        "detect_signatures": True,
        "query_set": [
            {
                "name": "industry",
                "query": "what industry vertical does the contract deal with? respond with only the type of industry",
                "query_alts": [
                    "what industry is mentioned? respond with only the type of industry"
                ],
                "use_alts": "on-fail",
                "postprocess": None,
                "fill_columns": ["industry_vertical"]
            },
            {
                "name": "companies",
                "query": "which two companies is this contract between? format your response as a json list",
                "postprocess": pp_companies,
                "fill_columns": ["company_1", "company_2"]
            },
            {
                "name": "contract type",
                "query": "what type of contract does the document represent? choose from one of the following options: service agreement, master services agreement, purchase order, change order, subscription, saas services agreement, ammendment",
                "postprocess": None,
                "fill_columns": ["contract_type"]
            },
            {
                "name": "start date",
                "query": "what is the start date of the contract? respond with only a date.",
                "query_alts": [
                    "what is the effective date of the contract? respond with only a date"
                ],
                "use_alts": "on-fail",
                "postprocess": None,
                "fill_columns": ["commencement_date"]
            },
            {
                "name": "end date",
                "query": "what is the end date of the contract? respond with only a date.",
                "postprocess": None,
                "fill_columns": ["termination_date"]
            },
            {
                "name": "billing frequency",
                "query": "what is the billing frequency mentioned in the contract? choose from one of the following options: daily, weekly, monthly, quarterly, semi-annually, annually, adhoc",
                "postprocess": None,
                "fill_columns": ["billing_freq"]
            },
            {
                "name": "duration",
                "query": "what is the duration of the contract",
                "query_mod": {
                    "method": mod_query_duration,
                    "inputs": ["billing_freq"],
                    "apply_to": "first"
                },
                "query_alts": [
                    "what is the duration of the contract?"
                ],
                "use_alts": "always",
                "postprocess": None,
                "fill_columns": ["duration"]
            },
            {
                "name": "billing currency",
                "query": "what is the billing currency for the contract? respond with only the currency code",
                "query_alts": [
                    "what cuurency is the cost mentioned in? respond only with the code"
                ],
                "use_alts": "on-fail",
                "postprocess": None,
                "fill_columns": ["billing_currency"]
            },
            {
                "name": "billable amount",
                "query": "what is the total billable value of the contract?",
                "query_alts": [
                    "what is the cost mentioned?"
                ],
                "use_alts": "on-fail",
                "postprocess": None,
                "fill_columns": ["billable_amount"]
            }
        ]
    }

    return query_spec


if __name__ == "__main__":

    # vars
    # cred = get_credentials_by_name('openai-api')
    persist_directory = "chromadb123"
    pdfpaths = {
        # "aidb": ".../ADIB Agreement.pdf",
        # "acko": ".../Acko Technologies Pvt Ltd-ACKO-Unicorn.pdf",
        # "cube": ".../Cube Investments.pdf",
        # "angeloak": ".../Angel Oak Vaultedge.pdf",
        # "hdfc": ".../HDFC_VaultEdge_Agreement_Signed.pdf",
        # "kpmg": ".../kpmg.pdf",
        # "miami": ".../Miami Dade College - Almabase Inc Partnership Agreement (2).pdf",
        # "servicenow": ".../Service Now Executed.pdf",
        # "infosys": ".../Infosys.pdf",
    }
    profilespec = get_sample_profilespec()
    contract_name = "acko"
    pdfpath = pdfpaths[contract_name]

    # create an agent
    agent = LLMQuerierExtractor(name=f"ecaps_agent_{contract_name}")

    # point it to a document to read
    agent.read_document(source="pdf", content=pdfpath, persist_directory=persist_directory)

    # run it against the profilespec
    result = agent.process_spec(profilespec)

    # output extraction
    print (json.dumps(result, indent=4, cls=SafeEncoder))
    # agent events
    print (json.dumps(agent.get_metadata(), indent=4, cls=SafeEncoder))
