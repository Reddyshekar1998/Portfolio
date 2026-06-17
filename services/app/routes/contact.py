from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Contact
from app.schemas import ContactForm

router = APIRouter()

@router.get("/data")
async def get_contacts():
    return {"message": "success"}

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
    print(contact)

    db.add(contact)

    await db.commit()
    await db.refresh(contact)

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
    print(contacts)
    return contacts