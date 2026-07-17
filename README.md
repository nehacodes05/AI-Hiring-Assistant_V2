#  AI Hiring Assistant v2

An AI-powered Applicant Tracking System (ATS) built with **Python, Flask, PostgreSQL, JWT Authentication, and Google Gemini AI**.

The platform enables recruiters to create jobs, candidates to apply with resumes, and automatically analyzes resumes using AI to generate a score and feedback, helping recruiters shortlist candidates faster.



# Features

## Authentication

- Recruiter & Candidate Signup
- Secure Login
- JWT Authentication
- Role-based Authorization



## Recruiter

- Create Jobs
- Update Jobs
- Delete Jobs
- View Own Jobs
- View Applications
- Rank Candidates by AI Score
- Download Candidate Resume



## Candidate

- View Available Jobs
- Apply to Jobs
- Upload Resume (PDF)



## AI Resume Analysis

- Extracts text from uploaded PDF resumes
- Sends resume content to Google Gemini
- Generates:
  - ATS Score
  - Resume Feedback
- Stores AI analysis in PostgreSQL



# Project Architecture


Client
   │
   ▼
Routes
   │
   ▼
Services
   │
   ▼
Utilities
   │
   ▼
PostgreSQL
        │
        ▼
Google Gemini AI




#  Project Structure


ai_hiring_assistant_version2/

├── routes/
│   ├── auth.py
│   ├── jobs.py
│   └── applications.py
│
├── services/
│   ├── auth_service.py
│   ├── job_service.py
│   ├── application_service.py
│   └── ai_service.py
│
├── utils/
│   ├── auth_decorator.py
│   ├── jwt_helper.py
│   ├── pdf_helper.py
│   └── prompts.py
│
├── uploads/
├── app.py
├── config.py
├── database.py
├── requirements.txt
└── README.md



#  Tech Stack

### Backend

- Python
- Flask

### Database

- PostgreSQL

### Authentication

- JWT

### AI

- Google Gemini API

### Libraries

- psycopg2
- PyPDF
- python-dotenv


# 🔄 Complete Workflow


Recruiter Login
        │
        ▼
Create Job
        │
        ▼
Candidate Login
        │
        ▼
Apply to Job
        │
        ▼
Upload Resume
        │
        ▼
Save PDF
        │
        ▼
Extract Resume Text
        │
        ▼
Gemini AI Analysis
        │
        ▼
Generate Score & Feedback
        │
        ▼
Save Analysis
        │
        ▼
Recruiter Dashboard
        │
        ▼
Download Resume


#  Authentication

JWT Authentication is used to secure all protected routes.

Roles:

- Recruiter
- Candidate

Each endpoint validates:

- Authentication
- Authorization

before processing the request.



#  AI Resume Analysis

When a candidate uploads a resume:

1. Resume is saved locally.
2. Resume path is stored in PostgreSQL.
3. PDF text is extracted.
4. Text is sent to Google Gemini.
5. Gemini returns:

json
{
  "score": 92,
  "feedback": "Strong Python and Flask skills."
}


6. Score and feedback are stored in PostgreSQL.


#  REST APIs

## Authentication

- POST /signup
- POST /login



## Jobs

- POST /jobs
- GET /jobs
- GET /jobs/<id>
- PUT /jobs/<id>
- DELETE /jobs/<id>



## Applications

- POST /jobs/<id>/apply
- POST /applications/<id>/resume
- GET /jobs/<id>/applications
- GET /applications/<id>/resume



# Design Decisions

### Layered Architecture

Business logic is separated from routes using a Service Layer.


Route
    ↓
Service
    ↓
Database / AI



### AI Fault Tolerance

Resume upload and AI analysis are intentionally separated.

1. Save resume immediately.
2. Update AI score only after Gemini succeeds.

This prevents data loss if the AI service is temporarily unavailable.

# What I Learned

Through this project I gained practical experience with:

- REST API Design

- Python Backend Development

- Flask

- PostgreSQL

- JWT Authentication

- Role-Based Authorization

- SQL JOINs

- File Uploads

- PDF Processing

- Google Gemini API Integration

- Prompt Engineering

- JSON Parsing

- Backend Project Architecture

- Git & GitHub

- Environment Variables

- Debugging Production-Style Issues


# Future Improvements

- Email Notifications
- Resume Re-analysis
- Dashboard Analytics
- Pagination
- Search & Filters
- Cloud Storage (AWS S3)
- Docker Deployment

# Author

Neha Kumari

B.Tech Computer Science Engineering

Python Backend Developer