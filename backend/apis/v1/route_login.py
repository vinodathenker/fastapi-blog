from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JOSEError

from core.config import settings
from db.session import get_db
from core.hashing import Hasher
from core.security import create_access_token
from db.repository.login import get_user_by_email

router = APIRouter()

def authenticate_user(email:str, password:str, db:Session):
    user = get_user_by_email(email=email, db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    return user

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(detail=f"Incorrect email or password",status_code=status.HTTP_401_UNAUTHORIZED)
    
    access_token = create_access_token(data={"sub":user.email})
    
    return {"access_token": access_token, "token_type":"bearer"}



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def get_current_user(token: str = Depends(oauth2_scheme) , db: Session = Depends(get_db)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials, Please Login Again"
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        email: str = payload.get("sub")
        if email is None:
            raise credential_exception
    except JOSEError:
        raise credential_exception
    user = get_user_by_email(email, db)
    if user is None:
        raise credential_exception
    return user
