from fastapi import FastAPI
import uvicorn
from routers import auth, user, book

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(book.router)
# app.include_router(task.router)

@app.get("/")
async def health_check():
    return "Service up and running"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)