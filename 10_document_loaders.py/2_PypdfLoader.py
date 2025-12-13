from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader("./deep_learning.pdf")

docs= loader.load()

print(docs)