from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(model='gpt-4', temperature=1.6, max_completion_tokens=10)

# result= model.invoke("what is the capital of India?")
# result= model.invoke("write a code for finding even number in python!") --> responsing good for temperature= 0-0.3
result= model.invoke("write a poem for letter sister!")

print(result.content)