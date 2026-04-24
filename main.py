from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/soma")
def soma(a: int, b: int):
    return {"resultado": a + b}