from pydantic import BaseModel

class SummaryRequest(BaseModel):
    text: str

class TranslateRequest(BaseModel):
    text: str
    target_language: str

class EmailRequest(BaseModel):
    recipient_name: str
    purpose: str