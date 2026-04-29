from pydantic import BaseModel
from fastapi import FastAPI

class Project(BaseModel):
    name : str
    description : str
    iscompleted : bool  = False
    rating :  int

app  = FastAPI()

@app.post("/project")
def project(project: Project):
    return { 
        'message' : 'prj is succesful' , 
        'name' : project.name,
        'summary' : f"{project.name} is rated {project.rating}"
    }