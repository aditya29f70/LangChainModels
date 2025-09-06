from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
 

embedding= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# question= 'what is the capital of india?'
question= 'goverment has to work'

documents= [
  'Delhi is the capital of india which is at the north part of it and there is two region in delhi, first one is new delhi and other one old delhi',
  'Delhi is the beatiful place of india but there is lot of problem those have to be solved by goverment',
  'paris is the capital of france and this my favrate place'
]

q_vector= embedding.embed_query(question)
doc_vectors= embedding.embed_documents(documents)

q_vector= np.array(q_vector)
q_vector= q_vector.reshape(1, -1)

simi= cosine_similarity(q_vector, doc_vectors)[0]
max_simi_i=0
# for i in range(len(simi)-1):
#   if simi[i+1]>simi[i]:
#     max_simi_i=i+1

# or by using enumerate fn it will directly attach the index number to the values give (list of tuples)
# now we can direct sort and the the max value index

modefy= [(val, ind) for (ind, val) in enumerate(simi)]

modefy.sort()

# print(documents[max_simi_i])
print(documents[modefy[-1][1]])
print(f'similarity score is {modefy[-1][0]}')