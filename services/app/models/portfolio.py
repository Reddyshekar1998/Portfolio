from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from ..core.database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))
    email = Column(String(255))
    subject = Column(String(255))
    message = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )