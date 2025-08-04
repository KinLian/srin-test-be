from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import csv

import random
import requests
from pydantic import BaseModel


class Phone(BaseModel):
    id: str = None
    model: str
    price: str = None
    processor: str = None
    ram: str = None
    battery: str = None
    display: str = None
    camera: str = None
    card: str = None
    os: str = None


def create():
    random_number = random.randint(1, 100000000)
    model_name = "MODEL " + str(random_number)
    new_phone = Phone(model=model_name)
    new_phone_json = new_phone.model_dump_json()

    requests.post('http://127.0.0.1:8000/phone', json=new_phone_json)


def convert_to_csv():
    response = requests.get('http://127.0.0.1:8000/phone')
    phone_datas = [Phone(**data) for data in response.json()['data']]
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for phone in phone_datas:
            writer.writerow([phone.model, phone.price, phone.os])

# ---------------------------------------------------------------------------------


with DAG(
    "create_then_savefile",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=10),
    },
    description="Create then save to data.csv",
    schedule=timedelta(hours=12),
    start_date=datetime(2025, 8, 1),
    catchup=False,
    tags=["custom"],
) as dag:

    t1 = PythonOperator(
        task_id="create_random_phone",
        python_callable=create
    )

    t2 = PythonOperator(
        task_id="convert_to_csv",
        python_callable=convert_to_csv
    )

    t1 >> t2
