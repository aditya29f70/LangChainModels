import os
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task='text-generation',
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)

parser= StrOutputParser()

loader= TextLoader("./1_text.txt", encoding='utf-8')

docs= loader.load()


prompt= PromptTemplate(
    template="Summarize the given text {text}",
    input_variables=['text']
)

# docs is list of dict which have Document (metadata(dict)), page_content
# not only this all the docuement loader output has list of docuement (and list cantains docuements current that above one contain one docuements (Docuement-> metadata, page_content))

# print(docs)

# print(docs[0])

# print(docs[0].metadata)
# print(docs[0].page_content)


chain= prompt | model | parser 

result= chain.invoke({'text': docs[0].page_content})

print(result)