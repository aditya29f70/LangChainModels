import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableSequence
from pydantic import BaseModel, Field
from dotenv import load_dotenv


load_dotenv()

llm= HuggingFaceEndpoint(
  repo_id="Qwen/Qwen2.5-1.5B-Instruct",
  task= "text-generation",
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)


class Joke(BaseModel):
  joke: str= Field('Generated joke')

parser1= PydanticOutputParser(pydantic_object=Joke)


# parser2= StrOutputParser()
class Summarizer(BaseModel):
  joke: str= Field('Generated joke'),
  summarizer: str= Field('Summarization of that joke')

parser2= PydanticOutputParser(pydantic_object=Summarizer)

prompt= PromptTemplate(
  template="Generate a joke on {topic} \ {format_instruction}",
  input_variables=['topic'],
  partial_variables= {"format_instruction": parser1.get_format_instructions()}
)

prompt1= PromptTemplate(
  template="Summaries this joke {joke} \ {format_instraction}",
  input_variables=['joke'],
  partial_variables={"format_instraction": parser2.get_format_instructions()}
)

# chain= prompt | model | parser 

chain= RunnableSequence(prompt, model, parser1, prompt1, model, parser2)

result= chain.invoke({'topic': "Ai"})

print(result)
