from fastapi import FastAPI , HTTPException

app = FastAPI()

students = {1 : 'Krishna'}

@app.get('/student/{id}')
def getstudent(id : int):
    if id not in students: 
        raise HTTPException(status_code=404 , detail = 'student not found in database')
    
    return {"name"  : students[id]}