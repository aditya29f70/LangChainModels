import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


load_dotenv() 


llm= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)

prompt= PromptTemplate(
    template="Suggest a catchy blog title about {topic}.",
    input_variables=['topic']
)

chain= LLMChain(llm= model, prompt= prompt)

topic= input("Enter a topic")
output= chain.run(topic)

print("Generated blog title :", output)


# first chain which is made by langchain which make work easier now we can direct connect most
# common step (prompt -> llm) directly without going manually