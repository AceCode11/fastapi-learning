from fastapi import FastAPI
from pydantic import BaseModel
from typing import List , Optional

class Task(BaseModel):
    id : int 
    title : str
    description : str
    completed : bool = False

todotask = [
    {
        "id" : 1 , 
        "title" : "today goal" , 
        "description" : "to do the revision" , 
        "completed" : True

    }
]
app = FastAPI()
@app.get('/tasks')
def getalltask():
    return todotask


@app.get('/tasks/{taskid}')
def taskbyid(taskid : int):
    for i in todotask:
        if i["id"] == taskid:
            return i 
        return {
            "message" : "the task is not listed"
        }
    

@app.post('/tasks')
def addtask(newtask : Task):
    todotask.append(newtask.dict())
    return{
        "message": " the task has been added" , 
        "total task":len(todotask)
    }

@app.put('/tasks/{taskid}')
def updatetask(taskid : int ,  Updatedtask : Task):
    for i ,task in enumerate(todotask):
        if task['id'] == taskid:
            todotask[i] = Updatedtask.dict()
            return{"message" : "you have successgully inserted the task"}
    return {"error : taks not found"}
        
@app.delete('tasks/{taskid}')
def deletetask(taskid : int ):
    for i , task in enumerate(todotask):
        if task['id'] ==taskid:

            todotask.pop(i)
            return{"message" : "you have deleted the task succesfuuly"}
    return{"error" : "task not found"}
