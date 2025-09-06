from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model= ChatAnthropic(model="claude-opus-4-1-20250805", temperature=0.2, max_tokens_to_sample=10)

result= model.invoke("what is the capital of india?")

print(result)
