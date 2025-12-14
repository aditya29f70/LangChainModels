from langchain.text_splitter import RecursiveCharacterTextSplitter

text= """
satellite or an artificial satellite[a] is an object, typically a spacecraft,
placed into orbit around a celestial body. They have a variety of uses, including
communication relay, weather forecasting, navigation (GPS), broadcasting, 
scientific research, and Earth observation. Additional military uses are 
reconnaissance, early warning, signals intelligence and, potentially, weapon 
delivery.

Other satellites include the final rocket stages that place satellites 
in orbit and formerly useful satellites that later become defunct.
Except for passive satellites, most satellites have an electricity generation 
system for equipment on board, such as solar panels or radioisotope thermoelectric
generators (RTGs).
"""

# print(len("""
# satellite or an artificial satellite[a] is an object, typically a spacecraft,
# placed into orbit around a celestial body.
# """))
# print(len("""
# They have a variety of uses, including
# communication relay, weather forecasting, navigation (GPS), broadcasting, 
# scientific research, and Earth observation. 
# """))
# print(len("""
# Additional military uses are 
# reconnaissance, early warning, signals intelligence and, potentially, weapon 
# delivery.
# """))

# print(len("""
# Other satellites include the final rocket stages that place satellites 
# in orbit and formerly useful satellites that later become defunct.
# """))
# print(len("""
# Except for passive satellites, most satellites have an electricity generation 
# system for equipment on board, such as solar panels or radioisotope thermoelectric
# generators (RTGs).
# """))

# Initialize the splitter
splitter= RecursiveCharacterTextSplitter(
  chunk_size=400,
  chunk_overlap=0,
)

chunks= splitter.split_text(text)

print(len(chunks))

print(chunks)

