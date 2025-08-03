import uuid

from app.database import supabase_phone
from app.models.phone import Phone
from fastapi import APIRouter

router = APIRouter()


@router.get("/phone", tags=["phone"])
def get_all_phones():
    res_phone_datas = supabase_phone.select("*").execute()
    phone_datas = res_phone_datas.data

    return {"data": phone_datas}


@router.get("/phone/{item_id}", tags=["phone"])
def get_single_phone(item_id: str):
    res_phone_datas = supabase_phone.select().eq("id", item_id).execute()
    phone_datas = res_phone_datas.data
    single_phone_data = phone_datas[0] if len(phone_datas) == 1 else None

    return {"data": single_phone_data}


@router.post("/phone", tags=["phone"])
def add_phone(item: Phone):
    item_dict: Phone = item.model_dump()
    item_dict['id'] = str(uuid.uuid4())

    res_phone_data = supabase_phone.insert(item_dict).execute()
    phone_data = res_phone_data.data

    return {"data": phone_data}


@router.put("/phone/{item_id}", tags=["phone"])
def update_phone(item_id: str, item: Phone):
    item_dict: Phone = item.model_dump()
    item_dict['id'] = item_id

    res_phone_data = supabase_phone.update(
        item_dict).eq("id", item_id).execute()
    phone_data = res_phone_data.data

    return {"data": phone_data}


@router.delete("/phone/{item_id}", tags=["phone"])
def delete_phone(item_id: str):
    res_phone_data = supabase_phone.delete().eq("id", item_id).execute()
    phone_data = res_phone_data.data

    return {"data": phone_data}
