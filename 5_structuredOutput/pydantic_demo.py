# now i have to make a student dict where we have to setup there information
# where if i set some attribute with some datatype i 'must' be that 

# pydantic also very useful for FastApi validatation (for security perpose) that api you geting must follow some criteria

# so for use perpose you have to install it first --> pip install pydantic


from pydantic import BaseModel
from typing import Optional

# just like TypedDict here also you make classes

class Student(BaseModel):
    name: str= 'nitish'
    age: Optional[int]= None

# new_student= {'name':'Aditya'}

# student= Student(**new_student)

# print(student)  # --> it is ok gives you pydantic obj

#now if 
# new_student2= {'name': 32}

# student= Student(**new_student2) # --> dir give you error , telling input should be valid str
# that what we want , which is typedDict coouldn't give

# 2. thing is how to set default value in pydantic
# name: str = 'nitish'

# new_student3= {}
# student= Student(**new_student3) # for default value set

# print(student.name) 




# 3. 'Optional' fields -> if that context present then only give
# lly use 'Option' lib from typing > but you have to set some default value like None if you don't want to put anything

# new_student4= {'age':32}
# student= Student(**new_student4)

# print(student)


# 4. that is new and good thing of pydantic is that , it try to analys that what kind of data you have given , and if it's possible of it that data convergens part it will do that ->it is also called -> Coerce -> '''type coercing( this name is called in python )''''

# eg in you pydantic shema you have defined that age should be int if you make a student and mistakely put it's age as str number then it will auto matically analys that and give you int age

# new_student= {'age':'32'}

# student= Student(**new_student)

# print(student)

## 5. Builting validation