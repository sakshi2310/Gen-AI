from pydantic import BaseModel,EmailStr , Field
from typing import Optional

class student(BaseModel):
    name : str
    name : str = "Sakshi"  # Set the default value
    age : Optional[int] = None  # OptiOnal value
    email : EmailStr
    cgpa : float = Field(gt=0,lt=10,default=5) # add the constrains
    cgpa : float = Field(gt=0,lt=10,default=5,description="A decimal value of represnting the cgpa of the student") # add the description


# new_student = {'name':32}   # Through the error

new_student = {'age':'32'} # Type coursing pydantic automatically change the datatype 
new_student = {'name':'sakshi'}






student = student(**new_student)

print(student)
print(type(student))
print("Student Dict : ",dict(student))

# this code not execute for the excuation pass all the parameters properly