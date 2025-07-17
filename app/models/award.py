from sqlalchemy import Column, String, Text, DateTime, Float, ForeignKey, JSON, Enum, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import enum


class AwardStatus(enum.Enum):
    PENDING = 'PENDING'
    ACTIVE = 'ACTIVE'
    CANCELLED = 'CANCELLED'
    UNSUCCESSFUL = 'UNSUCCESSFUL'


class ApprovalStatus(enum.Enum):
    NOT_SUBMITTED = 'NOT_SUBMITTED'
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    CHANGES_REQUESTED = 'CHANGES_REQUESTED'


class AwardItem(Base):
    """Award item model"""
    __tablename__ = "award_items"
    
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(Enum(AwardStatus), default=AwardStatus.PENDING)
    tender_id = Column(String, ForeignKey("tender_items.id"))
    supplier_id = Column(String, ForeignKey("organizations.id"))
    award_date = Column(DateTime)
    award_value = Column(Float)
    currency_code = Column(String, default='USD')
    contracting_process_id = Column(String, ForeignKey("contracting_processes.id"))
    created_by = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    custom_fields = Column(JSON)
    
    # Relationships
    contracting_process = relationship("ContractingProcess", back_populates="awards")
    tender_item = relationship("TenderItem")
    supplier = relationship("Organization", back_populates="award_items")
    evaluations = relationship("AwardEvaluation", back_populates="award_item")
    approvals = relationship("AwardApproval", back_populates="award_item")


class AwardEvaluation(Base):
    """Award evaluation model"""
    __tablename__ = "award_evaluations"
    
    id = Column(String, primary_key=True)
    award_item_id = Column(String, ForeignKey("award_items.id"))
    tender_id = Column(String)
    supplier_id = Column(String)
    evaluator_id = Column(String)
    criteria_id = Column(String)
    score = Column(Float)
    comments = Column(Text)
    evaluated_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    award_item = relationship("AwardItem", back_populates="evaluations")


class AwardApproval(Base):
    """Award approval model"""
    __tablename__ = "award_approvals"
    
    id = Column(String, primary_key=True)
    award_item_id = Column(String, ForeignKey("award_items.id"))
    title = Column(String, nullable=False)
    approver_id = Column(String)
    approver_name = Column(String)
    status = Column(Enum(ApprovalStatus), default=ApprovalStatus.PENDING)
    comments = Column(Text)
    required_date = Column(DateTime)
    completed_date = Column(DateTime)
    order = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    award_item = relationship("AwardItem", back_populates="approvals") 