from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/about")
async def about():
    return {"data": "This is the about page"}

@app.get("/posts")
async def get_posts():
    return {"data": "This is my posts"}