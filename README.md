## Authentication Module

### Features

- User Registration API
- User Login API
- Password Hashing using Werkzeug
- JWT Authentication
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
JWT Generation
↓
JSON Response