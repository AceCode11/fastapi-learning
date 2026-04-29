from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
import model , schemas
from database import engine , sessionlocal

model.base.metadata.create_all(bind = engine)
app = FastAPI(title="tsdc grade ")

def getdb():
    db = sessionlocal()

    try:
        yield db

    finally:
        db.close()

@app.post('/students' , response_model=schemas.Graderesponse)
def student(student:schemas.Gradecreate , db:Session = Depends(getdb)):
        db_student = db.query(model.Studentmodel).filter(model.Studentmodel.rollno == student.rollno).first()
        if db_student:
             raise HTTPException(status_code=400 , detail = "rollno already registered")
        

        #logic
        totalmarks = student.physics + student.maths + student.itskills
        perc = round((totalmarks / 300)*100 , 2)
        status = "pass" if(student.physics >= 35 and student.maths >=35 and student.itskills >=35) else "fail"
        

        newstudent = model.Studentmodel(
        **student.model_dump() ,
        total = totalmarks , 
        percentage = perc , 
        result = status
        )

        db.add(newstudent)
        db.commit()
        db.refresh(newstudent)
        return newstudent


@app.get('/students' , response_model=list[schemas.Graderesponse])
def getallstudents(db:Session = Depends(getdb)):
     return db.query(model.Studentmodel).all()

@app.get('/students/toppers')
def getalltoppers(db:Session = Depends(getdb)):
     return  db.query(model.Studentmodel).filter(model.Studentmodel.percentage>=75.0).all()

@app.delete('/students/{rollno}')
def deletestudents(rollno : int , db : Session = Depends(getdb)):
     student = db.query(model.Studentmodel).filter(model.Studentmodel.rollno ==rollno).first()
     if not student:
          raise HTTPException(status_code=404  , detail="no student rollno found")
     
     db.delete(student)
     db.commit()
     return{"detail" : f"student {rollno} deleted"}







        
            
