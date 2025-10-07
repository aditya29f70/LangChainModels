from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder



# now 1. first we have to create a chatTemplate
chat_template= ChatPromptTemplate([
  ('system', 'you are a helpful customer support agent!!'),
  MessagesPlaceholder(variable_name='chat_history'),
  ('human', '{query}')]
)

# let customer query --> where is my refoound --> so Ai never know what he want to say untill it don't have the previus context
# that why we create a MessagePlace holder between system message and human message
# now past very converstion bw chat and custer will autometically come in MessagePlaceholder

# 2. load the chatHistory
# that chat_history will be a txt file (use file handing)

chat_history= []
with open('chat_history.txt') as f:
  chat_history.extend(f.readlines())

print(chat_history)
# 3. create our Prompt
# now we have made a list of previus conversion message history
# now it's time to put it in the placeholder place 

prompt= chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refound ?'}) 

print(prompt)
