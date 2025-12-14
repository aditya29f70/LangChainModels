## here doc content will be markdows 

from langchain.text_splitter import RecursiveCharacterTextSplitter, Language


text= """
## Data Analytics Overview

Data Analytics is the process of **analyzing raw data** to find meaningful insights.  
It involves tools like **Excel, SQL, Python, and Power BI** for data processing.

### Key Applications
- Business decision making  
- Performance tracking  
- Predictive analysis  

> Data-driven decisions help organizations grow efficiently.
"""

splitter= RecursiveCharacterTextSplitter.from_language(
  language=Language.MARKDOWN,
  chunk_size=300,
  chunk_overlap=0,
)


chunks= splitter.split_text(text)

# print(len(chunks))

# print(chunks)

print(chunks[0])


