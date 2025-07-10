
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import csv

app = FastAPI()

DATA_PATH = "../processed/prices_processed.csv"

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Data Delivery API"}

@app.get("/data")
def get_processed_data():
    if not os.path.exists(DATA_PATH):
        return JSONResponse(content={"error": "Processed file not found."}, status_code=404)

    with open(DATA_PATH, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    return {"records": data}
