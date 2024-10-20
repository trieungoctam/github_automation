from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from typing import List
from src.utils.config import settings
from src.services.email_service import EmailService

router = APIRouter()

class EmailMessage(BaseModel):
    to: List[EmailStr]
    subject: str
    body: str

def get_email_service():
    return EmailService(settings.EMAIL_HOST, settings.EMAIL_PORT, settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)

@router.post("/send")
async def send_email(email_data: EmailMessage, email_service: EmailService = Depends(get_email_service)):
    try:
        email_service.send_email(email_data.to, email_data.subject, email_data.body)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/send-bulk")
async def send_bulk_email(email_data: List[EmailMessage], email_service: EmailService = Depends(get_email_service)):
    try:
        for email in email_data:
            email_service.send_email(email.to, email.subject, email.body)
        return {"message": f"{len(email_data)} emails sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
