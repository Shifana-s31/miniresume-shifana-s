from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import List

# FastAPI instance must be named 'app'
app = FastAPI()

# In-memory storage (No database)
resumes = []

# Resume model with validation
class Resume(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    skills: List[str]
    experience: int = Field(..., ge=0)

# Health check endpoint (MANDATORY)
@app.get("/health", status_code=200)
def health_check():
    return {"status": "ok"}

# Create resume endpoint
@app.post("/resumes", status_code=201)
def create_resume(resume: Resume):
    resumes.append(resume)
    return {
        "message": "Resume added successfully",
        "data": resume
    }

# Get all resumes
@app.get("/resumes", status_code=200)
def get_resumes():
    return resumes
