# Phone Catalogue (SRIN Test - Backend)

## Tech Stack

- Python 3.9
- FastAPI
- Pydantic
- pytest
- Supabase
- Apache Airflow

## Setup

- Clone this repo
- Move to this project directory in the terminal
- Add Python Virtual Environment

```
python -m venv .venv
```

- Run Virtual Environment
  - PowerShell : `.venv\Scripts\activate.ps1`
  - CMD : `.venv\Scripts\activate.bat`
  - Linux, macOS, WSL : `source .venv/bin/activate`
- Install all the packages needed

```
pip install -r requirements.txt
```

- Add .env to the venv **Always do it after starting the Virtual Environment** (showed only for test purposes, do not shared your .env publicly)
  - PowerShell :

```
$env:SUPABASE_URL="https://trehxrwuvxfdofrkqhxy.supabase.co"
$env:SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRyZWh4cnd1dnhmZG9mcmtxaHh5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQwNjQyMDYsImV4cCI6MjA2OTY0MDIwNn0.svmiirRPk3vCzqRpAbiJ-92DLYLLfxNwXxg7EFPIz1I"
```

- Run it locally

```
fastapi dev app/main.py
```

- BE should be running on http://127.0.0.1:8000

## Commands Available (after running venv)

- Run program : `fastapi dev app/main.py`
- Install packages : `pip install -r requirements.txt`
- Run pytest test (all) : `pytest`
- Run Apache Airflow : `airflow standalone`

## App Directory
- public/ ---------------------------- Public assets
- app/ ------------------------------- Application file
  - database.py --------------- Init database (supabase)
  - main.py --------------------- Main app
  - api/ --------------------------- API for CRUD
    - main.py --------------- CRUD Functions
  - test/ -------------------------- Unit Testing
    - test_main.py --------- Test Function for main.py
    - api ---------------------- Test Function for api/ folder
      - test_main.py --- Test Function for api/main.py

## Unit Testing Result
Unit testing always failed due to supabase mock object cannot being called

![Pytest result](./public/testing.png)

## Apache Airflow (Linux, macOS, WSL)
### Setup Apache Airflow
https://airflow.apache.org/docs/apache-airflow/stable/start.html
https://codefornepal.org/2023/02/21/data-pipeline-with-apache-airflow-and-fast-api.html
https://github.com/developer-prashant-999/Data-Pipeline-Apache-Airflow-and-Fast-API-

- Open the Virtual Environment
- Add AIRFLOW_HOME to the `.bashrc` (optional)
```
nano ~/.bashrc

# Example
AIRFLOW_HOME=~/airflow
```
- Install apache 
```
pip install apache-airflow
```
- Run airflow standalone
```
airflow standalone
```
- Open Airflow UI at http://localhost:8080/

### Updating the Apache Airflow DAGs sources
- Edit the airflow.cfg inside the located in APACHE_HOME folder to add more DAGs sources
```
nano airflow.cfg

# Example
dags_folder = /home/username/airflow/dags
```

![Apache Airflow Dashboard](./public/airflow.png)