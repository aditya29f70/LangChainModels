from langchain_huggingface import HuggingFaceEmbeddings

embedding= HuggingFaceEmbeddings(model_name= 'sentence-transformers/all-MiniLM-L6-v2')

# text= "Delhi is the capital of India!"
documents= [
  "Delhi is the capital of India",
  "kolkata is the capital of west Bangal",
  "Paris is the captial of France"
]


# vector= embedding.embed_query(text)
vector= embedding.embed_documents(documents)

print(str(vector))