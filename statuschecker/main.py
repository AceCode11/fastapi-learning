from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def home():
    return {"status" : "online"  , "server" : "fastapi_server"}

@app.get('/helth')
def health():
    return { 
        "database" : "connected" , 
        "uptime" : "99.9%" , 
        "memory_usage" : "low"
    }