from pydantic import BaseModel
from fastapi import Form

class Phone(BaseModel):
    id: str = None
    model: str = Form(...)
    price: str = Form(...)
    processor: str = Form(...)
    ram: str = Form(...)
    battery: str = Form(...)
    display: str = Form(...)
    camera: str = Form(...)
    card: str = Form(...)
    os: str = Form(...)