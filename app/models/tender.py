from sqlalchemy import Column, String, Text, DateTime, Float, ForeignKey, JSON, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import enum


class TenderStatus(enum.Enum):
    PLANNING = 'PLANNING'
    PLANNED = 'PLANNED'
    ACTIVE = 'ACTIVE'
    CANCELLED = 'CANCELLED'
    UNSUCCESSFUL = 'UNSUCCESSFUL'
    COMPLETE = 'COMPLETE'
    WITHDRAWN = 'WITHDRAWN'


class TenderItem(Base):
    """Tender item model"""
    __tablename__ = "tender_items"
    
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(Enum(TenderStatus), default=TenderStatus.PLANNING)
    tender_type = Column(String)
    publication_date = Column(DateTime)
    submission_deadline = Column(DateTime)
    estimated_value = Column(Float)
    currency_code = Column(String, default='USD')
    contracting_process_id = Column(String, ForeignKey("contracting_processes.id"))
    planning_id = Column(String, ForeignKey("planning_items.id"))
    created_by = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    custom_fields = Column(JSON)
    
    # Relationships
    contracting_process = relationship("ContractingProcess", back_populates="tenders")
    planning_item = relationship("PlanningItem")
    requirements = relationship("TenderRequirement", back_populates="tender_item")
    evaluation_criteria = relationship("TenderEvaluationCriteria", back_populates="tender_item")
    responses = relationship("TenderResponse", back_populates="tender_item")


class TenderRequirement(Base):
    """Tender requirement model"""
    __tablename__ = "tender_requirements"
    
    id = Column(String, primary_key=True)
    tender_item_id = Column(String, ForeignKey("tender_items.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    type = Column(String)  # MANDATORY, OPTIONAL, INFORMATIONAL
    category = Column(String)
    weight = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    tender_item = relationship("TenderItem", back_populates="requirements")


class TenderEvaluationCriteria(Base):
    """Tender evaluation criteria model"""
    __tablename__ = "tender_evaluation_criteria"
    
    id = Column(String, primary_key=True)
    tender_item_id = Column(String, ForeignKey("tender_items.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    weight = Column(Float)
    scoring_method = Column(String)
    max_score = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    tender_item = relationship("TenderItem", back_populates="evaluation_criteria")


class TenderResponse(Base):
    """Tender response model"""
    __tablename__ = "tender_responses"
    
    id = Column(String, primary_key=True)
    tender_item_id = Column(String, ForeignKey("tender_items.id"))
    supplier_id = Column(String, ForeignKey("organizations.id"))
    submission_date = Column(DateTime)
    price = Column(Float)
    currency_code = Column(String, default='USD')
    technical_score = Column(Float)
    financial_score = Column(Float)
    total_score = Column(Float)
    status = Column(String, default='SUBMITTED')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    tender_item = relationship("TenderItem", back_populates="responses")
    supplier = relationship("Organization", back_populates="tender_responses") 