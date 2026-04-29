# THIS IS THE CORRECT WAY
from fastapi import FastAPI, Depends
app = FastAPI()

def givegreet():
    return "HELLO KRISHNA"

@app.get('/test')
def testdepends(greeting : str = Depends(givegreet)):
    return {'result' : 'greeting'}