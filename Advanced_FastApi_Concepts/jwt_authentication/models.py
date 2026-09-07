from pydantic import BaseModel

class User(BaseModel):
    username : str
    password : str

class UserinDB(User):
    hashed_password : str