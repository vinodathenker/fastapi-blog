from fastapi import APIRouter, Depends
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.repository.blog import list_blog
from db.session import get_db


templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/")
def home(request:Request, db:Session= Depends(get_db)):
    blogs = list_blog(db=db)
    context = {"request":request,"blogs":blogs}
    return templates.TemplateResponse("blogs/home.html",context=context)
