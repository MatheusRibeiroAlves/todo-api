from fastapi import FastAPI
from database.config import engine, Base



Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def root():
    return {"message": "ok"}