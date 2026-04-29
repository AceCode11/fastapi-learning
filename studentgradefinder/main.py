from fastapi import FastAPI

app = FastAPI()

students = { 
    1:{"name":"krishna" , "role" : "datascience"} , 
    2:{"name":"raj" , "role":"datanalyst"}
}

@app.get('/students/{studentid}')

def student(studentid : int):
    if studentid in students:
        return students[studentid]
    
    return {"error" : "no data found"}

