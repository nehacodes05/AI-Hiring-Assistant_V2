## Authentication Module

### Features

- User Registration API
- User Login API
- Password Hashing using Werkzeug
- JWT Authentication
- JWT Protected Routes
- Authentication Decorator
- PostgreSQL Integration
- REST API Architecture
- JSON Request & Response

### Authentication Flow

Client
↓
POST /login
↓
Flask Route
↓
Authentication Service
↓
PostgreSQL
↓
Password verification
↓
JWT Generation
↓
JSON Response


### Protected Route Flow

Client
    ↓
GET /profile
    ↓
Authorization Header (Bearer JWT)
    ↓
Authentication Decorator
    ↓
JWT Verification
    ↓
Protected Route
    ↓
JSON Response

## Implemented APIs

### Authentication

POST /signup

Registers a new user.

POST /login

Authenticates the user and returns a JWT.

GET /profile

Protected route used to verify JWT authentication.

## Technologies Used

- Python
- Flask
- PostgreSQL
- PyJWT
- Werkzeug Security



## Job Management Module

### Features

- Recruiter can create jobs
- JWT Protected Endpoint
- PostgreSQL Integration
- Parameterized SQL Queries
- Transaction Handling
- Error Handling using try-except-finally

### API

POST /jobs

Authorization: Bearer Token

Request

{
  "title": "Python Backend Intern",
  "description": "Flask + PostgreSQL",
  "salary": 30000
}

Response

{
  "success": true,
  "message": "Job created successfully"
}



