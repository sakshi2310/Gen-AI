from typing import TypedDict

class person(TypedDict):
    name:str
    age:int

new_person: person = {'name':'SAKSHI','age':20}

print(new_person)  


new_person_2 : person = {'name':'ANU','age':22}
print(new_person_2)