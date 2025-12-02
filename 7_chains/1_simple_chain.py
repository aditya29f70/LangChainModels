import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm= HuggingFaceEndpoint(
  repo_id="google/gemma-2-2b-it",
  task="text-generation",
  huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)



parser= StrOutputParser()

template= PromptTemplate(
  template= ("Generate exactly 5 interesting facts about {topic}."),
  input_variables =['topic']
)


# prompt= template.invoke({'topic':'india'})

model= ChatHuggingFace(llm= llm)

# result= model.invoke(prompt)       

# final_result= parser.parse(result.content)

chain= template | model | parser 

result= chain.invoke({'topic':'india'})

print(result)   

chain.get_graph().print_ascii()

