from sqlalchemy import Column, String, Text, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class ContractingProcess(Base):
    """Main contracting process model"""
    __tablename__ = "contracting_processes"
    
    id = Column(String, primary_key=True)  # OCID
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(String)
    buyer_id = Column(String, ForeignKey("organizations.id"))
    value_amount = Column(Float)
    value_currency = Column(String)
    procurement_method = Column(String)
    submission_method = Column(String)
    date_published = Column(DateTime)
    tender_period_start = Column(DateTime)
    tender_period_end = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    buyer = relationship("Organization", back_populates="contracting_processes")
    red_flags = relationship("RedFlag", back_populates="contracting_process")
    planning_items = relationship("PlanningItem", back_populates="contracting_process")
    tenders = relationship("TenderItem", back_populates="contracting_process")
    awards = relationship("AwardItem", back_populates="contracting_process")
    contracts = relationship("ContractItem", back_populates="contracting_process")
    implementations = relationship("ImplementationItem", back_populates="contracting_process") 