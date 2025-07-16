from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import JSONResponse

app = FastAPI(title="Portfolio API", description="Backend for Personal Portfolio", version="1.1.0")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    print(f"Request: {request.method} {request.url} Status: {response.status_code}")
    return response

class Project(BaseModel):
    name: str
    description: str
    tech_stack: List[str]

class About(BaseModel):
    name: str
    title: str
    description: str
    email: str
    location: str

about_data = About(
    name="Kilari Reddy Sekhar",
    title="Backend Developer | AI/ML Enthusiast",
    description="I design and build scalable APIs and machine learning systems with Python, FastAPI, and Django.",
    email="reddyshekar1998@gmail.com",
    location="India"
)

skills = ["Python", "FastAPI", "Django", "Flask", "REST API", "Machine Learning", "PostgreSQL", "Docker", "Git"]

projects: List[Project] = [
    Project(
        name="Voicebot Application",
        description="A voicebot system with STT, LLM, and TTS pipeline using FastAPI backend.",
        tech_stack=["FastAPI", "Python", "NVIDIA T4", "LLM"]
    ),
    Project(
        name="AI Resume Parser",
        description="A FastAPI microservice to extract structured data from resumes using NLP.",
        tech_stack=["FastAPI", "spaCy", "Python"]
    )
]

@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to Kilari Reddy Sekhar's Portfolio API"}

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}

@app.get("/about", response_model=About, tags=["About"])
def get_about():
    return about_data

@app.get("/skills", response_model=List[str], tags=["Skills"])
def get_skills():
    return skills

@app.get("/projects", response_model=List[Project], tags=["Projects"])
def get_projects(tech: Optional[str] = Query(None, description="Filter by tech stack")):
    if tech:
        filtered = [p for p in projects if tech in p.tech_stack]
        return filtered
    return projects

@app.post("/projects", response_model=Project, tags=["Projects"])
def add_project(project: Project):
    projects.append(project)
    return project
