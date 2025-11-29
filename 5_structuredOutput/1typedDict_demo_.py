from typing import TypedDict

class Person(TypedDict):
  name:str
  age:int


# here as person object (typedDict) will be made
# if you put your cursor on the 'name' or 'age' it will sugges you what would 
# be there answer

new_person: Person= {'name':'Adita Kumar', 'age':16}
print(new_person)


