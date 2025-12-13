import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import re

load_dotenv()

url= "https://www.amazon.in/2022-Apple-MacBook-Laptop-chip/dp/B0DLHWMPQL/ref=sr_1_1?crid=18HMQKEF9CSI0&dib=eyJ2IjoiMSJ9.pe2vlBr-6VKlIeKwJuVw54rybiREDWeY1ICSuTRSOK9Cb8PMv6P6B61WkDJUNes37Ym-OQ0Mfa92fPci1qu9M1PpwTAUvVRv_vai46H2A6HLhY0wGSiiehnatBQGNQMh2JuzfcYjJC-40Xw1DQtPdceTMKthr-qunsgcZ1h23BsX1-JvO3lToonce4oY2kmDFDI6wU7qNuUc0yWVf9Jznp6DqBqSuEiEhDOwGr_4mtM.dGHlcwrjO1HAfiUgaZ3YOwFgNFeNEr2h62oZe5kAbnY&dib_tag=se&keywords=Apple+mac+m2&qid=1765613122&sprefix=apple+mac+m2%2Caps%2C245&sr=8-1"

loader= WebBaseLoader(url)
# one facility is that you can give list of urls then you will be gotten list of documents object

docs= loader.load()

# print(len(docs)) # numbers of documents which you will get will only one

# print(docs[0])

## now try to ask using model ;; one problem is that there were lot of spaces in page content so for that


# print(re.sub(r"\s+", " ", docs[0].page_content))

about_product= re.sub(r"\s+", " ", docs[0].page_content)

# sub usually means “substitute” or “replace”


llm= HuggingFaceEndpoint(
  repo_id="Qwen/Qwen2.5-1.5B-Instruct",
  task="text-generation",
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)

parser= StrOutputParser()

prompt= PromptTemplate(
  template="Answer the following question \n {question} from this text about product \n {text}",
  input_variables=['question', 'text']
)

chain= prompt | model | parser 

result= chain.invoke({"question": "tell me about it's reviews?, what it's ration",
                      "text": about_product})

print(result)
