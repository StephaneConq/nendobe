from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

load_dotenv()

from routers import photo_router, price_router, nendoroid_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://nendobe-pmvbal4k7a-od.a.run.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(photo_router)
app.include_router(price_router)
app.include_router(nendoroid_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)