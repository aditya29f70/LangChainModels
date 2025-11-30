import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)

# template1= PromptTemplate(
#     template= "write a detailed report on {topic}",
#     input_variables= ['topic']
# )

# # 2nd prompt --> summary

# template2= PromptTemplate(
#     template="Write a 5 line summary on the following text. \n {text} ",
#     input_variable= ['text']
# )

parser= JsonOutputParser()

# template= PromptTemplate(
#     template="Give me the name, age and city of a fictional person \n {format_instraction}",
#     input_variables=[],
#     partial_variables= {"format_instraction": parser.get_format_instructions()}
# )


template= PromptTemplate(
    template="Tell me 5 fact about {topic} \n {format_instraction}",
    input_variables=["topic"],
    partial_variables= {"format_instraction": parser.get_format_instructions()}
)

# prompt= template.format() # not input bz it is a static prompt

# print(prompt)
# output:
# Give me the name, age and city of a fictional person 
# Return a JSON object.

# result= model.invoke(prompt)

# print(result) # you will get json output 
# nw what ever you are getting from llm json output you have to parser it with the help of parser method

# final_result= parser.parse(result.content)

# print(final_result)
# print(type(final_result)) # give you dict bz py treat json as dict (bz you are asking type py fn)

# you can write this whole code in simple way with the help of ''' chain''''
# mean you don't need to invoke the template and model separatly

chain= template | model | parser 

# result_thr_chain= chain.invoke({}) # basically you have to give input as dict of variable we you have defined in the template ; you do not any then you only {}
# print(result_thr_chain)

result= chain.invoke({"topic":"black hole"})

print(result)

"""
{'name': 'Black Holes', 'description': 'Black holes are region in spacetime where the gravitational pull is so strong that nothing, including light, can escape.', 'formation': 'Supermassive black holes are formed when a star collapses in on itself', 'size': 'Black holes can range from less than 3 times the mass of the sun to over 100 billion times the mass of the sun', 'Bending of Light': 'Light that comes near a black hole is bent by its gravity', 'Examples': 'Cygnus X-1, located about 6000 light-years away is the closest known black hole to Earth', 'Importance': 'Black holes help scientists learn about the formation of galaxies and the universe'}
"""

# what if we want a structure like fact_1: , fact_2 .... (or in this kind of schema)
# so you can't do that through jsonOutputParser




