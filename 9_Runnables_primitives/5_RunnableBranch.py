import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
# from typing import Literal
from langchain.schema.runnable import RunnableSequence, RunnableBranch, RunnablePassthrough, RunnableLambda
from pydantic import BaseModel, Field
from dotenv import load_dotenv


load_dotenv()

llm= HuggingFaceEndpoint(
  repo_id="Qwen/Qwen2.5-1.5B-Instruct",
  task='text-generation',
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)

class About_report(BaseModel):
  report: str= Field("Generated report")

parser =PydanticOutputParser(pydantic_object= About_report)
parser1= StrOutputParser()


prompt= PromptTemplate(
  template="Generate a report on this topic {topic} \n {format_instractions}",
  input_variables=['topic'],
  partial_variables={"format_instractions": parser.get_format_instructions()}
)

prompt1= PromptTemplate(
  template="Summarize this report \n {report}",
  input_variables=['report']
)

seq_chain= RunnableSequence(prompt, model, parser)

chain_branch= RunnableBranch(
  (lambda x: len(x.report.strip().split())> 500, RunnableSequence(prompt1, model, parser1)),
  # RunnableLambda(lambda x: RunnablePassthrough())
  # or directly
  RunnablePassthrough()
)

chain= RunnableSequence(seq_chain, chain_branch)

result= chain.invoke({"topic": 'indian'})

print(result)
