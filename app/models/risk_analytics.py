from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class RiskProfile(Base):
    """Risk profile for entities"""
    __tablename__ = "risk_profiles"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    entity_type = Column(String, nullable=False)  # organization, tender, supplier
    entity_id = Column(String, nullable=False)
    overall_risk_score = Column(Float, nullable=False)
    corruption_risk = Column(Float, default=0.0)
    competition_risk = Column(Float, default=0.0)
    process_risk = Column(Float, default=0.0)
    supplier_risk = Column(Float, default=0.0)
    total_flags = Column(Integer, default=0)
    critical_flags = Column(Integer, default=0)
    high_flags = Column(Integer, default=0)
    medium_flags = Column(Integer, default=0)
    low_flags = Column(Integer, default=0)
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class PolicyRule(Base):
    """Policy rules for automated actions"""
    __tablename__ = "policy_rules"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    rule_code = Column(String, unique=True, nullable=False)
    rule_name = Column(String, nullable=False)
    rule_type = Column(String, nullable=False)  # blocking, warning, monitoring
    condition = Column(JSON, nullable=False)  # Rule condition as JSON
    action = Column(JSON, nullable=False)  # Action to take as JSON
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class AnalyticsEvent(Base):
    """Analytics events for tracking system usage"""
    __tablename__ = "analytics_events"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    event_type = Column(String, nullable=False)
    event_data = Column(JSON)
    user_id = Column(String)
    session_id = Column(String)
    ip_address = Column(String)
    user_agent = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class AuditLog(Base):
    """Audit log for tracking changes"""
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    table_name = Column(String, nullable=False)
    record_id = Column(String, nullable=False)
    action = Column(String, nullable=False)  # CREATE, UPDATE, DELETE
    old_values = Column(JSON)
    new_values = Column(JSON)
    user_id = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())


class RiskAssessment(Base):
    """Risk assessment model"""
    __tablename__ = "risk_assessments"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    entity_type = Column(String, nullable=False)
    entity_id = Column(String, nullable=False)
    assessment_date = Column(DateTime(timezone=True), server_default=func.now())
    assessor_id = Column(String)
    risk_factors = Column(JSON)
    mitigation_measures = Column(JSON)
    overall_risk_level = Column(String)  # LOW, MEDIUM, HIGH, CRITICAL
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 