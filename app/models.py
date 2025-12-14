from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    speciality = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
