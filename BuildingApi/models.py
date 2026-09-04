from pydantic import BaseModel


class Employee(BaseModel):
    id:int
    name:str
    department:str
    age:int
    
#for strict enforcing the syntax is 
#id:int=Field(...,gt=0)    similarly others 