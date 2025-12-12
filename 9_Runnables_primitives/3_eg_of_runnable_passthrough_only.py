import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

load_dotenv()

parser= StrOutputParser()

llm = HuggingFaceEndpoint(
  repo_id="Qwen/Qwen2.5-1.5B-Instruct",
  task= "sentance-generation",
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)


prompt= PromptTemplate(
  template="Generate a joke on topic {topic}",
  input_variables=['topic']
)

chain= RunnablePassthrough()

# what ever input you will give to this runnable passthrough it will give you that input as it is

# result= chain.invoke(2)
result= chain.invoke({"topic": 'india'})

print(result)

