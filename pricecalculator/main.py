from fastapi import FastAPI
app = FastAPI()

@app.get('/home')
def calculator(price : float , quantity : int , discount : float = 0.0):
    finalprice = (price * quantity) - discount

    return{
        'unitprice' : price , 
        'quantity' : quantity , 
        'discount' : discount , 
        'price' : finalprice
    }