import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

llm= HuggingFaceEndpoint(
  repo_id="Qwen/Qwen2.5-1.5B-Instruct",
  task= "text-generation",
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)

parser= StrOutputParser()

prompt= PromptTemplate(
  template="Generate a joke on {topic}",
  input_variables=['topic']
)

chain= prompt | model | parser 

result= chain.invoke('india')

print(result)
