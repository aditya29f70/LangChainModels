from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# chat_template= ChatPromptTemplate([
#   SystemMessage(content='You are a helpful {domain} expert'),
#   HumanMessage(content='Explain in simple terms, what is {topic}?')
# ])


# that is biard that some places it should work as same as we are expecting but don't like here it will directly print thing without rendering these variables 
# so this is not a good way to solve this we hav to use any other way

# so you have to sent diff structoral chat template where you have only tell that this 'system' and this is it message
# lly this 'human', and this is it's message
# baiscally tuple -> ('role': message)
# role --> sys, human , ai
# you can also use ChatPromptTemplate.from_messages --> also give some outcomes 


# chat_template= ChatPromptTemplate([
#   ('system','You are a helpful {domain} expert' ),
#   ('human', 'Explain in simple terms, what is {topic}?')
# ])


# prompt= chat_template.invoke({'domain':'Mental Health','topic':'metal health Deases'})


# print(prompt)


########################### complate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template= ChatPromptTemplate([
  ('system','You are a helpful {domain} expert' ),
  MessagesPlaceholder(variable_name= 'chat_history'),
  ('human', 'Explain in simple terms, what is {topic}?')
])

chat_history=[]
with open('chat_history.txt') as f: 
  chat_history.extend(f.readlines())

while True:
  you= input('You: ')
  if you =='exit':
    break
  result= chat_template.invoke({'chat_history': chat_history, 'domain': 'client helper', 'topic':you})
  #...chatmodel --> get AImessage like response= model(result) , then q.write(result+ AiMessage(response.content))
  with open('chat_history.txt', 'w') as q:
    q.write(result)

  

print(result)
