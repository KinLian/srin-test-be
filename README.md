# Phone Catalogue (SRIN Test - Backend)

## Setup

- Clone this repo
- Add virtual environment

```
python -m venv .venv
```

- Run Virtual Environment (Windows)
  - PowerShell : `.\myenv\Scripts\activate.ps1`
  - Bash : `.\myenv\Scripts\activate.bat`
- Install packages needed

```
pip install -r requirements.txt
```

- Add .env (showed only for test purposes, do not shared your .env publicly)

```
$env:SUPABASE_URL="https://trehxrwuvxfdofrkqhxy.supabase.co"
$env:SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJpc3MiOiJzdXBhYmFzZSIsIJlZiI6InRyZWh4cnd1dnhmZG9mcmtxaHh5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQwNjQyMDYsImVcCI6MjA2OTY0MDIwNn0.svmiirRPk3vCzqRpAbiJ-92DLYLLfxNwXxg7EFPIz1I"
```

- Run it locally (windows)

```
fastapi dev main.py
```

- BE should be running on http://127.0.0.1:8000
