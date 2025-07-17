from sqlalchemy import Column, String, Text, DateTime, Float, Boolean, ForeignKey, JSON, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import enum


class PlanningStatus(enum.Enum):
    DRAFT = 'DRAFT'
    PENDING_APPROVAL = 'PENDING_APPROVAL'
    APPROVED = 'APPROVED'
    ACTIVE = 'ACTIVE'
    ON_HOLD = 'ON_HOLD'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class Priority(enum.Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    CRITICAL = 'CRITICAL'


class ApprovalStatus(enum.Enum):
    NOT_SUBMITTED = 'NOT_SUBMITTED'
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    CHANGES_REQUESTED = 'CHANGES_REQUESTED'


class PlanningItem(Base):
    """Planning item model"""
    __tablename__ = "planning_items"
    
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(Enum(PlanningStatus), default=PlanningStatus.DRAFT)
    budget_estimate = Column(Float)
    budget_allocated = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    organization_id = Column(String, ForeignKey("organizations.id"))
    contracting_process_id = Column(String, ForeignKey("contracting_processes.id"))
    created_by = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    approval_status = Column(Enum(ApprovalStatus), default=ApprovalStatus.NOT_SUBMITTED)
    priority = Column(Enum(Priority), default=Priority.MEDIUM)
    tags = Column(JSON)
    custom_fields = Column(JSON)
    
    # Relationships
    organization = relationship("Organization", back_populates="planning_items")
    contracting_process = relationship("ContractingProcess", back_populates="planning_items")
    milestones = relationship("PlanningMilestone", back_populates="planning_item")
    stakeholders = relationship("PlanningStakeholder", back_populates="planning_item")
    risks = relationship("PlanningRisk", back_populates="planning_item")


class PlanningMilestone(Base):
    """Planning milestone model"""
    __tablename__ = "planning_milestones"
    
    id = Column(String, primary_key=True)
    planning_item_id = Column(String, ForeignKey("planning_items.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    due_date = Column(DateTime)
    status = Column(String, default='NOT_STARTED')
    completed_date = Column(DateTime)
    assigned_to = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    planning_item = relationship("PlanningItem", back_populates="milestones")


class PlanningStakeholder(Base):
    """Planning stakeholder model"""
    __tablename__ = "planning_stakeholders"
    
    id = Column(String, primary_key=True)
    planning_item_id = Column(String, ForeignKey("planning_items.id"))
    user_id = Column(String)
    name = Column(String, nullable=False)
    email = Column(String)
    role = Column(String)
    department = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    planning_item = relationship("PlanningItem", back_populates="stakeholders")


class PlanningRisk(Base):
    """Planning risk model"""
    __tablename__ = "planning_risks"
    
    id = Column(String, primary_key=True)
    planning_item_id = Column(String, ForeignKey("planning_items.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    probability = Column(String)
    impact = Column(String)
    mitigation_plan = Column(Text)
    status = Column(String, default='IDENTIFIED')
    assigned_to = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    planning_item = relationship("PlanningItem", back_populates="risks") 