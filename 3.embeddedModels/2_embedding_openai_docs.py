from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents= [
  "Delhi is the capital of India",
  "kolkata is the capital of west Bangal",
  "Paris is the captial of France"
]


result= embedding.embed_documents(documents)


print(str(result))