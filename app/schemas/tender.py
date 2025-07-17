from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum


class TenderStatus(str, Enum):
    PLANNING = 'PLANNING'
    PLANNED = 'PLANNED'
    ACTIVE = 'ACTIVE'
    CANCELLED = 'CANCELLED'
    UNSUCCESSFUL = 'UNSUCCESSFUL'
    COMPLETE = 'COMPLETE'
    WITHDRAWN = 'WITHDRAWN'


# Tender Item Schemas
class TenderItemBase(BaseModel):
    """Base tender item schema"""
    title: str
    description: Optional[str] = None
    status: TenderStatus = TenderStatus.PLANNING
    tender_type: Optional[str] = None
    publication_date: Optional[datetime] = None
    submission_deadline: Optional[datetime] = None
    estimated_value: Optional[float] = None
    currency_code: str = 'USD'
    contracting_process_id: Optional[str] = None
    planning_id: Optional[str] = None
    created_by: Optional[str] = None
    custom_fields: Optional[Dict[str, Any]] = None


class TenderItemCreate(TenderItemBase):
    """Schema for creating a tender item"""
    pass


class TenderItemUpdate(BaseModel):
    """Schema for updating a tender item"""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TenderStatus] = None
    tender_type: Optional[str] = None
    publication_date: Optional[datetime] = None
    submission_deadline: Optional[datetime] = None
    estimated_value: Optional[float] = None
    currency_code: Optional[str] = None
    contracting_process_id: Optional[str] = None
    planning_id: Optional[str] = None
    custom_fields: Optional[Dict[str, Any]] = None


class TenderItemInDB(TenderItemBase):
    """Schema for tender item in database"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class TenderItem(TenderItemBase):
    """Schema for tender item response"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Tender Requirement Schemas
class TenderRequirementBase(BaseModel):
    """Base tender requirement schema"""
    title: str
    description: Optional[str] = None
    type: Optional[str] = None  # MANDATORY, OPTIONAL, INFORMATIONAL
    category: Optional[str] = None
    weight: Optional[float] = None


class TenderRequirementCreate(TenderRequirementBase):
    """Schema for creating a tender requirement"""
    tender_item_id: str


class TenderRequirementUpdate(BaseModel):
    """Schema for updating a tender requirement"""
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    category: Optional[str] = None
    weight: Optional[float] = None


class TenderRequirementInDB(TenderRequirementBase):
    """Schema for tender requirement in database"""
    id: str
    tender_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class TenderRequirement(TenderRequirementBase):
    """Schema for tender requirement response"""
    id: str
    tender_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


# Tender Evaluation Criteria Schemas
class TenderEvaluationCriteriaBase(BaseModel):
    """Base tender evaluation criteria schema"""
    title: str
    description: Optional[str] = None
    weight: Optional[float] = None
    scoring_method: Optional[str] = None
    max_score: Optional[float] = None


class TenderEvaluationCriteriaCreate(TenderEvaluationCriteriaBase):
    """Schema for creating tender evaluation criteria"""
    tender_item_id: str


class TenderEvaluationCriteriaUpdate(BaseModel):
    """Schema for updating tender evaluation criteria"""
    title: Optional[str] = None
    description: Optional[str] = None
    weight: Optional[float] = None
    scoring_method: Optional[str] = None
    max_score: Optional[float] = None


class TenderEvaluationCriteriaInDB(TenderEvaluationCriteriaBase):
    """Schema for tender evaluation criteria in database"""
    id: str
    tender_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class TenderEvaluationCriteria(TenderEvaluationCriteriaBase):
    """Schema for tender evaluation criteria response"""
    id: str
    tender_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


# Tender Response Schemas
class TenderResponseBase(BaseModel):
    """Base tender response schema"""
    supplier_id: str
    submission_date: Optional[datetime] = None
    price: Optional[float] = None
    currency_code: str = 'USD'
    technical_score: Optional[float] = None
    financial_score: Optional[float] = None
    total_score: Optional[float] = None
    status: str = 'SUBMITTED'


class TenderResponseCreate(TenderResponseBase):
    """Schema for creating a tender response"""
    tender_item_id: str


class TenderResponseUpdate(BaseModel):
    """Schema for updating a tender response"""
    supplier_id: Optional[str] = None
    submission_date: Optional[datetime] = None
    price: Optional[float] = None
    currency_code: Optional[str] = None
    technical_score: Optional[float] = None
    financial_score: Optional[float] = None
    total_score: Optional[float] = None
    status: Optional[str] = None


class TenderResponseInDB(TenderResponseBase):
    """Schema for tender response in database"""
    id: str
    tender_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class TenderResponse(TenderResponseBase):
    """Schema for tender response response"""
    id: str
    tender_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True 