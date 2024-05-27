from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from fastapi.staticfiles import StaticFiles
import uvicorn
from app.routers import auth, user, book
from app.routers.admin import book as admin_book, category as admin_category, rating as admin_rating, user as admin_user

load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get('ALLOWED_ORIGINS')],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Allow access static folder
app.mount(f"/{os.environ.get('UPLOAD_FOLDER')}",
          StaticFiles(directory=f"{os.environ.get('UPLOAD_FOLDER')}"),
          name="static")

# Add routers
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