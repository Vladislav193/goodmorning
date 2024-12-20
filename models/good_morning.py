from sqlalchemy import Column, Integer, String
from database import Base


class Good_Morning(Base):
    __tablename__ = "good_morning"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)