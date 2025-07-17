from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class ContractingProcessBase(BaseModel):
    """Base contracting process schema"""
    title: str
    description: Optional[str] = None
    status: Optional[str] = None
    buyer_id: Optional[str] = None
    value_amount: Optional[float] = None
    value_currency: Optional[str] = None
    procurement_method: Optional[str] = None
    submission_method: Optional[str] = None
    date_published: Optional[datetime] = None
    tender_period_start: Optional[datetime] = None
    tender_period_end: Optional[datetime] = None


class ContractingProcessCreate(ContractingProcessBase):
    """Schema for creating a contracting process"""
    pass


class ContractingProcessUpdate(BaseModel):
    """Schema for updating a contracting process"""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    buyer_id: Optional[str] = None
    value_amount: Optional[float] = None
    value_currency: Optional[str] = None
    procurement_method: Optional[str] = None
    submission_method: Optional[str] = None
    date_published: Optional[datetime] = None
    tender_period_start: Optional[datetime] = None
    tender_period_end: Optional[datetime] = None


class ContractingProcessInDB(ContractingProcessBase):
    """Schema for contracting process in database"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ContractingProcess(ContractingProcessBase):
    """Schema for contracting process response"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 