import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 


load_dotenv()


llm = HuggingFaceEndpoint(
  repo_id="Qwen/Qwen2.5-1.5B-Instruct",
  task="text-generation",
  huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model= ChatHuggingFace(llm= llm) 

parser= StrOutputParser()

prompt1= PromptTemplate(
  template= "Generate a tweet for my twitter on the topic of {topic}",
  input_variables=['topic']
)

prompt2= PromptTemplate(
  template= "Generate a linkedin post for me on the topic of {topic}",
  input_variables=['topic']
)

prompt3= PromptTemplate(
  template="merge both of the posts for twitter and linkedin {tweet} \n\n {post}",
  input_variables=['tweet', 'post']
)



parallel_chain= RunnableParallel({
  'tweet': RunnableSequence(prompt1 , model , parser),
  'post': RunnableSequence(prompt2, model, parser)
})
## see output of this parallele_chain will be that dict


result= parallel_chain.invoke({'topic': 'Indian'})

# merage_chain= RunnableSequence(prompt3, model, parser)

# chain= RunnableSequence(parallel_chain, merage_chain)

# result= chain.invoke({'topic':'AI'})

print(result)