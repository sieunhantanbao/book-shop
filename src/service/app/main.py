from fastapi import FastAPI
import uvicorn
from routers import auth, user, book
from routers.admin import book as admin_book, category as admin_category, rating as admin_rating, user as admin_user
app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(book.router)
app.include_router(admin_book.router)
app.include_router(admin_category.router)
app.include_router(admin_rating.router)
app.include_router(admin_user.router)

@app.get("/")
async def health_check():
    return "Service up and running"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)