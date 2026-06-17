# # # main.py
# # from fastapi import FastAPI, HTTPException, status
# # from fastapi.middleware.cors import CORSMiddleware
# # from pydantic import BaseModel, EmailStr

# # app = FastAPI()

# # # Enable CORS for Next.js development server
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["http://localhost:3000"],  # Next.js local address
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # Define the expected request payload format
# # class ContactForm(BaseModel):
# #     name: str
# #     email: str  # Use EmailStr if you install 'pydantic[email]'
# #     subject: Optional[str] = None
# #     message: str

# # @app.post("/api/contact", status_code=status.HTTP_200_OK)
# # async def submit_contact_form(payload: ContactForm):
# #     try:
# #         # Process data here (e.g., save to DB, send email via a service)
# #         print(f"Received message from {payload.name} ({payload.email}): {payload.message}")
# #         print(f"Subject: {payload.subject}")
        
# #         return {"success": True, "message": "Message received successfully!"}
# #     except Exception as e:
# #         raise HTTPException(
# #             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
# #             detail="Failed to process request"
# #         )


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, EmailStr
# from typing import Optional
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

# # conf = ConnectionConfig(
# #     MAIL_USERNAME="gmr9502@gmail.com",
# #     MAIL_PASSWORD="gmail_app_password",
# #     MAIL_FROM="yourgmail@gmail.com",
# #     MAIL_PORT=587,
# #     MAIL_SERVER="smtp.gmail.com",
# #     MAIL_STARTTLS=True,
# #     MAIL_SSL_TLS=False,
# #     USE_CREDENTIALS=True,
# # )

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Next.js URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class ContactForm(BaseModel):
#     name: str
#     email: EmailStr
#     subject: Optional[str] = None
#     message: str

# @app.post("/contact")
# async def submit_contact(form: ContactForm):
#     print("New Contact Request:")
#     print(form.dict())
    
#     # Save to DB / Send Email here
#     # message = MessageSchema(
#     #     subject=f"Portfolio Contact: {form.subject}",
#     #     recipients=["yourgmail@gmail.com"],
#     #     body=f"""
#     #     Name: {form.name}
#     #     Email: {form.email}

#     #     Message:
#     #     {form.message}
#     #     """,
#     #     subtype="plain",
#     # )

#     # fm = FastMail(conf)
#     # await fm.send_message(message)

    
    


#     return {
#         "success": True,
#         "message": "Message sent successfully"
#     }



from fastapi import FastAPI
from app.routes.contact import router
from contextlib import asynccontextmanager
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "www.kilari.online",
        "https://www.kilari.online",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    router,
    prefix="/api",
    tags=["Contact"]
)



@app.get("/")
async def root():
    return {"message": "Hello World"}

print("MAIN.PY LOADED")
