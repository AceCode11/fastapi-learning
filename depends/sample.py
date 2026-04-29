from fastapi import FastAPI , Depends , HTTPException , Query

app = FastAPI()

def professorvalid(token : str = Query(...)):
    if token!='tsdc':
        raise HTTPException(
            status_code = 404 , 
            detail = 'token not verified , not verified user '
        )
    return "professor valid"

@app.get('/timetable')
def gettimetable():
    return {"bscit" : "monday - java ,  tuesday -  python  ,  wednesday  - c"}


@app.post('/uploadmarks')
def uploadmarks(
    subj : str , 
    marks : int, 
    auth :  str = Depends(professorvalid)
):
    return {
        "message": f"Successfully uploaded {marks} marks for {subj}.",
        "security_log": auth
    }