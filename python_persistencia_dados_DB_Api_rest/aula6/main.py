from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine


# Cria tabelas (caso não existam)
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close

# Studants Controller


@app.post('/estudantes', response_model = schemas.Studant_Response)
def create_studant(studant: schemas.Create_Studant, db: Session = Depends(get_db)):

    db_studant = models.Studants(**studant.model_dump())

    db.add(db_studant)
    db.commit()

    db.refresh(db_studant)

    return db_studant


@app.get("/estudantes", response_model = List[schemas.Studant_Response])
def get_studants(db: Session = Depends(get_db)):

    return db.query(models.Studants).all()


# Desafio aula 6 -->
@app.get("/estudantes/{studant_id}", response_model = schemas.StudantOut)
def get_a_studant(studant_id, db: Session = Depends(get_db)):
    
    # Ajuda IA -->
    studant = db.query(models.Studants).filter(models.Studants.id == studant_id).first()
    # <-- Ajuda IA

    if not studant:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    
    return studant



