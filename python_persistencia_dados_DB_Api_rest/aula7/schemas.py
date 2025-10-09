from typing import List, Optional
from pydantic import BaseModel
from models import Perfil



class Perfil(BaseModel):

    id: int
    age: int
    address: str

    
    model_config = {
        "from_attributes": True
    }



class Studant(BaseModel):

    id: int
    name: str
    perfil: Optional[Perfil] = None


    model_config = {
        "from_attributes": True
    }

    

class CreatePerfil(BaseModel):

    age: int
    address: str



class CreateStudant(BaseModel):

    name: str
    email: str
    perfil: CreatePerfil