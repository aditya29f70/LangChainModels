from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model= ChatOpenAI()


# normally you after above step you next step is invoke but it will not give you
# structure data you have to tell to give that 

# so now first thing is you have to create a schema how would your schema looks

class Review(TypedDict):

  # summary:str
  # sentiment:str
  # instead to give only shema type now you can also give description

  key_themes: Annotated[list[str], 'Write down all the key themes discussed in the review in a list']
  summary: Annotated[str, 'A brief summary of the review!']
  sentiment: Annotated[Literal['Pos', 'neg'], 'Return sentiment of the review either negative, positive or neutral']
  pros: Annotated[Optional[list[str]], 'Write down all the pros inside a list']
  cons: Annotated[Optional[list[str]], 'Write down all the cons inside a list']
  name: Annotated[Optional[str], 'Write the name of reviewer']


# now called to with_structured_output() fn on on model with 
# what would be structure of output 'Review'

structured_model= model.with_structured_output(Review)
# now this model has that schema 'Review' defination that how would our outcome structe looks like 
# now instead of invokeing model now invoke this modeifed model

# result= structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre- intalled apps that i can't remove. Also, the UI looks outdated compared to other brand, Hoping for a softare update to fix this""")

# print(result)


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
# step2 --> add one more shema attribute -> key_themes -> would we list bz multiple thems possible

# step3 --> add proms shema in typedDict --> option--> so for this we use Optional module from typing

# step4 --> lly cons --> option

# if i want that in 'sentimate' response would give post or neg instead of full ward --> for this you have  'Literal' obj in typing




result= structured_model.invoke(""" I’ve been using LearnSphere, an online learning platform, for nearly six months now to upskill in data analytics and AI. At first glance, the website looks sleek, and the onboarding process is simple — you can create an account and start exploring free content instantly. What drew me to LearnSphere was its promise of “personalized learning powered by AI.” In practice, this feature is quite impressive. The platform tracks your progress and weak areas, recommending new lessons or exercises tailored to your performance. The video quality is excellent, instructors are generally knowledgeable, and most courses include real-world projects that help reinforce learning.

That said, not everything is perfect. The discussion forums, which are supposed to encourage peer interaction, are often inactive or filled with repetitive questions that go unanswered. Customer support also takes too long to respond — sometimes over 48 hours — which can be frustrating if you’re stuck on an assignment. Additionally, the pricing model feels a bit confusing. There are multiple subscription tiers, and the differences between them aren’t well explained. While the platform claims to offer job placement assistance, the support is limited to resume templates and a few webinars.

Despite those downsides, I’ve noticed genuine improvement in my skills and confidence. The quizzes and mini-projects are thoughtfully designed, and the instructors’ feedback is often detailed. The AI mentor that suggests topics and study reminders is a nice touch, though it sometimes sends too many notifications. Overall, I think LearnSphere is an excellent tool for self-motivated learners who prefer flexibility and guided structure but don’t rely heavily on community support.""")

print(result)
print(result['summary'])
print(result['sentiment'])




# this works good --> but there is only one problem --> there is not any gerently that what ever you have
# design you shema like somethings would be in 'list' or 'str' will be come as you have metioned
# there is positivility that you want 'str' it is giving you list -->so there is posibility that 
# your llm model can be wrong

## finally mean you can use '''datavalidation'' here ; so typedDict only for represention learning porpush
############## so for datavalidation you have another shema designer ==> called '''pydantic'''





 



