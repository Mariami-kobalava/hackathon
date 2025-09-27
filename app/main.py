from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.routes import router

app = FastAPI(title="UniBot Admin Chatbot")
app.include_router(router)

# Serve the HTML file at root
@app.get("/")
async def serve_index():
    return FileResponse('test.html')
