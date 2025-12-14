## now take eg where doc has python code

from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text="""
>>> class Student:
     def __init__(self, name):
         self.name = name
         self.grades = []  # empty list of grades

     def add_grade(self, grade):
         self.grades.append(grade)
         return f"Added grade: {grade}"

     def average_grade(self):
         if not self.grades:
             return "No grades"
         return sum(self.grades) / len(self.grades)

# Creating a student
 student = Student("Maria")
 print(f"Created student: {student.name}")
Created student: Maria
 print(f"Average grade: {student.average_grade()}")
Average grade: No grades
"""

splitter= RecursiveCharacterTextSplitter.from_language(
  language= Language.PYTHON,
  chunk_size=400,
  chunk_overlap=0,
)

chunks= splitter.split_text(text)

# print(len(chunks))

# print(chunks)

print(chunks[0])
