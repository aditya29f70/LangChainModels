from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HugginFAceEmbedding 
from langchain.vectorstores import FAISS 
from langchain.llms import OpenAI 
from langchain.chains import RetrivalQA 


# load the doc 
loader = TextLoader('docs.txt')
documents= loader.load() 

# split the text into smaller chunks 

text_splitter= RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs= text_splitter.split_documents(documents)

vectorstore= FAISS.from_documents(docs, OpenAIEmbeddings())

retriever= vectorstore.as_retriever() 

llm= OpenAI()

qa_chain= RetrivalQA.from_chain_type(llm= llm, retriever= retriever)

query= "what are the key takeways from the documents?"

answer= qa_chain.run(query)

print(answer)

