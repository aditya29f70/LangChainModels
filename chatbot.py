# import os
# from transformers import pipeline
# from langchain_huggingface import  HuggingFacePipeline

# genertor= pipeline('text-generation', model='distilgpt2', max_new_tokens=100, temperature=0.7)


# model= HuggingFacePipeline(pipeline= genertor)

# llm= HuggingFacePipeline.from_model_id(
#   model_id="distilgpt2",
#   task="text-generation", 
#   pipeline_kwargs= dict(
#     temperature= 0.8,
#     max_new_tokens= 80
#   )
# )

# model= ChatHuggingFace(llm= llm)

# while True:
#   user_input= input('you: ')
#   if user_input== 'exit':
#     break

#   result= model.invoke(user_input)
#   print('AI: ', result)





from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model= ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=50)


# chat_history=[]
messages= [
  SystemMessage(content='You are a helpful Ai assistant!!')
]
# here , basically we are assigning the role to this ai assistant

while True:
  user_input= input('You: ')
  messages.append(HumanMessage(content= user_input))
  # chat_history.append(user_input)
  if user_input== 'exit':
    break
  # result= model.invoke(chat_history)
  result= model.invoke(messages)
  # chat_history.append(result.content)
  messages.append(AIMessage(content= result.content))
  print('AI: ',result.content)

# print(chat_history)
print(messages)