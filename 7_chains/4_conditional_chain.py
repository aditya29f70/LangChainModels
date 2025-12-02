import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()


llm1= HuggingFaceEndpoint(
  repo_id="Qwen/Qwen2.5-1.5B-Instruct",
  task= "text-generation",
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

llm2= HuggingFaceEndpoint(
  repo_id="HuggingFaceH4/zephyr-7b-beta",
  task= "text-generation",
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model1= ChatHuggingFace(llm= llm1)
model2= ChatHuggingFace(llm= llm2)





# parser= StrOutputParser()

# prompt1= PromptTemplate(
#   template="Classify the sentiment of the following feedback text into positive or negative \n {feedback}",
#   input_variables=["feedback"]
# )


# classifier_chain= prompt1 | model1 | parser

# feedback= "I recieved my parser by there was lot damages in my product"

# result= classifier_chain.invoke({"feedback": feedback})

# print(result)





class Schema(BaseModel):
  sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback either positive or negative")


parser= PydanticOutputParser(pydantic_object=Schema)

parser1= StrOutputParser()

prompt1= PromptTemplate(
  template="Give the sentiment analysis of this feedback {feedback} \n {format_instractions}",
  input_variables=["feedback"],
  partial_variables={"format_instractions": parser.get_format_instructions()}
)


prompt2= PromptTemplate(
  template="Write an appropriate response to this postive response feedback \n {feedback}",
  input_variables=['feedback']
)

prompt3= PromptTemplate(
  template="Write an appropriate response to this negative response feedback \n {feedback}",
  input_variables=['feedback']
)



classifier_chain= prompt1 | model1 | parser 



#  now the sentiment analysis work done now we have to work on this branching model

# since we don't have any default chain so we use lambda fn at last also to sent a message that we could not able to find the sentiment
# since what ever thing which take in default which would also be chain so we can only sent text message we have to make it thought any chain , so 
# we have to change this lambda fn in any runnable --> using called --> runnable lambda
# so its convert a lambda fn in runnable --> once it is converted in runnable so we can use it as chain


# this is kind of if/else statement in langchain world
branch_chain= RunnableBranch(
  (lambda x: x.sentiment =='positive', prompt2 | model1 | parser1),
  (lambda x: x.sentiment =='negative', prompt3 | model2| parser1),
  RunnableLambda(lambda x: "could not find sentiment")
)

# the classifier chain output will be it's input which giving a dict which key is sentiment and it's value

chain= classifier_chain | branch_chain

feedback="the product which i recieved that was not my project which i ordered."

result= chain.invoke({"feedback": feedback})

print(result) # we can directly able to print bz we took stroutput parser

chain.get_graph().print_ascii()


"""
    +-------------+      
    | PromptInput |
    +-------------+
            *
            *
            *
   +----------------+
   | PromptTemplate |
   +----------------+
            *
            *
            *
  +-----------------+
  | ChatHuggingFace |
  +-----------------+
            *
            *
            *
+----------------------+
| PydanticOutputParser |
+----------------------+
            *
            *
            *
       +--------+
       | Branch |
       +--------+
            *
            *
            *
    +--------------+
    | BranchOutput |
    +--------------+
"""