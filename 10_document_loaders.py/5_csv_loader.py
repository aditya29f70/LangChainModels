from langchain_community.document_loaders import CSVLoader

loader= CSVLoader(file_path="./indian_farm_activities_dataset.csv")

docs= loader.load()
## use lazy_load if data are high , now you can ask any data correspoinding to any row


print(len(docs))
print(docs)