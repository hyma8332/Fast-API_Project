from fastapi import APIRouter
from app.models.request_models import SummaryRequest
from app.services.summarizer_service import summarize_text

router = APIRouter()

@router.post("/summarize")
def summarize(req: SummaryRequest):
    return {
        "summary": summarize_text(req.text)
    }