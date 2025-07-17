from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


# Risk Profile Schemas
class RiskProfileBase(BaseModel):
    """Base risk profile schema"""
    entity_type: str  # organization, tender, supplier
    entity_id: str
    overall_risk_score: float
    corruption_risk: float = 0.0
    competition_risk: float = 0.0
    process_risk: float = 0.0
    supplier_risk: float = 0.0
    total_flags: int = 0
    critical_flags: int = 0
    high_flags: int = 0
    medium_flags: int = 0
    low_flags: int = 0


class RiskProfileCreate(RiskProfileBase):
    """Schema for creating a risk profile"""
    pass


class RiskProfileUpdate(BaseModel):
    """Schema for updating a risk profile"""
    overall_risk_score: Optional[float] = None
    corruption_risk: Optional[float] = None
    competition_risk: Optional[float] = None
    process_risk: Optional[float] = None
    supplier_risk: Optional[float] = None
    total_flags: Optional[int] = None
    critical_flags: Optional[int] = None
    high_flags: Optional[int] = None
    medium_flags: Optional[int] = None
    low_flags: Optional[int] = None


class RiskProfileInDB(RiskProfileBase):
    """Schema for risk profile in database"""
    id: int
    last_updated: datetime

    class Config:
        from_attributes = True


class RiskProfile(RiskProfileBase):
    """Schema for risk profile response"""
    id: int
    last_updated: datetime

    class Config:
        from_attributes = True


# Policy Rule Schemas
class PolicyRuleBase(BaseModel):
    """Base policy rule schema"""
    rule_code: str
    rule_name: str
    rule_type: str  # blocking, warning, monitoring
    condition: Dict[str, Any]
    action: Dict[str, Any]
    is_active: bool = True


class PolicyRuleCreate(PolicyRuleBase):
    """Schema for creating a policy rule"""
    pass


class PolicyRuleUpdate(BaseModel):
    """Schema for updating a policy rule"""
    rule_name: Optional[str] = None
    rule_type: Optional[str] = None
    condition: Optional[Dict[str, Any]] = None
    action: Optional[Dict[str, Any]] = None
    is_active: Optional[bool] = None


class PolicyRuleInDB(PolicyRuleBase):
    """Schema for policy rule in database"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class PolicyRule(PolicyRuleBase):
    """Schema for policy rule response"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Analytics Event Schemas
class AnalyticsEventBase(BaseModel):
    """Base analytics event schema"""
    event_type: str
    event_data: Optional[Dict[str, Any]] = None
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None


class AnalyticsEventCreate(AnalyticsEventBase):
    """Schema for creating an analytics event"""
    pass


class AnalyticsEventInDB(AnalyticsEventBase):
    """Schema for analytics event in database"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class AnalyticsEvent(AnalyticsEventBase):
    """Schema for analytics event response"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Audit Log Schemas
class AuditLogBase(BaseModel):
    """Base audit log schema"""
    table_name: str
    record_id: str
    action: str  # CREATE, UPDATE, DELETE
    old_values: Optional[Dict[str, Any]] = None
    new_values: Optional[Dict[str, Any]] = None
    user_id: Optional[str] = None


class AuditLogCreate(AuditLogBase):
    """Schema for creating an audit log"""
    pass


class AuditLogInDB(AuditLogBase):
    """Schema for audit log in database"""
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True


class AuditLog(AuditLogBase):
    """Schema for audit log response"""
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True


# Risk Assessment Schemas
class RiskAssessmentBase(BaseModel):
    """Base risk assessment schema"""
    entity_type: str
    entity_id: str
    assessor_id: Optional[str] = None
    risk_factors: Optional[Dict[str, Any]] = None
    mitigation_measures: Optional[Dict[str, Any]] = None
    overall_risk_level: Optional[str] = None  # LOW, MEDIUM, HIGH, CRITICAL
    notes: Optional[str] = None


class RiskAssessmentCreate(RiskAssessmentBase):
    """Schema for creating a risk assessment"""
    pass


class RiskAssessmentUpdate(BaseModel):
    """Schema for updating a risk assessment"""
    assessor_id: Optional[str] = None
    risk_factors: Optional[Dict[str, Any]] = None
    mitigation_measures: Optional[Dict[str, Any]] = None
    overall_risk_level: Optional[str] = None
    notes: Optional[str] = None


class RiskAssessmentInDB(RiskAssessmentBase):
    """Schema for risk assessment in database"""
    id: int
    assessment_date: datetime
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class RiskAssessment(RiskAssessmentBase):
    """Schema for risk assessment response"""
    id: int
    assessment_date: datetime
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 