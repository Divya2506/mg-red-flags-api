# MyGets Red Flags FastAPI Backend

A well-structured FastAPI backend for the MyGets Red Flags detection system with proper folder organization and clear scope separation.

## Project Structure

```
mygets_backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── api/                    # API layer
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py          # Main API router
│   │       └── endpoints/      # API endpoints
│   │           ├── __init__.py
│   │           ├── auth.py     # Authentication endpoints
│   │           ├── users.py    # User management endpoints
│   │           ├── red_flags.py # Red flags endpoints
│   │           ├── ocds.py     # OCDS data endpoints
│   │           └── analytics.py # Analytics endpoints
│   ├── core/                   # Core application components
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration settings
│   │   ├── database.py        # Database configuration
│   │   └── security.py        # Security and authentication
│   ├── crud/                  # Database operations
│   │   ├── __init__.py
│   │   ├── base.py           # Base CRUD operations
│   │   ├── user.py           # User CRUD operations
│   │   ├── red_flag.py       # Red flag CRUD operations
│   │   └── ocds.py           # OCDS CRUD operations
│   ├── models/               # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py          # User model
│   │   ├── red_flag.py      # Red flag models
│   │   └── ocds.py          # OCDS models
│   ├── schemas/             # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py         # User schemas
│   │   ├── red_flag.py     # Red flag schemas
│   │   └── ocds.py         # OCDS schemas
│   └── services/           # Business logic services
│       ├── __init__.py
│       ├── red_flag_engine.py # Red flag detection engine
│       └── analytics_service.py # Analytics service
├── requirements.txt         # Python dependencies
├── .env                    # Environment variables (create this)
└── README.md              # This file
```

## Features

- **Authentication & Authorization**: JWT-based authentication with role-based access control
- **User Management**: Complete user CRUD operations with password hashing
- **Red Flags Detection**: Rule-based red flag detection engine with configurable rules
- **OCDS Integration**: Open Contracting Data Standard (OCDS) data management
- **Analytics**: Comprehensive analytics and reporting capabilities
- **API Documentation**: Automatic OpenAPI/Swagger documentation
- **Database**: SQLAlchemy ORM with SQLite (configurable for other databases)

## Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the project root:

```env
# Application settings
PROJECT_NAME=MyGets Red Flags API
VERSION=1.0.0
DEBUG=true

# Server settings
HOST=0.0.0.0
PORT=8000

# Security
SECRET_KEY=your-super-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database
DATABASE_URL=sqlite:///./mygets.db

# CORS
ALLOWED_HOSTS=["*"]

# External APIs
OCDS_API_URL=https://api.example.com/ocds
```

### 3. Run the Application

```bash
# Run with uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or run the main.py directly
python -m app.main
```

### 4. Access the API

- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/api/v1/health

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login and get access token

### Users
- `GET /api/v1/users/me` - Get current user
- `GET /api/v1/users/` - List users
- `GET /api/v1/users/{user_id}` - Get user by ID
- `PUT /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user

### Red Flags
- `GET /api/v1/red-flags/` - List red flags
- `POST /api/v1/red-flags/` - Create red flag
- `GET /api/v1/red-flags/{red_flag_id}` - Get red flag by ID
- `PUT /api/v1/red-flags/{red_flag_id}` - Update red flag
- `DELETE /api/v1/red-flags/{red_flag_id}` - Delete red flag
- `GET /api/v1/red-flags/rules/` - List red flag rules
- `POST /api/v1/red-flags/detect/` - Detect red flags in data

### OCDS Data
- `GET /api/v1/ocds/contracts/` - List OCDS contracts
- `POST /api/v1/ocds/contracts/` - Create OCDS contract
- `GET /api/v1/ocds/contracts/{contract_id}` - Get contract by ID
- `GET /api/v1/ocds/parties/` - List OCDS parties
- `POST /api/v1/ocds/parties/` - Create OCDS party
- `GET /api/v1/ocds/parties/{party_id}` - Get party by ID
- `GET /api/v1/ocds/tenders/` - List OCDS tenders
- `POST /api/v1/ocds/tenders/` - Create OCDS tender
- `GET /api/v1/ocds/tenders/{tender_id}` - Get tender by ID

### Analytics
- `GET /api/v1/analytics/red-flags/summary` - Red flags summary
- `GET /api/v1/analytics/red-flags/by-severity` - Red flags by severity
- `GET /api/v1/analytics/red-flags/by-category` - Red flags by category
- `GET /api/v1/analytics/ocds/contracts/summary` - OCDS contracts summary
- `GET /api/v1/analytics/ocds/contracts/by-value` - Contracts by value range
- `GET /api/v1/analytics/ocds/parties/summary` - OCDS parties summary
- `GET /api/v1/analytics/dashboard/overview` - Dashboard overview

## Authentication

The API uses JWT tokens for authentication. To access protected endpoints:

1. Register a user: `POST /api/v1/auth/register`
2. Login: `POST /api/v1/auth/login`
3. Use the returned access token in the Authorization header:
   ```
   Authorization: Bearer <your-access-token>
   ```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_auth.py
```

### Code Structure Principles

1. **Separation of Concerns**: Each layer has a specific responsibility
   - **Models**: Database structure and relationships
   - **Schemas**: Data validation and serialization
   - **CRUD**: Database operations
   - **Services**: Business logic
   - **API**: Request/response handling

2. **Dependency Injection**: FastAPI's dependency injection system is used throughout

3. **Type Hints**: All functions include proper type annotations

4. **Error Handling**: Comprehensive error handling with proper HTTP status codes

5. **Documentation**: All endpoints and functions are documented

## Deployment

### Production Considerations

1. **Environment Variables**: Use proper environment variables for production
2. **Database**: Use a production database (PostgreSQL, MySQL)
3. **Security**: Use strong secret keys and HTTPS
4. **CORS**: Configure CORS properly for your frontend domain
5. **Logging**: Implement proper logging
6. **Monitoring**: Add health checks and monitoring

### Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Contributing

1. Follow the existing code structure and patterns
2. Add proper type hints and documentation
3. Write tests for new functionality
4. Update the README if needed

## License

This project is licensed under the MIT License. 