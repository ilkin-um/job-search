from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    email: str
    password: str


class ShowUser(BaseModel):
    username: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True
