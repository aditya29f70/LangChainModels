import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough


load_dotenv()

llm= HuggingFaceEndpoint(
  repo_id="Qwen/Qwen2.5-1.5B-Instruct",
  task="text-generation",
  huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm)

parser= StrOutputParser()

prompt1= PromptTemplate(
  template="Generate a joke on {topic}",
  input_variables=['topic']
)

prompt2= PromptTemplate(
  template="Summarize this joke {joke}",
  input_variables=['joke']
)


joke_gen_chain= RunnableSequence(prompt1, model, parser)

parallel_chain= RunnableParallel({
  'joke': RunnablePassthrough(),
  'summarization': RunnableSequence(prompt2, model, parser)
})


chain= RunnableSequence(joke_gen_chain, parallel_chain)

result= chain.invoke({'topic': 'indian'})

print(result)