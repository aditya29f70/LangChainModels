import os
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm= HuggingFaceEndpoint(
  repo_id="HuggingFaceH4/zephyr-7b-beta",
  task="text-generation",
  huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_API_TOKEN")
  )

model= ChatHuggingFace(llm=llm)

template= load_prompt('template.json')

st.header('Reasearch Tool')

paper_input= st.selectbox("Select Reaserch Paper Name", ["Attention is All you need", "BERT: Pre-training Deep Bidirectional Transformers", "GPT-3:Language Model are few-shot Learners", "Diffusion Model Beat GANs on Image Synthesis"])

style_input= st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

lenght_input= st.selectbox("Select Explanation Lenght",["Short(1-2 paragraphs)", "Medium(3-5 paragraph)", "Long(detailed explanation)"])





if st.button('Summarize'):
  chain= template | model
  result= chain.invoke({
  'paper_input':paper_input,
  'style_input':style_input,
  'lenght_input':lenght_input
  })

  st.write(result.content)

# # now i will fill the placeHolders
## now you don't need to invoke template bz chain will invoke it with that dict and there output attomatically go into model
#   prompt= template.invoke({
#   'paper_input':paper_input,
#   'style_input':style_input,
#   'lenght_input':lenght_input
#   }
#   )

  # result= model.invoke(prompt)
  # st.write(result.content)


# command for running these steamlit --> steamlit run your_file_name(prompt_ui.py)
# after that steamlit will create a server where you can open you ui



