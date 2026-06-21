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
from app.core.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
# from fastapi_utilities import repeat_every
# import httpx

# @repeat_every(seconds=10)  # 600 seconds = 10 minutes
# async def keep_alive():
#     async with httpx.AsyncClient() as client:
#         try:
#             # Replace with your app's actual live URL
#             response = await client.get("https://api.kilari.online")
#             print(f"Ping successful! Status: {response.status_code}")
#         except Exception as e:
#             print("Ping failed:", e)


@asynccontextmanager
async def lifespan(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",        # Local Next.js dev server
        "https://www.kilari.online",    # Production with www
        "https://kilari.online",        # Production apex domain (highly recommended to add)
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

@app.get("/health")
def health_check():
    return {"status": "alive"}


@app.get("/")
async def root():
    print("Root endpoint accessed")
    return {"message": "Hello Brossss"}

# print("MAIN.PY LOADED")
