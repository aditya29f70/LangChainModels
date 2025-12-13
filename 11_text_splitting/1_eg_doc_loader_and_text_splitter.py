from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter


loader= PyPDFLoader('../10_books/Introduction_to_Agents.pdf')

docs= loader.load() # you will get document obj correspont to each page


splitter= CharacterTextSplitter(
  chunk_size=100,
  chunk_overlap=0,
  separator=''
)

# since we have list of document obj so we will split_document
result= splitter.split_documents(docs)

# print(result) ## it will list of chunks and note:: each chunk will be itself a document obj

print(result[0].page_content)