from fastapi import FastAPI
from database.config import engine, Base
from routers.tasks import router as tasks_router



Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(tasks_router)


@app.get("/")
def root():
    return {"message": "ok"}


