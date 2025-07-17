from sqlalchemy import Column, String, Text, DateTime, Float, ForeignKey, JSON, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import enum


class ImplementationStatus(enum.Enum):
    NOT_STARTED = 'NOT_STARTED'
    IN_PROGRESS = 'IN_PROGRESS'
    ON_HOLD = 'ON_HOLD'
    DELAYED = 'DELAYED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class ImplementationItem(Base):
    """Implementation item model"""
    __tablename__ = "implementation_items"
    
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(Enum(ImplementationStatus), default=ImplementationStatus.NOT_STARTED)
    contract_id = Column(String, ForeignKey("contract_items.id"))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    contracting_process_id = Column(String, ForeignKey("contracting_processes.id"))
    created_by = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    custom_fields = Column(JSON)
    
    # Relationships
    contracting_process = relationship("ContractingProcess", back_populates="implementations")
    contract_item = relationship("ContractItem")
    deliverables = relationship("ImplementationDeliverable", back_populates="implementation_item")
    issues = relationship("ImplementationIssue", back_populates="implementation_item")
    resources = relationship("ImplementationResource", back_populates="implementation_item")


class ImplementationDeliverable(Base):
    """Implementation deliverable model"""
    __tablename__ = "implementation_deliverables"
    
    id = Column(String, primary_key=True)
    implementation_item_id = Column(String, ForeignKey("implementation_items.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    due_date = Column(DateTime)
    status = Column(String, default='PENDING')  # PENDING, IN_PROGRESS, SUBMITTED, UNDER_REVIEW, ACCEPTED, REJECTED
    assigned_to = Column(String)
    completed_date = Column(DateTime)
    accepted_date = Column(DateTime)
    accepted_by = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    implementation_item = relationship("ImplementationItem", back_populates="deliverables")


class ImplementationIssue(Base):
    """Implementation issue model"""
    __tablename__ = "implementation_issues"
    
    id = Column(String, primary_key=True)
    implementation_item_id = Column(String, ForeignKey("implementation_items.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    priority = Column(String)
    severity = Column(String)  # LOW, MEDIUM, HIGH, CRITICAL
    status = Column(String, default='OPEN')  # OPEN, IN_PROGRESS, RESOLVED, CLOSED, REOPENED
    reported_by = Column(String)
    reported_at = Column(DateTime(timezone=True), server_default=func.now())
    assigned_to = Column(String)
    resolved_at = Column(DateTime)
    resolution = Column(Text)
    
    # Relationships
    implementation_item = relationship("ImplementationItem", back_populates="issues")


class ImplementationResource(Base):
    """Implementation resource model"""
    __tablename__ = "implementation_resources"
    
    id = Column(String, primary_key=True)
    implementation_item_id = Column(String, ForeignKey("implementation_items.id"))
    name = Column(String, nullable=False)
    role = Column(String)
    allocation = Column(Float)  # Percentage allocation
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String, default='ASSIGNED')  # ASSIGNED, ACTIVE, ON_LEAVE, COMPLETED, REMOVED
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    implementation_item = relationship("ImplementationItem", back_populates="resources") 