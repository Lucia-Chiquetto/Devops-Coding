from fastapi import FastAPI

app = FastAPI()

@app.get("/helloword")
async def root():
    return {"message": "Hello World"}

@app.get("/endpoint")
async def funcaoteste():
    return {"teste": "deu certo"}

