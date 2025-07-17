from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum


class ContractStatus(str, Enum):
    PENDING = 'PENDING'
    ACTIVE = 'ACTIVE'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'
    TERMINATED = 'TERMINATED'


class ApprovalStatus(str, Enum):
    NOT_SUBMITTED = 'NOT_SUBMITTED'
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    CHANGES_REQUESTED = 'CHANGES_REQUESTED'


# Contract Item Schemas
class ContractItemBase(BaseModel):
    """Base contract item schema"""
    title: str
    description: Optional[str] = None
    status: ContractStatus = ContractStatus.PENDING
    award_id: Optional[str] = None
    supplier_id: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    value: Optional[float] = None
    currency_code: str = 'USD'
    contracting_process_id: Optional[str] = None
    created_by: Optional[str] = None
    custom_fields: Optional[Dict[str, Any]] = None


class ContractItemCreate(ContractItemBase):
    """Schema for creating a contract item"""
    pass


class ContractItemUpdate(BaseModel):
    """Schema for updating a contract item"""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ContractStatus] = None
    award_id: Optional[str] = None
    supplier_id: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    value: Optional[float] = None
    currency_code: Optional[str] = None
    contracting_process_id: Optional[str] = None
    custom_fields: Optional[Dict[str, Any]] = None


class ContractItemInDB(ContractItemBase):
    """Schema for contract item in database"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ContractItem(ContractItemBase):
    """Schema for contract item response"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Contract Term Schemas
class ContractTermBase(BaseModel):
    """Base contract term schema"""
    title: str
    description: Optional[str] = None
    type: Optional[str] = None  # GENERAL, FINANCIAL, LEGAL, TECHNICAL, SERVICE_LEVEL
    is_negotiable: bool = False
    status: str = 'PROPOSED'


class ContractTermCreate(ContractTermBase):
    """Schema for creating a contract term"""
    contract_item_id: str


class ContractTermUpdate(BaseModel):
    """Schema for updating a contract term"""
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    is_negotiable: Optional[bool] = None
    status: Optional[str] = None


class ContractTermInDB(ContractTermBase):
    """Schema for contract term in database"""
    id: str
    contract_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class ContractTerm(ContractTermBase):
    """Schema for contract term response"""
    id: str
    contract_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


# Contract Amendment Schemas
class ContractAmendmentBase(BaseModel):
    """Base contract amendment schema"""
    title: str
    description: Optional[str] = None
    reason: Optional[str] = None
    status: ApprovalStatus = ApprovalStatus.PENDING
    created_by: Optional[str] = None
    approved_by: Optional[str] = None
    approved_at: Optional[datetime] = None


class ContractAmendmentCreate(ContractAmendmentBase):
    """Schema for creating a contract amendment"""
    contract_item_id: str


class ContractAmendmentUpdate(BaseModel):
    """Schema for updating a contract amendment"""
    title: Optional[str] = None
    description: Optional[str] = None
    reason: Optional[str] = None
    status: Optional[ApprovalStatus] = None
    approved_by: Optional[str] = None
    approved_at: Optional[datetime] = None


class ContractAmendmentInDB(ContractAmendmentBase):
    """Schema for contract amendment in database"""
    id: str
    contract_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class ContractAmendment(ContractAmendmentBase):
    """Schema for contract amendment response"""
    id: str
    contract_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


# Contract Performance Schemas
class ContractPerformanceBase(BaseModel):
    """Base contract performance schema"""
    metric_name: str
    description: Optional[str] = None
    target: Optional[float] = None
    actual: Optional[float] = None
    unit: Optional[str] = None
    period: Optional[str] = None
    status: Optional[str] = None  # EXCEEDING, MEETING, BELOW, CRITICAL


class ContractPerformanceCreate(ContractPerformanceBase):
    """Schema for creating contract performance"""
    contract_item_id: str


class ContractPerformanceUpdate(BaseModel):
    """Schema for updating contract performance"""
    metric_name: Optional[str] = None
    description: Optional[str] = None
    target: Optional[float] = None
    actual: Optional[float] = None
    unit: Optional[str] = None
    period: Optional[str] = None
    status: Optional[str] = None


class ContractPerformanceInDB(ContractPerformanceBase):
    """Schema for contract performance in database"""
    id: str
    contract_item_id: str
    measured_at: datetime

    class Config:
        from_attributes = True


class ContractPerformance(ContractPerformanceBase):
    """Schema for contract performance response"""
    id: str
    contract_item_id: str
    measured_at: datetime

    class Config:
        from_attributes = True 