from pydantic import BaseModel

class Chip(BaseModel):
    name: str
    module: str
    class Config():
        orm_mode = True
