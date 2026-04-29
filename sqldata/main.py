from fastapi import FastAPI, Depends , HTTPException
import model
from database import engine, sessionlocal
from sqlalchemy.orm import Session

app = FastAPI()

# 1. Matches your models.py 'base'
model.base.metadata.create_all(bind=engine)

def dbget():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def testdb(db: Session = Depends(dbget)):
    return {"message": "the pipe is working"}

@app.post("/students/")
#
def create_student(roll_no: int, name: str, db: Session = Depends(dbget)):
    existingstudent = db.query(model.student).filter(model.student.rollno==roll_no).first()
    if existingstudent:
        raise HTTPException(status_code=404 , detail = "rollno already exit ")
    
    new_student = model.student(rollno=roll_no, name=name)
    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    return {"message": "Student saved!", "data": new_student}


@app.get('/students')
def getstudents(db:Session = Depends(dbget)):
    students = db.query(model.student).all()
    return students 




'''handlinig optional'''

'''
    from typing import Optional

@app.put("/students/partial/{student_id}")
def update_student_partial(
    student_id: int, 
    name: Optional[str] = None, 
    course: Optional[str] = None, 
    db: Session = Depends(dbget)
):
    student = db.query(model.student).filter(model.student.id == student_id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Only update if the user actually sent a value
    if name is not None:
        student.name = name
    if course is not None:
        student.course = course
    
    db.commit()
    db.refresh(student)
    return student
    '''