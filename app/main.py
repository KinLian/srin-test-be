from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import main

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

app.include_router(main.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
