from langchain_community.document_loaders import TextLoader

loader= TextLoader("./1_text.txt", encoding='utf-8')

docs= loader.load()

# docs is list of dict which have Document (metadata(dict)), page_content
# not only this all the docuement loader output has list of docuement (and list cantains docuements current that above one contain two docuements (Docuement, page_content))

print(docs) 