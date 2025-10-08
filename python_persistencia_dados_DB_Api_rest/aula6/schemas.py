from pydantic import BaseModel


class Base_Studant(BaseModel):
    name: str
    age: int


class Create_Studant(Base_Studant):
    pass

class Studant_Response(Base_Studant):
    id: int

    class Config:
        from_atributes = True



class Base_Registration(BaseModel):
    estudant_id: int
    diciplinas_name: str


class Create_Registration(Base_Registration):
    pass


class Registration_Response(Base_Registration):
    id: int

    class Config:
        from_atributes = True

class StudantOut(Base_Studant):
    pass