from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum


class AwardStatus(str, Enum):
    PENDING = 'PENDING'
    ACTIVE = 'ACTIVE'
    CANCELLED = 'CANCELLED'
    UNSUCCESSFUL = 'UNSUCCESSFUL'


class ApprovalStatus(str, Enum):
    NOT_SUBMITTED = 'NOT_SUBMITTED'
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    CHANGES_REQUESTED = 'CHANGES_REQUESTED'


# Award Item Schemas
class AwardItemBase(BaseModel):
    """Base award item schema"""
    title: str
    description: Optional[str] = None
    status: AwardStatus = AwardStatus.PENDING
    tender_id: Optional[str] = None
    supplier_id: str
    award_date: Optional[datetime] = None
    award_value: Optional[float] = None
    currency_code: str = 'USD'
    contracting_process_id: Optional[str] = None
    created_by: Optional[str] = None
    custom_fields: Optional[Dict[str, Any]] = None


class AwardItemCreate(AwardItemBase):
    """Schema for creating an award item"""
    pass


class AwardItemUpdate(BaseModel):
    """Schema for updating an award item"""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[AwardStatus] = None
    tender_id: Optional[str] = None
    supplier_id: Optional[str] = None
    award_date: Optional[datetime] = None
    award_value: Optional[float] = None
    currency_code: Optional[str] = None
    contracting_process_id: Optional[str] = None
    custom_fields: Optional[Dict[str, Any]] = None


class AwardItemInDB(AwardItemBase):
    """Schema for award item in database"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class AwardItem(AwardItemBase):
    """Schema for award item response"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Award Evaluation Schemas
class AwardEvaluationBase(BaseModel):
    """Base award evaluation schema"""
    tender_id: Optional[str] = None
    supplier_id: Optional[str] = None
    evaluator_id: Optional[str] = None
    criteria_id: Optional[str] = None
    score: Optional[float] = None
    comments: Optional[str] = None


class AwardEvaluationCreate(AwardEvaluationBase):
    """Schema for creating an award evaluation"""
    award_item_id: str


class AwardEvaluationUpdate(BaseModel):
    """Schema for updating an award evaluation"""
    tender_id: Optional[str] = None
    supplier_id: Optional[str] = None
    evaluator_id: Optional[str] = None
    criteria_id: Optional[str] = None
    score: Optional[float] = None
    comments: Optional[str] = None


class AwardEvaluationInDB(AwardEvaluationBase):
    """Schema for award evaluation in database"""
    id: str
    award_item_id: str
    evaluated_at: datetime

    class Config:
        from_attributes = True


class AwardEvaluation(AwardEvaluationBase):
    """Schema for award evaluation response"""
    id: str
    award_item_id: str
    evaluated_at: datetime

    class Config:
        from_attributes = True


# Award Approval Schemas
class AwardApprovalBase(BaseModel):
    """Base award approval schema"""
    title: str
    approver_id: Optional[str] = None
    approver_name: Optional[str] = None
    status: ApprovalStatus = ApprovalStatus.PENDING
    comments: Optional[str] = None
    required_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    order: Optional[int] = None


class AwardApprovalCreate(AwardApprovalBase):
    """Schema for creating an award approval"""
    award_item_id: str


class AwardApprovalUpdate(BaseModel):
    """Schema for updating an award approval"""
    title: Optional[str] = None
    approver_id: Optional[str] = None
    approver_name: Optional[str] = None
    status: Optional[ApprovalStatus] = None
    comments: Optional[str] = None
    required_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    order: Optional[int] = None


class AwardApprovalInDB(AwardApprovalBase):
    """Schema for award approval in database"""
    id: str
    award_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class AwardApproval(AwardApprovalBase):
    """Schema for award approval response"""
    id: str
    award_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True 