from typing import Dict, List, Any
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from datetime import datetime, timedelta

from app.models.red_flag import RedFlag
from app.models.ocds import OCDSContract, OCDSParty, OCDSTender


class AnalyticsService:
    """Analytics service for data analysis and reporting"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_red_flags_summary(self) -> Dict[str, Any]:
        """Get red flags summary statistics"""
        total_flags = self.db.query(func.count(RedFlag.id)).scalar()
        active_flags = self.db.query(func.count(RedFlag.id)).filter(RedFlag.is_active == True).scalar()
        
        # Count by severity
        severity_counts = self.db.query(
            RedFlag.severity,
            func.count(RedFlag.id)
        ).group_by(RedFlag.severity).all()
        
        # Count by category
        category_counts = self.db.query(
            RedFlag.category,
            func.count(RedFlag.id)
        ).group_by(RedFlag.category).all()
        
        return {
            "total_flags": total_flags,
            "active_flags": active_flags,
            "inactive_flags": total_flags - active_flags,
            "severity_distribution": dict(severity_counts),
            "category_distribution": dict(category_counts)
        }
    
    def get_red_flags_by_severity(self) -> Dict[str, List[Dict[str, Any]]]:
        """Get red flags grouped by severity"""
        flags_by_severity = {}
        
        for severity in ["low", "medium", "high", "critical"]:
            flags = self.db.query(RedFlag).filter(
                RedFlag.severity == severity,
                RedFlag.is_active == True
            ).all()
            
            flags_by_severity[severity] = [
                {
                    "id": flag.id,
                    "title": flag.title,
                    "description": flag.description,
                    "confidence_score": flag.confidence_score,
                    "category": flag.category,
                    "created_at": flag.created_at.isoformat()
                }
                for flag in flags
            ]
        
        return flags_by_severity
    
    def get_red_flags_by_category(self) -> Dict[str, List[Dict[str, Any]]]:
        """Get red flags grouped by category"""
        categories = self.db.query(RedFlag.category).distinct().all()
        flags_by_category = {}
        
        for (category,) in categories:
            flags = self.db.query(RedFlag).filter(
                RedFlag.category == category,
                RedFlag.is_active == True
            ).all()
            
            flags_by_category[category] = [
                {
                    "id": flag.id,
                    "title": flag.title,
                    "description": flag.description,
                    "severity": flag.severity,
                    "confidence_score": flag.confidence_score,
                    "created_at": flag.created_at.isoformat()
                }
                for flag in flags
            ]
        
        return flags_by_category
    
    def get_ocds_contracts_summary(self) -> Dict[str, Any]:
        """Get OCDS contracts summary statistics"""
        total_contracts = self.db.query(func.count(OCDSContract.id)).scalar()
        
        # Total contract value
        total_value = self.db.query(func.sum(OCDSContract.value_amount)).scalar() or 0
        
        # Average contract value
        avg_value = self.db.query(func.avg(OCDSContract.value_amount)).scalar() or 0
        
        # Count by status
        status_counts = self.db.query(
            OCDSContract.status,
            func.count(OCDSContract.id)
        ).group_by(OCDSContract.status).all()
        
        # Count by procurement method
        method_counts = self.db.query(
            OCDSContract.procurement_method,
            func.count(OCDSContract.id)
        ).group_by(OCDSContract.procurement_method).all()
        
        return {
            "total_contracts": total_contracts,
            "total_value": total_value,
            "average_value": avg_value,
            "status_distribution": dict(status_counts),
            "procurement_method_distribution": dict(method_counts)
        }
    
    def get_ocds_contracts_by_value(self) -> Dict[str, List[Dict[str, Any]]]:
        """Get OCDS contracts grouped by value ranges"""
        value_ranges = [
            (0, 10000, "0-10k"),
            (10000, 100000, "10k-100k"),
            (100000, 1000000, "100k-1M"),
            (1000000, 10000000, "1M-10M"),
            (10000000, float('inf'), "10M+")
        ]
        
        contracts_by_value = {}
        
        for min_val, max_val, range_name in value_ranges:
            if max_val == float('inf'):
                contracts = self.db.query(OCDSContract).filter(
                    OCDSContract.value_amount >= min_val
                ).all()
            else:
                contracts = self.db.query(OCDSContract).filter(
                    OCDSContract.value_amount >= min_val,
                    OCDSContract.value_amount < max_val
                ).all()
            
            contracts_by_value[range_name] = [
                {
                    "id": contract.id,
                    "contract_id": contract.contract_id,
                    "title": contract.title,
                    "value_amount": contract.value_amount,
                    "value_currency": contract.value_currency,
                    "status": contract.status,
                    "procurement_method": contract.procurement_method
                }
                for contract in contracts
            ]
        
        return contracts_by_value
    
    def get_ocds_parties_summary(self) -> Dict[str, Any]:
        """Get OCDS parties summary statistics"""
        total_parties = self.db.query(func.count(OCDSParty.id)).scalar()
        
        # Count by party type
        type_counts = self.db.query(
            OCDSParty.party_type,
            func.count(OCDSParty.id)
        ).group_by(OCDSParty.party_type).all()
        
        return {
            "total_parties": total_parties,
            "party_type_distribution": dict(type_counts)
        }
    
    def get_dashboard_overview(self) -> Dict[str, Any]:
        """Get dashboard overview data"""
        # Recent red flags (last 30 days)
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)
        recent_flags = self.db.query(func.count(RedFlag.id)).filter(
            RedFlag.created_at >= thirty_days_ago
        ).scalar()
        
        # Recent contracts (last 30 days)
        recent_contracts = self.db.query(func.count(OCDSContract.id)).filter(
            OCDSContract.created_at >= thirty_days_ago
        ).scalar()
        
        # High severity flags
        high_severity_flags = self.db.query(func.count(RedFlag.id)).filter(
            RedFlag.severity.in_(["high", "critical"]),
            RedFlag.is_active == True
        ).scalar()
        
        # Total contract value
        total_contract_value = self.db.query(func.sum(OCDSContract.value_amount)).scalar() or 0
        
        return {
            "recent_red_flags": recent_flags,
            "recent_contracts": recent_contracts,
            "high_severity_flags": high_severity_flags,
            "total_contract_value": total_contract_value,
            "last_updated": datetime.utcnow().isoformat()
        } 