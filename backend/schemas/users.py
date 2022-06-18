from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserShow(BaseModel):
    username: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True
