from fastapi import FastAPI
from app.db import Base, engine
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

app.include_router(router)
