from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RedFlagBase(BaseModel):
    """Base red flag schema"""
    title: str
    description: str
    severity: str  # low, medium, high, critical
    confidence_score: float
    category: str
    source: str
    is_active: bool = True


class RedFlagCreate(RedFlagBase):
    """Schema for creating a red flag"""
    pass


class RedFlagUpdate(BaseModel):
    """Schema for updating a red flag"""
    title: Optional[str] = None
    description: Optional[str] = None
    severity: Optional[str] = None
    confidence_score: Optional[float] = None
    category: Optional[str] = None
    source: Optional[str] = None
    is_active: Optional[bool] = None


class RedFlagInDB(RedFlagBase):
    """Schema for red flag in database"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class RedFlag(RedFlagBase):
    """Schema for red flag response"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class RedFlagRuleBase(BaseModel):
    """Base red flag rule schema"""
    name: str
    description: str
    rule_type: str  # pattern, threshold, anomaly
    parameters: str  # JSON string
    is_active: bool = True


class RedFlagRuleCreate(RedFlagRuleBase):
    """Schema for creating a red flag rule"""
    pass


class RedFlagRuleUpdate(BaseModel):
    """Schema for updating a red flag rule"""
    name: Optional[str] = None
    description: Optional[str] = None
    rule_type: Optional[str] = None
    parameters: Optional[str] = None
    is_active: Optional[bool] = None


class RedFlagRuleInDB(RedFlagRuleBase):
    """Schema for red flag rule in database"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class RedFlagRule(RedFlagRuleBase):
    """Schema for red flag rule response"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 