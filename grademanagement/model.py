from sqlalchemy import Column  , Integer , String , Float , Boolean
from database import base 


class Studentmodel(base):
    __tablename__ = "students"

    id  = Column(Integer , primary_key=True , index=True)
    rollno = Column(Integer , unique=True , index = True)
    name = Column(String)
    physics = Column(Integer)
    maths = Column(Integer)
    itskills = Column(Integer)
    total = Column(Integer)
    percentage = Column(Float)
    result = Column(String)