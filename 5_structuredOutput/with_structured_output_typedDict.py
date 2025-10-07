from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model= ChatOpenAI()


# normally you after above step you next step is invoke but it will not give you
# structure data you have to tell to give that 

# so now first thing is you have to create a schema how would your schema looks

class Review(TypedDict):

  # summary:str
  # sentiment:str
  # instead to give only shema type now you can also give description

  summary: Annotated[str, 'A brief summary of the review!']
  sentiment: Annotated[str, 'Return sentiment of the review either negative, positive or neutral']

# now called to with_structured_output() fn on on model with 
# what would be structure of output 'Review'

structured_model= model.with_structured_output(Review)
# now this model has that schema 'Review' defination that how would our outcome structe looks like 
# now instead of invokeing model now invoke this modeifed model

result= structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre- intalled apps that i can't remove. Also, the UI looks outdated compared to other brand, Hoping for a softare update to fix this""")

print(result)


# what is happening here ; like i am only giving that a Review class obj
# and my model know what i want to know (mean here i don't need to ask or specify what i want)
# --> when you call with_structure_output() and structure proved or schema provide 
# behind the screen one system promt is generated 
'''
look like this -> 
you are Ai assistant that extracts structured insights from text.Give a prompt review, 
extract: - summary: A brief overview of the main points. -Sentiment: Overall tone of the review (positive, neutral, negative)
return the response in JSON format
'''


#now see more things if you are making schema with the help of TypedDict
# --> Annotated TypedDict

# so what can happens --> so in shema where you only giving the as key points and aspecting that 
# llm model can know what i want -->sometime may be it can't able to know what you want only given key word
# so at the key word you can also guide you llm --> you can attached a line
# --> that is called annotation --> so for this import Annotated from typing


##### now try to parse some more complex Review
# let we have some large review --> here we don't only want summary and sentimant 
# also want to know key topics( here someone discuss about charging , processor or like these key topic)

# and second --> we want all the pros at one position and cons at one position will come
# and also if there is not any pros or cons then don't give it ( mean if want to take this as a option things)

# step-1 copy you big review that you had and put it at model.invoke('text_review'<--here)
# 


# at 30: min