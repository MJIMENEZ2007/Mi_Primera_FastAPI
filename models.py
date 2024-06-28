from sqlalchemy import String , Integer , Column
from database import Base 

class Ingreso(Base):
    __tablename__ = "registro_de_ingreso"
    idregistro = Column(Integer, primary_key=True , index= True)
    documentoingreso = Column(String(11))
    nombrepersona = Column(String(100))
