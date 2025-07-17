from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class Organization(Base):
    """Organization model for buyers, suppliers, etc."""
    __tablename__ = "organizations"
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    identifier = Column(String, unique=True)
    address = Column(Text)
    contact_point = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    contracting_processes = relationship("ContractingProcess", back_populates="buyer")
    planning_items = relationship("PlanningItem", back_populates="organization")
    tender_responses = relationship("TenderResponse", back_populates="supplier")
    award_items = relationship("AwardItem", back_populates="supplier")
    contract_items = relationship("ContractItem", back_populates="supplier") 