from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum


class ImplementationStatus(str, Enum):
    NOT_STARTED = 'NOT_STARTED'
    IN_PROGRESS = 'IN_PROGRESS'
    ON_HOLD = 'ON_HOLD'
    DELAYED = 'DELAYED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


# Implementation Item Schemas
class ImplementationItemBase(BaseModel):
    """Base implementation item schema"""
    title: str
    description: Optional[str] = None
    status: ImplementationStatus = ImplementationStatus.NOT_STARTED
    contract_id: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    contracting_process_id: Optional[str] = None
    created_by: Optional[str] = None
    custom_fields: Optional[Dict[str, Any]] = None


class ImplementationItemCreate(ImplementationItemBase):
    """Schema for creating an implementation item"""
    pass


class ImplementationItemUpdate(BaseModel):
    """Schema for updating an implementation item"""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ImplementationStatus] = None
    contract_id: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    contracting_process_id: Optional[str] = None
    custom_fields: Optional[Dict[str, Any]] = None


class ImplementationItemInDB(ImplementationItemBase):
    """Schema for implementation item in database"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ImplementationItem(ImplementationItemBase):
    """Schema for implementation item response"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Implementation Deliverable Schemas
class ImplementationDeliverableBase(BaseModel):
    """Base implementation deliverable schema"""
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: str = 'PENDING'  # PENDING, IN_PROGRESS, SUBMITTED, UNDER_REVIEW, ACCEPTED, REJECTED
    assigned_to: Optional[str] = None
    completed_date: Optional[datetime] = None
    accepted_date: Optional[datetime] = None
    accepted_by: Optional[str] = None


class ImplementationDeliverableCreate(ImplementationDeliverableBase):
    """Schema for creating an implementation deliverable"""
    implementation_item_id: str


class ImplementationDeliverableUpdate(BaseModel):
    """Schema for updating an implementation deliverable"""
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    completed_date: Optional[datetime] = None
    accepted_date: Optional[datetime] = None
    accepted_by: Optional[str] = None


class ImplementationDeliverableInDB(ImplementationDeliverableBase):
    """Schema for implementation deliverable in database"""
    id: str
    implementation_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class ImplementationDeliverable(ImplementationDeliverableBase):
    """Schema for implementation deliverable response"""
    id: str
    implementation_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


# Implementation Issue Schemas
class ImplementationIssueBase(BaseModel):
    """Base implementation issue schema"""
    title: str
    description: Optional[str] = None
    priority: Optional[str] = None
    severity: Optional[str] = None  # LOW, MEDIUM, HIGH, CRITICAL
    status: str = 'OPEN'  # OPEN, IN_PROGRESS, RESOLVED, CLOSED, REOPENED
    reported_by: Optional[str] = None
    assigned_to: Optional[str] = None
    resolved_at: Optional[datetime] = None
    resolution: Optional[str] = None


class ImplementationIssueCreate(ImplementationIssueBase):
    """Schema for creating an implementation issue"""
    implementation_item_id: str


class ImplementationIssueUpdate(BaseModel):
    """Schema for updating an implementation issue"""
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    severity: Optional[str] = None
    status: Optional[str] = None
    reported_by: Optional[str] = None
    assigned_to: Optional[str] = None
    resolved_at: Optional[datetime] = None
    resolution: Optional[str] = None


class ImplementationIssueInDB(ImplementationIssueBase):
    """Schema for implementation issue in database"""
    id: str
    implementation_item_id: str
    reported_at: datetime

    class Config:
        from_attributes = True


class ImplementationIssue(ImplementationIssueBase):
    """Schema for implementation issue response"""
    id: str
    implementation_item_id: str
    reported_at: datetime

    class Config:
        from_attributes = True


# Implementation Resource Schemas
class ImplementationResourceBase(BaseModel):
    """Base implementation resource schema"""
    name: str
    role: Optional[str] = None
    allocation: Optional[float] = None  # Percentage allocation
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: str = 'ASSIGNED'  # ASSIGNED, ACTIVE, ON_LEAVE, COMPLETED, REMOVED


class ImplementationResourceCreate(ImplementationResourceBase):
    """Schema for creating an implementation resource"""
    implementation_item_id: str


class ImplementationResourceUpdate(BaseModel):
    """Schema for updating an implementation resource"""
    name: Optional[str] = None
    role: Optional[str] = None
    allocation: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = None


class ImplementationResourceInDB(ImplementationResourceBase):
    """Schema for implementation resource in database"""
    id: str
    implementation_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class ImplementationResource(ImplementationResourceBase):
    """Schema for implementation resource response"""
    id: str
    implementation_item_id: str
    created_at: datetime

    class Config:
        from_attributes = True 