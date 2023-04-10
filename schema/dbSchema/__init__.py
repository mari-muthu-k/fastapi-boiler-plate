from sqlalchemy import Column,Integer, String,DateTime
from datetime import datetime

from db import Base

class Example(Base):
    __tablename__ = "example"

    id = Column(Integer, primary_key=True, index=True)
    name  = Column(String(255))
    email = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())