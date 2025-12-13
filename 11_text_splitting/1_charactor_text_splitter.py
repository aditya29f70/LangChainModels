from langchain.text_splitter import CharacterTextSplitter

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
generators (RTGs). Most satellites also have a method of communication to ground 
stations, called transponders. Many satellites use a standardized bus to save cost 
and work, the most popular of which are small CubeSats. Similar satellites can 
work together as groups, forming constellations. Because of the high launch cost 
to space, most satellites are designed to be as lightweight and robust as possible.
Most communication satellites are radio relay stations in orbit and carry dozens of
transponders, each with a bandwidth of tens of megahertz.
"""

splitter= CharacterTextSplitter(
  chunk_size=100,  # how many char should be in a chunk
  chunk_overlap=0,
  separator= '' # at that position where we are done with 100 char just go to next chunk
)

result= splitter.split_text(text)

print(result)

## now try to do text spliting with document loaders so i will load a pdf and then apply 
# char text splitter on it