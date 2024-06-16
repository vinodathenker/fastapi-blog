from fastapi import FastAPI
from core.config import settings
from db.session import engine
from apis.base import api_router

def include_route(app:FastAPI):
      app.include_router(api_router)

def start_application():
      app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)      
      include_route(app)
      return app

app = start_application()

@app.get("/")
def hello():
    return {"msg":"Hello FastAPI"}
