from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import SQLColumnExpression
from sqlalchemy.orm import Session, joinedload
import models, schemas
from database import engine, SessionLocal
from typing import List


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():

    db= SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/estudantes", response_model= schemas.Studant)

def create_studant(

    studant: schemas.CreateStudant,
    db: Session = Depends(get_db)

):
    
    db_studant = models.Studants(
        name = studant.name,
        perfil = models.Perfil(**studant.perfil.dict()),
        email = studant.email

    )

    db.add(db_studant)

    db.commit()
    db.refresh(db_studant)

    return db_studant


@app.get("/estudantes", response_model=List[schemas.Studant])

def list_studants(db: Session = Depends(get_db)):

    return db.query(models.Studants).options(joinedload(models.Studants.perfil)).all()