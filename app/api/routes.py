from fastapi import APIRouter
from pydantic import BaseModel
from app.core.qa_service import get_answer_with_video

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask_question(request: QuestionRequest):
    response = get_answer_with_video(request.question)
    return response

