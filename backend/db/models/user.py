from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.orm import relationship

from db.base_class import Base
from .blog import Blog

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String,nullable=False)
    is_active = Column(Boolean,default=False)
    blogs = relationship("Blog", back_populates="author")
