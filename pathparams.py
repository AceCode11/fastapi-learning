from fastapi import FastAPI
app = FastAPI()

@app.get('/items/{itemid}')
def items(itemid : int):
    return{'itemid': 1 , 'message' : f"you are looking at item number:{itemid}"}