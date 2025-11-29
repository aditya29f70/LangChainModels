import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
from pydantic import BaseModel, Field
from typing import Optional, Literal

#note you'll use Option the you have to give default value as None in pydantic

load_dotenv() 

# llm= HuggingFaceEndpoint(
#   repo_id="HuggingFaceH4/zephyr-7b-beta",
#   task= "text-generation",
#   huggingfacehub_api_token= os.getenv('HUGGINGFACEHUB_API_TOKEN')
# )


# model= ChatHuggingFace(llm= llm)


model= ChatOpenAI(model='gpt-4o-mini')



# class Review(BaseModel):
#   key_themes: list[str]= Field(description="Write down all the key themes discussed in the review in a list")
#   summary: str= Field(description='A brief summary of the review!')
#   sentiment: Literal['Pos', 'Neg', 'neu']= Field(description="Return sentiment of the review either negative, positive or neutral")
#   pros: Optional[list[str]]= Field(description='Write down all the pros inside a list')
#   cons: Optional[list[str]]= Field(description='Write down all the cons inside a list')
#   name: Optional[str]= Field(description='Write the name of reviewer')


# now try to put json schema

json_schema= {
  "title": "Review",
  "type": "object",
  "properties":{
    "key_themes":{
      "type":"array",
      "items":{
        "type":"string"
      },
      "description":"Write down all the key themes discussed in the review in a list"
    },
    "summary":{
      "type":"string",
      "descrition":"A brief summary of the review",
    },
    "sentiment":{
      "type":"array",
      "enum":["pos", "neg"],
      "description":"Return sentiment of the review either negative, positive or neutral",

    },
    "pros":{
      "type":["array", "null"],
      "items":{
        "type":"string"
      },
      "description":"Write down all the pros inside a list",
    },
    "cons":{
      "type":["array", "null"],
      "items":{
        "type":"string"
      },
      "description":"Write down all the cons inside a list"
    },
    "name":{
      "type":["string", "null"],
      "description":"Write the name of reviewer"
    }
  },
  "required":["key_themes", "summary", "sentiment"]
}
# good thing to give json review is output which we got from llm will be python dic
#  now you just have to run 


# structured_model= model.with_structured_output(Review)

structured_model= model.with_structured_output(json_schema)

result= structured_model.invoke("""
I've been using LearnSphere, an online learning platform, for nearly six months now to upskill in data analytics and AI. At first glance, the website looks sleek, and the onboarding process is simple — you can create an account and start exploring free content instantly. What drew me to LearnSphere was its promise of “personalized learning powered by AI.” In practice, this feature is quite impressive. The platform tracks your progress and weak areas, recommending new lessons or exercises tailored to your performance. The video quality is excellent, instructors are generally knowledgeable, and most courses include real-world projects that help reinforce learning.
That said, not everything is perfect. The discussion forums, which are supposed to encourage peer interaction, are often inactive or filled with repetitive questions that go unanswered. Customer support also takes too long to respond — sometimes over 48 hours — which can be frustrating if you’re stuck on an assignment. Additionally, the pricing model feels a bit confusing. There are multiple subscription tiers, and the differences between them aren’t well explained. While the platform claims to offer job placement assistance, the support is limited to resume templates and a few webinars.
Despite those downsides, I've noticed genuine improvement in my skills and confidence. The quizzes and mini-projects are thoughtfully designed, and the instructors’ feedback is often detailed. The AI mentor that suggests topics and study reminders is a nice touch, though it sometimes sends too many notifications. Overall, I think LearnSphere is an excellent tool for self-motivated learners who prefer flexibility and guided structure but don’t rely heavily on community support.
""")

# result will be pydantic object which is basically --> oop object

print(result)

"""
output:
key_themes=['User experience', 'Onboarding process', 'Personalized learning', 'Course quality', 'Instructor uctor knowledge', 'Discussion forums', 'Customer support', 'Pricing model', 'Job placement assistance'] 
summary='LearnSphere offers a sleek interface and effective personalized learning features, but struggles with community engagement and customer support.' sentiment='Pos' 
pros=['Sleek website design', 'Simple onboarding process', 'Impressive personalized learning through AI', 'Excellent video quality', 'Knowledgeable instructors', 'Real-world projects included', 'Genuine skill improvement', 'Thoughtful quizzes and projects', 'Detailed feedback from instructors'] 
cons=['Inactive discussion forums', 'Slow customer support response time', 'Confusing pricing model', 'Limited job placement assistance', 'Excessive notifications from AI mentor'] name='Anonymous'
"""


# so this is more power-full then typeddict bz if any is occured due to some validation it will direct tell me


# now next how we will do these things by using json schema
# it is used when your whole project is not mode by only using one language eg for backend you are using python
# and for frontent you are using js (so here you don't use pydantic or typeddic)

# so here we will see how to create a schema
# three four import things which you have to put inside the schema
# 1. title
# 2. description(optional) # but for us , its import (bz we are interecting with llm)
# 3 type (would be obj bz it's json)
# 4. properties
# 5. required (like unOptional)

# output got while using json_schema
"""
{'summary': 'LearnSphere is an online learning platform for data analytics and AI with a user-friendly interface and personalized learning features powered by AI. While it excels in video quality and instructor knowledge, it faces issues like inactive forums, slow customer support, and a confusing pricing model.', 'key_themes': ['online learning', 'data analytics', 'AI', 'personalized learning', 'progress tracking', 'course quality', 'customer support issues', 'pricing model', 'community interaction'], 'sentiment': ['pos'], 'pros': ['Sleek website and simple onboarding process', 'Personalized AI-powered learning', 'Effective progress tracking and recommendations', 'Excellent video quality', 'Knowledgeable instructors', 'Real-world project integration', 'Well-designed quizzes and mini-projects', 'Detailed instructor feedback'], 'cons': ['Inactive discussion forums', 'Slow customer support response', 'Confusing pricing model', 'Limited job placement assistance', 'Overwhelming notifications from AI mentor'], 'name': 'Anonymous'}
"""



# now at the last we have learnt three schema to get structure output
# 1. typed dict
# 2. pydantic
# 3. json
# now have to know which one we should where

"""
1. typed dict 
you should when 
-> you only need type hinds (basic structure enforcement)
-> you don't need validation (eg. checking numbers are positive)
-> you trust the LLM to return correct data. (very less in general)

or you can use python in whole project

2. Use pydantic 
-> you need data validation (eg. sentimate mush be 'pos', 'neg', 'neu')
-> you need default values if the LLM misses field
-> you want automatic type conversion (e.g "100" --> 100)

3. json Schema 
-> You don't want to import extra Python lib (pydrantic)
-> you need validation but don't need python objects.
-> you want to define structure in a standard  JSON format.
"""


# ############################## 
# in with_structure_out fn when you call your model by that , through 
# this fn you can also tell your model that ''through which method you want
# that structure output''' 
# in it a parameter is there -> ''method'' you can give two value in it
# 1. json mode (used when you want your structure output would be json format; most of the time it will true), 2.functional calling (after getting structure output instently you want to call a fn (used in agent) or when agent call any tool (like calculater) then you use this fn calling thing)

# rule of thumb --> if you are working with open ai model then you should use fn calling (default)
# and if you are working with other (claude, gemai) so you should use json model (bz they support json for structure output)


# and there are some model where these kind of options are not provided bz they can't give structure output --> eg HuggingFace (code will not support with _structure_output()) --> so they do not support structure output in any of them json mode or functional calling

# so here you have to apply '''output parsers yourself''' --> next lec