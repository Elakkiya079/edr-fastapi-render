from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doc = models.Doctor(
        name=doctor.name,
        age=doctor.age,
        gender=doctor.gender,
        speciality=doctor.speciality,
    )
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id, models.Doctor.is_active==True).first()

def list_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Doctor).filter(models.Doctor.is_active==True).offset(skip).limit(limit).all()

def update_doctor(db: Session, doctor_id: int, updates: schemas.DoctorUpdate):
    doc = db.query(models.Doctor).filter(models.Doctor.id == doctor_id, models.Doctor.is_active==True).first()
    if not doc:
        return None
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(doc, field, value)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

def soft_delete_doctor(db: Session, doctor_id: int):
    doc = db.query(models.Doctor).filter(models.Doctor.id == doctor_id, models.Doctor.is_active==True).first()
    if not doc:
        return False
    doc.is_active = False
    db.add(doc)
    db.commit()
    return True
