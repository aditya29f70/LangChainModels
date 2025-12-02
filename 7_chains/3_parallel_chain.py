import os 
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel

load_dotenv()

llm1 = HuggingFaceEndpoint(
  repo_id="Qwen/Qwen2.5-1.5B-Instruct",
  task="text-generation",
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

# llm2= HuggingFaceEndpoint(
#   repo_id= "moonshotai/Kimi-K2-Thinking",
#   task="text-generation",
#   huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

llm3= HuggingFaceEndpoint(
  repo_id="HuggingFaceH4/zephyr-7b-beta",
  task="text-generation",
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
)


model1= ChatHuggingFace(llm= llm1)
# model2= ChatHuggingFace(llm= llm2)
model3= ChatHuggingFace(llm= llm3)



prompt1= PromptTemplate(
  template="Generate short and simple notes from the following text \n {text}",
  input_variables=['text']
)

prompt2= PromptTemplate(
  template="Generate 5 short questions answers from the following text \n {text}",
  input_variables=['text']
)

prompt3= PromptTemplate(
  template="merage the provided notes and quiz into a single document \n notes --> {notes} \n quiz --> {quiz} ",
  input_variables=['notes', 'quiz']
)


parser= StrOutputParser()


# now make parallel chain

parallel_chain= RunnableParallel({
  "notes": prompt1 | model1 | parser ,
  "quiz": prompt2 | model3 | parser
})


# now time to make that merge chain (simple sequncecial chain)

merge_chain= prompt3 | model1 | parser

# final chain
chain= parallel_chain | merge_chain


text= """
In statistics, linear regression is a model that estimates the relationship between a scalar response (dependent variable) and one or more explanatory variables 
(regressor or independent variable). A model with exactly one explanatory variable is a simple linear regression; a model with two or more explanatory variables is a
 multiple linear regression.This term is distinct from multivariate linear regression, which predicts multiple correlated dependent variables rather than a single dependent variable.
In linear regression, the relationships are modeled using linear predictor functions whose unknown model parameters are estimated from the data. Most commonly,
 the conditional mean of the response given the values of the explanatory variables (or predictors) is assumed to be an affine function of those values; less commonly,
 the conditional median or some other quantile is used. Like all forms of regression analysis, linear regression focuses on the conditional probability distribution
 of the response given the values of the predictors, rather than on the joint probability distribution of all of these variables, which is the domain of multivariate
 analysis.
"""

result= chain.invoke({"text":text})

print(result)


chain.get_graph().print_ascii()


"""
              +---------------------------+
              | Parallel<notes,quiz>Input |
              +---------------------------+
                  ***               ***
               ***                     ***
             **                           **
+----------------+                    +----------------+
| PromptTemplate |                    | PromptTemplate |
+----------------+                    +----------------+
          *                                   *
          *                                   *
          *                                   *
+-----------------+                  +-----------------+
| ChatHuggingFace |                  | ChatHuggingFace |
+-----------------+                  +-----------------+
          *                                   *
          *                                   *
          *                                   *
+-----------------+                  +-----------------+
| StrOutputParser |                  | StrOutputParser |
+-----------------+                  +-----------------+
                  ***               ***
                     ***         ***
                        **     **
             +----------------------------+
             | Parallel<notes,quiz>Output |
             +----------------------------+
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
                  +-----------------+
                  | StrOutputParser |
                  +-----------------+
                            *
                            *
                            *
                +-----------------------+
                | StrOutputParserOutput |
                +-----------------------+
"""