from sqlalchemy import Column , Integer , String , Boolean
from database import base

class student(base):
    __tablename__ = "students"

    id = Column(Integer , primary_key=True , index=True)
    rollno = Column(Integer , unique=True , index=True)
    name = Column(String)
    course = Column(String , default="bscit")
    isactive = Column(Boolean , default=True)