import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task= 'text-generation',
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)


model= ChatHuggingFace(llm= llm)



em_model= HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# load the doc
loader= TextLoader("./docs.txt") # Ensure docs.txt exists
documents= loader.load()

# split the text into smaller chunks
text_splitter= RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs= text_splitter.split_documents(documents)

# convert text into embedding and store in FAISS
vectorstore= FAISS.from_documents(docs, em_model)

# create a retriever (fetches relevant document)
retriever= vectorstore.as_retriever()

# manually retrieve relevent doc
query= "What are the key takeaways from the document?"

# sementic search
retrieved_docs = retriever.invoke(query)

# combine retrieved text into a single prompt
retrieved_text= "\n".join([doc.page_content for doc in retrieved_docs])


# manually pass retrieved text to llm

prompt= f"Based on the following text, answer the question: {query} \n\n {retrieved_text}"

answer= model.invoke(prompt)

print("Answer :", answer)
