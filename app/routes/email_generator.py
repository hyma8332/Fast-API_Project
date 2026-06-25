from fastapi import APIRouter
from app.models.request_models import EmailRequest
from app.services.email_service import generate_email

router = APIRouter()

@router.post("/generate-email")
def email(req: EmailRequest):
    return {
        "email":
        generate_email(
            req.recipient_name,
            req.purpose
        )
    }