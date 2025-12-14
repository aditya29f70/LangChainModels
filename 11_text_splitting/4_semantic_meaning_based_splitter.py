from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


load_dotenv()

embeddings= HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")


text= """
Farmers were working hard in the fields, preparing the soil and planting seeds for 
the next season. The sun was bright, and the air smelled of earth and fresh grass.
The Indian Premier League (IPL) is the biggest cricket league in the world. People
all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. It causes harm to people and creates 
fear in cities and villages. When such attacks happen, they leave behind pain and 
sadness. To fight terrorism, we need strong laws, alert security forces, and support 
from people who care about peace and safety.
"""

## now tell me how many chunks should be had for this text
## if you see it directly then you guess would be 2

## but if you read if then you will realise there would be 3 chunks

## if you use RecursiveCharactorSplitter then most probabily it will divide this text into two chunks for it it very hard to divide this 
# into 3 chunks which semantically correct

######### in such situation semantic-meaning-based-splitter helps us

# here we don't take decision according text length or structor instead it take decision according to it's text meaning if anywhere it feels text has diff meaning
# it just splitte text at that position (it is at experimental stage) --> sir tried but did get good results

# --> how it works ==> it split text in sentences and according to each sentance it create it's embedding vectors ==> compare s1 sentance vector with s2 for similarity
# lly s2-> s3, s3-> s4 ...etc and at that position where similarity bw pair is very less mean that is point where context change so that have to split it at that position


splitter= SemanticChunker(
  embeddings , breakpoint_threshold_type='standard_deviation',breakpoint_threshold_amount=1
)

# standard_deviation mean data which comming from when we were checking for similarity (those similarity data) we first find those data std , and that would be parameter of finding that splite
# and breakpoint_threshold_amount=1 mean if at any point similarity greater than 1 std then that point we will take as splitter point


chunks= splitter.split_text(text)

print(len(chunks))
print(chunks)


## as of now it is not giving me good results (RecursiveTextSpliter is best for now )