from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, booking, equipments, payments, users, fields, news

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(booking.router)
app.include_router(equipments.router)
app.include_router(payments.router)
app.include_router(fields.router)
app.include_router(news.router)


@app.get("/")
async def read_root():
  return {"message": "This is API for Athletix website."}
