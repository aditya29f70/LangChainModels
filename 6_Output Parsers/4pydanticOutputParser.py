import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta", 
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)


class Person(BaseModel):
    name: str= Field(description="name of the person.")
    age: int= Field(gt=18, description="Age of that person.")
    city: str= Field(description="name of the city where that person belongs to")


parser= PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {format_instractions}",
    input_variables=["place"],
    partial_variables={"format_instractions": parser.get_format_instructions()}
)

prompt= template.invoke({"place":'india'})

print(prompt)

# result= model.invoke(prompt)

# final_result= parser.parse(result.content)

# print(final_result)

# through chain

# chain= template | model | parser 

# result= chain.invoke({"place":'india'})
# print(result)