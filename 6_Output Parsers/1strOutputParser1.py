import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace 
from dotenv import load_dotenv 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm= HuggingFaceEndpoint(
  repo_id="google/gemma-2-2b-it", 
  task="text-generation",
  huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)
# so by default it can't give you struture output you have to make it structure

# 1st prompt -> detailed report 

template1= PromptTemplate(
    template= "write a detailed report on {topic}",
    input_variables= ['topic']
)

# 2nd prompt --> summary

template2= PromptTemplate(
    template="Write a 5 line summary on the following text. \n {text} ",
    input_variable= ['text']
)

parser= StrOutputParser()
# you can see same thing we did in strOutputParser.py and here by using parser 
# how it is easier (we don't have to write every things)

chain= template1 | model | parser | template2 | model | parser

result= chain.invoke({'topic': "black hole!!"})

print(result)