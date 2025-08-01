import uuid
from typing import Union

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from database import supabase_phone
from models import Phone

app = FastAPI()
origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/phone")
def get_all_phones():
    res_phone_datas = supabase_phone.select("*").execute()
    phone_datas = res_phone_datas.data

    return {"data": phone_datas}


@app.get("/phone/{item_id}")
def get_single_phone(item_id: int):
    res_phone_data = supabase_phone.select("*").eq("id", item_id).execute()
    phone_data = res_phone_data.data

    return {"data": phone_data}


@app.post("/phone")
async def add_phone(item: Phone):
    item_dict: Phone = item.model_dump()
    item_dict['id'] = str(uuid.uuid4())

    res_phone_data = supabase_phone.insert(item_dict).execute()
    phone_data = res_phone_data.data

    return {"data": phone_data}


@app.put("/phone/{item_id}")
def update_phone(item_id: int, item: Phone):
    item_dict: Phone = item.model_dump()

    res_phone_data = supabase_phone.update(item_dict).eq("id", item_id).execute()
    phone_data = res_phone_data.data

    return {"data": phone_data}


@app.delete("/phone/{item_id}")
def delete_phone(item_id: int):
    res_phone_data = supabase_phone.delete().eq("id", item_id).execute()
    phone_data = res_phone_data.data

    return {"data": phone_data}
