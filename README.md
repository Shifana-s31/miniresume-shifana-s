# Mini Resume Collector API

A simple REST API built using FastAPI to collect and manage candidate resume details.

## Python Version Used
Python 3.14.0

## Installation Steps

1. Clone the repository:

   git clone https://github.com/your-username/miniresume-shifana-s.git

2. Navigate into the project folder:

   cd miniresume-shifana-s

3. Create virtual environment:

   python -m venv venv

4. Activate virtual environment:

   Windows:
   venv\Scripts\Activate

5. Install dependencies:

   pip install -r requirements.txt

## Running the Application

Run the following command:

   python -m uvicorn main:app --reload

The application will run at:

   http://127.0.0.1:8000

Swagger documentation available at:

   http://127.0.0.1:8000/docs

## API Endpoints

### 1. Health Check

GET /health

Response:
{
  "status": "ok"
}

### 2. Create Resume

POST /resumes

Example Request:

{
  "name": "Shifana",
  "email": "shifana@gmail.com",
  "phone": "9876543210",
  "skills": ["Python", "FastAPI"],
  "experience": 2
}

Response:
Status Code: 201
{
  "message": "Resume added successfully",
  "data": { ... }
}

### 3. Get All Resumes

GET /resumes

Returns list of stored resumes.
