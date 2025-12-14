from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import app.crud as crud
import app.schemas as schemas
from app.database import SessionLocal, init_db

init_db()

app = FastAPI(title="EDR - Electronic Doctor Record")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/Doctor/", response_model=schemas.DoctorOut, status_code=201)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db, doctor)

@app.get("/Doctor/{id}", response_model=schemas.DoctorOut)
def read_doctor(id: int, db: Session = Depends(get_db)):
    doc = crud.get_doctor(db, id)
    if not doc:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doc

@app.get("/Doctors/", response_model=list[schemas.DoctorOut])
def read_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_doctors(db, skip=skip, limit=limit)

@app.put("/Doctors/{id}", response_model=schemas.DoctorOut)
def update_doctor(id: int, updates: schemas.DoctorUpdate, db: Session = Depends(get_db)):
    updated = crud.update_doctor(db, id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return updated

@app.delete("/Doctors/{id}")
def delete_doctor(id: int, db: Session = Depends(get_db)):
    ok = crud.soft_delete_doctor(db, id)
    if not ok:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"detail": "Doctor soft-deleted"}
