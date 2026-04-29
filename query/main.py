from fastapi import FastAPI , Query
app = FastAPI()

@app.get('/filtermarks')
def filtermarks(
    score : int  = Query(... , ge = 0 , le = 100 , description = "The student exam score: ")

):
    if score  < 40:
        return  {"status" : "Fail" , "message" : " need to work harder "}
    return {"status": "pass" , "score" : score }
