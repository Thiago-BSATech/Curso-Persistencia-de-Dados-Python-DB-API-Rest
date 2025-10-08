from sqlalchemy import \
    Column, Integer, String, ForeignKey
from database import Base



class Studants(Base):

    __tablename__ = 'estudantes'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    age = Column(Integer)


class Registration(Base):

    __tablename__ = 'matriculas'

    id = Column(Integer, primary_key=True, index=True)

    studant_id = ForeignKey('estudantes.id')

    diciplina = Column(String(100), nullable=False)
