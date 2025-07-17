from sqlalchemy import Column, String, Text, DateTime, Float, Boolean, ForeignKey, JSON, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import enum


class ContractStatus(enum.Enum):
    PENDING = 'PENDING'
    ACTIVE = 'ACTIVE'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'
    TERMINATED = 'TERMINATED'


class ApprovalStatus(enum.Enum):
    NOT_SUBMITTED = 'NOT_SUBMITTED'
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    CHANGES_REQUESTED = 'CHANGES_REQUESTED'


class ContractItem(Base):
    """Contract item model"""
    __tablename__ = "contract_items"
    
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(Enum(ContractStatus), default=ContractStatus.PENDING)
    award_id = Column(String, ForeignKey("award_items.id"))
    supplier_id = Column(String, ForeignKey("organizations.id"))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    value = Column(Float)
    currency_code = Column(String, default='USD')
    contracting_process_id = Column(String, ForeignKey("contracting_processes.id"))
    created_by = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    custom_fields = Column(JSON)
    
    # Relationships
    contracting_process = relationship("ContractingProcess", back_populates="contracts")
    award_item = relationship("AwardItem")
    supplier = relationship("Organization", back_populates="contract_items")
    terms = relationship("ContractTerm", back_populates="contract_item")
    amendments = relationship("ContractAmendment", back_populates="contract_item")
    performance = relationship("ContractPerformance", back_populates="contract_item")


class ContractTerm(Base):
    """Contract term model"""
    __tablename__ = "contract_terms"
    
    id = Column(String, primary_key=True)
    contract_item_id = Column(String, ForeignKey("contract_items.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    type = Column(String)  # GENERAL, FINANCIAL, LEGAL, TECHNICAL, SERVICE_LEVEL
    is_negotiable = Column(Boolean, default=False)
    status = Column(String, default='PROPOSED')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    contract_item = relationship("ContractItem", back_populates="terms")


class ContractAmendment(Base):
    """Contract amendment model"""
    __tablename__ = "contract_amendments"
    
    id = Column(String, primary_key=True)
    contract_item_id = Column(String, ForeignKey("contract_items.id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    reason = Column(Text)
    status = Column(Enum(ApprovalStatus), default=ApprovalStatus.PENDING)
    created_by = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    approved_by = Column(String)
    approved_at = Column(DateTime)
    
    # Relationships
    contract_item = relationship("ContractItem", back_populates="amendments")


class ContractPerformance(Base):
    """Contract performance model"""
    __tablename__ = "contract_performance"
    
    id = Column(String, primary_key=True)
    contract_item_id = Column(String, ForeignKey("contract_items.id"))
    metric_name = Column(String, nullable=False)
    description = Column(Text)
    target = Column(Float)
    actual = Column(Float)
    unit = Column(String)
    period = Column(String)
    status = Column(String)  # EXCEEDING, MEETING, BELOW, CRITICAL
    measured_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    contract_item = relationship("ContractItem", back_populates="performance") 