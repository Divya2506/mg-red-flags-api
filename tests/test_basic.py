"""
Basic tests to verify the application setup
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.core.database import Base, get_db


# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """Override database dependency for testing"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def client():
    """Create test client"""
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    with TestClient(app) as test_client:
        yield test_client
    
    # Clean up
    Base.metadata.drop_all(bind=engine)


def test_app_startup(client):
    """Test that the application starts up correctly"""
    response = client.get("/docs")
    assert response.status_code == 200


def test_api_health(client):
    """Test API health endpoint"""
    response = client.get("/api/v1/")
    assert response.status_code == 200


def test_openapi_schema(client):
    """Test that OpenAPI schema is generated"""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "openapi" in response.json() 