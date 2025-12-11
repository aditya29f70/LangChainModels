import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task= 'text-generation',
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)


model= ChatHuggingFace(llm= llm)


prompt= PromptTemplate(
    template="Suggest a catchy blog title about {topic}.",
    input_variables=['topic']
)

# define the input
topic= input('Enter a topic!')

# format the prompt manually using promptTemplate
formatted_prompt= prompt.format(topic= topic)

# call the llm directly
blog_title= model.predict(formatted_prompt)

# print the output
print("Generated blog title :", blog_title)





