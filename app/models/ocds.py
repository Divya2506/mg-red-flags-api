from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, JSON
from sqlalchemy.sql import func
from app.core.database import Base


class OCDSContract(Base):
    """OCDS Contract model"""
    __tablename__ = "ocds_contracts"

    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    value_amount = Column(Float)
    value_currency = Column(String, default="USD")
    procurement_method = Column(String)
    status = Column(String)
    contract_data = Column(JSON)  # Full OCDS contract data
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class OCDSParty(Base):
    """OCDS Party model"""
    __tablename__ = "ocds_parties"

    id = Column(Integer, primary_key=True, index=True)
    party_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    party_type = Column(String)  # buyer, supplier, etc.
    contact_point = Column(JSON)
    address = Column(JSON)
    party_data = Column(JSON)  # Full OCDS party data
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class OCDSTender(Base):
    """OCDS Tender model"""
    __tablename__ = "ocds_tenders"

    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    value_amount = Column(Float)
    value_currency = Column(String, default="USD")
    procurement_method = Column(String)
    status = Column(String)
    tender_data = Column(JSON)  # Full OCDS tender data
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 