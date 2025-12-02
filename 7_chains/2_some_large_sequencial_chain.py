import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.output_parsers import StrOutputParser



load_dotenv()

llm = HuggingFaceEndpoint(
  repo_id="Qwen/Qwen2.5-1.5B-Instruct",
  task="text-generation",
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)

# class Schema(BaseModel):
#   name: str= Field(description="That person's name")
#   age: int= Field(gt=18, description="That person age")

# parser= PydanticOutputParser(pydantic_object=Schema)

# prompt= PromptTemplate(
#   template="Generate information about a person who belongs to {place} \n {format_instractions}",
#   input_variables=['place'],
#   partial_variables={"format_instractions": parser.get_format_instructions()}
# )

# chain= prompt | model | parser 

# result= chain.invoke({"place":'india'})
# print(result)


parser= StrOutputParser()

prompt1= PromptTemplate(
  template="Generate a detail report on {topic}",
  input_variables=['topic']
)

prompt2= PromptTemplate(
  template="Generate a 5 pointer summary from the following text \n {text}",
  input_variables=['text']

)

chain= prompt1 | model | parser | prompt2 | model | parser 

result= chain.invoke({"topic": 'Unemployment in india'})

print(result)

chain.get_graph().print_ascii()


# model-> parser first bz output from model as lot of thing like content and lot of meta data but we only need content so 
# parser is import to we get a structure content
