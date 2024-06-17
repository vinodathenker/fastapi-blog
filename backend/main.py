from fastapi import FastAPI
from core.config import settings
from db.session import engine
from apis.base import api_router
from apps.base import app_router
from fastapi.staticfiles import StaticFiles

def include_route(app:FastAPI):
      app.include_router(api_router)
      app.include_router(app_router)

def configure_staticfiles(app:FastAPI):
      app.mount("/static", StaticFiles(directory="static"), name="static")      

def start_application():
      app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)      
      include_route(app)
      configure_staticfiles(app)
      return app

app = start_application()

