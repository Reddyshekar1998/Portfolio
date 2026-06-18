from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.portfolio import Contact
from app.schemas.portfolio import ContactForm
import resend
import os

resend.api_key = os.getenv("RESEND_API_KEY")

router = APIRouter()

@router.post("/contact")
async def create_contact(
    payload: ContactForm,
    db: AsyncSession = Depends(get_db),
):
    contact = Contact(
        name=payload.name,
        email=payload.email,
        subject=payload.subject,
        message=payload.message,
    )

    db.add(contact)

    await db.commit()
    await db.refresh(contact)

    # Send confirmation email
    try:
        # email = resend.Emails.send({
        #     "from": "onboarding@resend.dev",
        #     "to": contact.email,
        #     "subject": f"Thank you for your message, {contact.name}!",
        #     "html": f"""
        #         <p>Hello {contact.name},</p>
        #         <p>Thank you for contacting me. I will get back to you soon.</p>
        #         <p>Best regards,<br/>Kilari Reddy Sekhar</p>
        #     """
        # })
        r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "kilarireddysekhar@gmail.com",
        "subject": f"New Contact Message from portfolio: {contact.subject}",
        "html": f"""
            <p>Hello Kilari,</p>
            <p>You have a new contact message from {contact.name}.</p>
            <p><strong>Subject:</strong> {contact.subject}</p>
            <p><strong>Message:</strong> {contact.message}</p>
            <p><strong>Email:</strong> {contact.email}</p>
        """
        })
        # print(f"Email sent successfully: {email}")
        print(f"Notification email sent successfully: {r}")
    except Exception as e:
        print(f"Error sending email: {e}")

    


    return {
        "success": True,
        "id": contact.id
    }


@router.get("/contacts")
async def get_contacts(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Contact))

    contacts = result.scalars().all()
    return contacts