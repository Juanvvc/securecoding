from fastapi import FastAPI

app = FastAPI()




@app.get("/create")
async def create( ):
    return {"message": "Hello World"}
    