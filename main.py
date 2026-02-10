from fastapi import FastAPI
from storage import load_items, save_items

app = FastAPI()

@app.get("/")
def root():
    return {"Hola": "User!"}
