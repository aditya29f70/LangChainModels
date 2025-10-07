from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=40)


# through that messages Ai will be knowing the context meaning of each question which
# depends on the previus response or question
messages=[
  SystemMessage(content='You are a helpful assistant!!'),
  HumanMessage(content='tell me about LangChain?')
]

result= model.invoke(messages)

messages.append(AIMessage(result.content))

print(messages)