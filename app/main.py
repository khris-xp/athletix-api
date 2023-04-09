from fastapi import FastAPI
from .routers import auth, booking, equipments, payments, users, fields, news

app = FastAPI()

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
