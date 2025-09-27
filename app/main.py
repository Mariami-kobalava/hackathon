from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="UniBot Admin Chatbot")
app.include_router(router)
