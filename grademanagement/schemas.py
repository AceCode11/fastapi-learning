from pydantic import BaseModel , Field
from typing import Optional

class Gradecreate(BaseModel):
    rollno : int
    name : str
    physics : int  = Field(ge = 0 , le = 100)
    maths : int  = Field(ge = 0 , le = 100)
    itskills  : int  = Field(ge = 0 , le = 100)

class Graderesponse(Gradecreate):
    id : int
    total : int
    percentage : float
    result : str

    class config:
        from_attributes = True