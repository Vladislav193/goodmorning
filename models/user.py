from sqlalchemy import Column, Integer, String, Date, DateTime
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    birthday = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    zodiac_sign = Column(String, nullable=True)
