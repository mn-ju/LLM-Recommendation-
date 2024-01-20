import numpy as np
import pandas as pd
from langchain.embeddings import LlamaCppEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain.chains import (
    ConversationalRetrievalChain,
    LLMChain
)
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts.prompt import PromptTemplate
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.http import models
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import OpenAI
from langchain.document_loaders import DataFrameLoader
from src.config import config
from src.prompt import condense_question_prompt_template, qa_prompt_template

def QdrantClient_setup():
    url = config['url']
    api_key = config['api_key']
    client = QdrantClient(url= url,api_key=api_key,)
    return client
  

def qdrant_instance_setup(collection_name):
    client = QdrantClient_setup()
    embeddings_model_name = config['embeddings_model_name']
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    qdrant_instance = Qdrant(client, collection_name, embeddings)
    return qdrant_instance

def llm_model_setup():
    openai_api_key = config['openai_api_key']
    # openai_api_base = config ['openai_api_base']
    # openai_organization = config['openai_organization']
    Open_ai_llm = OpenAI(openai_api_key= openai_api_key , verbose=True, max_tokens= 1800)
    # Open_ai_llm = OpenAI(openai_api_key = openai_api_key,openai_api_base=openai_api_base, model= "meta-llama/Llama-2-13b-chat-hf", logit_bias = None, max_tokens= 1000 )
    return Open_ai_llm

def streaming_llm_setup(): 
    openai_api_key = config['openai_api_key']
    # openai_api_base = config ['openai_api_base']
    streaming_llm = OpenAI(openai_api_key= openai_api_key , verbose=True, max_tokens= 1800)
    # streaming_llm = OpenAI(openai_api_key = openai_api_key,openai_api_base=openai_api_base,model= "meta-llama/Llama-2-13b-chat-hf", logit_bias = None, verbose=True, streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), max_tokens= 1000 )
    return streaming_llm


def llm_model(): 
    collection_name = "Myntra_fashion_products"
    qdrant_instance = qdrant_instance_setup(collection_name)
    retriever = qdrant_instance.as_retriever(k = 10)
    llm = llm_model_setup()
    streaming_llm = streaming_llm_setup()
    condense_question_prompt = PromptTemplate.from_template(condense_question_prompt_template)
    qa_prompt= PromptTemplate.from_template(qa_prompt_template)
    question_generator = LLMChain( llm=llm, prompt=condense_question_prompt)
    doc_chain = load_qa_chain( llm=streaming_llm, chain_type="stuff", prompt=qa_prompt)
    chatbot = ConversationalRetrievalChain( retriever=retriever, combine_docs_chain=doc_chain, question_generator=question_generator)
    return chatbot





