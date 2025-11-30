import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema, OutputFixingParser
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm= llm)


# let suppose i want three fact
# your schema is here
schema= [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic.'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic.'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic.')
]

# parser is here
parser= StructuredOutputParser.from_response_schemas(schema)


# prompt here
template= PromptTemplate(
    template='Give me 3 fact about {topic} \n {format_instructions}',
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


# prompt= template.invoke({"topic":"black hole"})



# result = model.invoke(prompt)
# print(result.content)
# or

# final_result= parser.parse(result.content)
# print(final_result)

# fixing_parser= OutputFixingParser.from_llm(parser=parser, llm=model)
# final_result= fixing_parser.parse(result.content)


# chain (pipeline)
chain= template | model | parser 

result= chain.invoke({"topic": 'black hole'})

print(result)

# now try to know the desadvantage of that 




