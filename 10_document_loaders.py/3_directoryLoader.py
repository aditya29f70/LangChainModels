from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader= DirectoryLoader(
  path="../10_books",
  glob="*.pdf",
  loader_cls= PyPDFLoader
)

docs= loader.load()

# print(len(docs)) # give you total number pages= total number of Documents objects

# # if you want to see first pdf's first page content
# print(docs[1].page_content)
# print(docs[1].metadata)

# for doc in docs:
#   print(doc.metadata)
# it will take more time to load page content to momery after that once it is loaded all the process will be ron faster


# but if we use lazy_load then loading will we faster but asking each doc(which generator of document) to load will take time

docs_lazy= loader.lazy_load() # generator object DirectoryLoader.lazy_load

for doc in docs_lazy:
  print(doc.metadata)

