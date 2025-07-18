from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()


def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def init_db():
    """Initialize database tables"""
    # Import all models here to ensure they are registered
    from app.models import (
        user, red_flag, ocds, organization, contracting_process, 
        planning, tender, award, contract, implementation, risk_analytics
    )  # noqa
    
    # Create all tables
    Base.metadata.create_all(bind=engine) 