from sqlalchemy import Column, String, Integer
from database import Base


class Good_Night(Base):
    __tablename__ = "good_night"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)