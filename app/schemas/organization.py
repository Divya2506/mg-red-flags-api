from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class OrganizationBase(BaseModel):
    """Base organization schema"""
    name: str
    identifier: Optional[str] = None
    address: Optional[str] = None
    contact_point: Optional[Dict[str, Any]] = None


class OrganizationCreate(OrganizationBase):
    """Schema for creating an organization"""
    pass


class OrganizationUpdate(BaseModel):
    """Schema for updating an organization"""
    name: Optional[str] = None
    identifier: Optional[str] = None
    address: Optional[str] = None
    contact_point: Optional[Dict[str, Any]] = None


class OrganizationInDB(OrganizationBase):
    """Schema for organization in database"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class Organization(OrganizationBase):
    """Schema for organization response"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 