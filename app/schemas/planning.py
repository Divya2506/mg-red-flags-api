from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import Enum


class PlanningStatus(str, Enum):
    DRAFT = 'DRAFT'
    PENDING_APPROVAL = 'PENDING_APPROVAL'
    APPROVED = 'APPROVED'
    ACTIVE = 'ACTIVE'
    ON_HOLD = 'ON_HOLD'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class Priority(str, Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    CRITICAL = 'CRITICAL'


class ApprovalStatus(str, Enum):
    NOT_SUBMITTED = 'NOT_SUBMITTED'
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    CHANGES_REQUESTED = 'CHANGES_REQUESTED'


# Planning Item Schemas
class PlanningItemBase(BaseModel):
    """Base planning item schema"""
    title: str
    description: Optional[str] = None
    status: PlanningStatus = PlanningStatus.DRAFT
    budget_estimate: Optional[float] = None
    budget_allocated: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    organization_id: Optional[str] = None
    contracting_process_id: Optional[str] = None
    created_by: Optional[str] = None
    approval_status: ApprovalStatus = ApprovalStatus.NOT_SUBMITTED
    priority: Priority = Priority.MEDIUM
    tags: Optional[Dict[str, Any]] = None
    custom_fields: Optional[Dict[str, Any]] = None


class PlanningItemCreate(PlanningItemBase):
    """Schema for creating a planning item"""
    pass


class PlanningItemUpdate(BaseModel):
    """Schema for updating a planning item"""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[PlanningStatus] = None
    budget_estimate: Optional[float] = None
    budget_allocated: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    organization_id: Optional[str] = None
    contracting_process_id: Optional[str] = None
    approval_status: Optional[ApprovalStatus] = None
    priority: Optional[Priority] = None
    tags: Optional[Dict[str, Any]] = None
    custom_fields: Optional[Dict[str, Any]] = None


class PlanningItemInDB(PlanningItemBase):
    """Schema for planning item in database"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class PlanningItem(PlanningItemBase):
    """Schema for planning item response"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Planning Milestone Schemas
class PlanningMilestoneBase(BaseModel):
    """Base planning milestone schema"""
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: str = 'NOT_STARTED'
    completed_date: Optional[datetime] = None
    assigned_to: Optional[str] = None


class PlanningMilestoneCreate(PlanningMilestoneBase):
    """Schema for creating a planning milestone"""
    planning_item_id: str


class PlanningMilestoneUpdate(BaseModel):
    """Schema for updating a planning milestone"""
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: Optional[str] = None
    completed_date: Optional[datetime] = None
    assigned_to: Optional[str] = None


class PlanningMilestoneInDB(PlanningMilestoneBase):
    """Schema for planning milestone in database"""
    id: str
    planning_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class PlanningMilestone(PlanningMilestoneBase):
    """Schema for planning milestone response"""
    id: str
    planning_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


# Planning Stakeholder Schemas
class PlanningStakeholderBase(BaseModel):
    """Base planning stakeholder schema"""
    name: str
    user_id: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    department: Optional[str] = None


class PlanningStakeholderCreate(PlanningStakeholderBase):
    """Schema for creating a planning stakeholder"""
    planning_item_id: str


class PlanningStakeholderUpdate(BaseModel):
    """Schema for updating a planning stakeholder"""
    name: Optional[str] = None
    user_id: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    department: Optional[str] = None


class PlanningStakeholderInDB(PlanningStakeholderBase):
    """Schema for planning stakeholder in database"""
    id: str
    planning_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class PlanningStakeholder(PlanningStakeholderBase):
    """Schema for planning stakeholder response"""
    id: str
    planning_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


# Planning Risk Schemas
class PlanningRiskBase(BaseModel):
    """Base planning risk schema"""
    title: str
    description: Optional[str] = None
    probability: Optional[str] = None
    impact: Optional[str] = None
    mitigation_plan: Optional[str] = None
    status: str = 'IDENTIFIED'
    assigned_to: Optional[str] = None


class PlanningRiskCreate(PlanningRiskBase):
    """Schema for creating a planning risk"""
    planning_item_id: str


class PlanningRiskUpdate(BaseModel):
    """Schema for updating a planning risk"""
    title: Optional[str] = None
    description: Optional[str] = None
    probability: Optional[str] = None
    impact: Optional[str] = None
    mitigation_plan: Optional[str] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None


class PlanningRiskInDB(PlanningRiskBase):
    """Schema for planning risk in database"""
    id: str
    planning_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class PlanningRisk(PlanningRiskBase):
    """Schema for planning risk response"""
    id: str
    planning_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True 