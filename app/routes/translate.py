from fastapi import APIRouter
from app.models.request_models import TranslateRequest
from app.services.translator_service import translate_text

router = APIRouter()

@router.post("/translate")
def translate(req: TranslateRequest):
    return {
        "translated_text":
        translate_text(
            req.text,
            req.target_language
        )
    }