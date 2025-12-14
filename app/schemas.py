from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional

class DoctorCreate(BaseModel):
    name: str = Field(..., example="Dr. Priya")
    age: int = Field(..., example=38)
    gender: str = Field(..., example="Female")
    speciality: str = Field(..., example="Cardiology")

class DoctorUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    speciality: Optional[str]

class DoctorOut(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    speciality: str
    is_active: bool

    class Config:
        orm_mode = True


# Ensure any forward references (string annotations) are resolved
DoctorCreate.update_forward_refs()
DoctorUpdate.update_forward_refs()
DoctorOut.update_forward_refs()
