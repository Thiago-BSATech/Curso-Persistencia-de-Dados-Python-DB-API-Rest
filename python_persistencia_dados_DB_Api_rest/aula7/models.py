# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Studants(Base):
    __tablename__ = 'estudantes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100))

    perfil = relationship(
        "Perfil",
        back_populates="studant",
        uselist=False,
        cascade="all, delete-orphan"
    )


class Perfil(Base):
    __tablename__ = 'perfis'

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    address = Column(String(200))
    studant_id = Column(Integer, ForeignKey("estudantes.id"), unique=True)

    studant = relationship("Studants", back_populates="perfil")
