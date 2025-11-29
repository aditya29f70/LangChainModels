# now i have to make a student dict where we have to setup there information
# where if i set some attribute with some datatype i 'must' be that 

# pydantic also very useful for FastApi validatation (for security perpose) that api you geting must follow some criteria

# so for use perpose you have to install it first --> pip install pydantic


from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# just like TypedDict here also you make classes

class Student(BaseModel):
    name: str= 'nitish'
    age: Optional[int]= None
    email: EmailStr

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

# in python it is called python coerce

## 5. Builting validation
# there is something with the help of that you can perform validation check in pydantic eg
# you can validate email by using --> EmailStr


# new_student= {'age':'32', 'email': 'abc@gmail.com'} # since it is not a correct email so it will through error

# student= Student(**new_student)

# print(student)

# so such build in validation you will get in pydantic

###  6. Feild fn (by using this you can set default values, can apply any kind of contrain , can give a description of any value, and can apply reg-expresion)
# first see how to apply 'constraints' for that we have to import 'Feild' fn

# and also you can give it's default value inside the field as well

# now you can put constum description (like what this value want or representing)
# lly it is doing like in typedicp we had annotation ; so we will be using it for the same purpus


# you can also add  reg expresation if you want to add your phone number(like if this pattern is not matching then don't accept this phone number)



class Student_with_constraint(BaseModel):
    name: str= 'Aditya'
    age: Optional[int]=None 
    email: Optional[EmailStr]=None
    cgpa: float= Field(gt=0, lt=10, default=5, description='decimal value representing cgpa of a student!!') # gt= greater than, lt= less than
    phone_number: str= Field(pattern=r"[+]")



# student_with_c= Student_with_constraint()

student_with_c= Student_with_constraint(phone_number='+')

# print(student_with_c)

## 7. when it is made, its a pydantic object 
# if you want you can convert it to python dic or json 

student_with_c_convert_to_dic= dict(student_with_c)

# print(student_with_c_convert_to_dic)
# print(student_with_c_convert_to_dic['name'])

student_with_c_convert_to_json= student_with_c.model_dump_json()

print(student_with_c_convert_to_json)

# now let go to see how with_structure_output fn use along side pydantic
