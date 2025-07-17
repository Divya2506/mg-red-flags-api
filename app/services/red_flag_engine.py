from typing import List, Dict, Any
from sqlalchemy.orm import Session
import json

from app.crud.red_flag import get_active_red_flag_rules
from app.models.red_flag import RedFlagRule


class RedFlagEngine:
    """Red flag detection engine"""
    
    def __init__(self, db: Session):
        self.db = db
        self.rules = self._load_rules()
    
    def _load_rules(self) -> List[RedFlagRule]:
        """Load active red flag rules from database"""
        return get_active_red_flag_rules(self.db)
    
    def detect_red_flags(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Detect red flags in the given data"""
        detected_flags = []
        
        for rule in self.rules:
            try:
                rule_params = json.loads(rule.parameters)
                if self._evaluate_rule(data, rule.rule_type, rule_params):
                    detected_flags.append({
                        "rule_id": rule.id,
                        "rule_name": rule.name,
                        "rule_description": rule.description,
                        "rule_type": rule.rule_type,
                        "confidence_score": self._calculate_confidence(data, rule_params),
                        "severity": self._determine_severity(data, rule_params),
                        "category": rule_params.get("category", "general"),
                        "source": "rule_engine"
                    })
            except (json.JSONDecodeError, KeyError) as e:
                # Log error and continue with next rule
                print(f"Error processing rule {rule.id}: {e}")
                continue
        
        return detected_flags
    
    def _evaluate_rule(self, data: Dict[str, Any], rule_type: str, params: Dict[str, Any]) -> bool:
        """Evaluate if a rule matches the data"""
        if rule_type == "pattern":
            return self._evaluate_pattern_rule(data, params)
        elif rule_type == "threshold":
            return self._evaluate_threshold_rule(data, params)
        elif rule_type == "anomaly":
            return self._evaluate_anomaly_rule(data, params)
        else:
            return False
    
    def _evaluate_pattern_rule(self, data: Dict[str, Any], params: Dict[str, Any]) -> bool:
        """Evaluate pattern-based rules"""
        field = params.get("field")
        pattern = params.get("pattern")
        
        if not field or not pattern:
            return False
        
        value = self._get_nested_value(data, field)
        if value is None:
            return False
        
        # Simple string pattern matching
        if isinstance(value, str) and pattern.lower() in value.lower():
            return True
        
        return False
    
    def _evaluate_threshold_rule(self, data: Dict[str, Any], params: Dict[str, Any]) -> bool:
        """Evaluate threshold-based rules"""
        field = params.get("field")
        threshold = params.get("threshold")
        operator = params.get("operator", ">")
        
        if not field or threshold is None:
            return False
        
        value = self._get_nested_value(data, field)
        if value is None:
            return False
        
        try:
            value = float(value)
            threshold = float(threshold)
        except (ValueError, TypeError):
            return False
        
        if operator == ">":
            return value > threshold
        elif operator == ">=":
            return value >= threshold
        elif operator == "<":
            return value < threshold
        elif operator == "<=":
            return value <= threshold
        elif operator == "==":
            return value == threshold
        else:
            return False
    
    def _evaluate_anomaly_rule(self, data: Dict[str, Any], params: Dict[str, Any]) -> bool:
        """Evaluate anomaly-based rules"""
        # This is a simplified implementation
        # In a real system, you might use statistical methods or ML models
        field = params.get("field")
        if not field:
            return False
        
        value = self._get_nested_value(data, field)
        if value is None:
            return False
        
        # Simple anomaly detection based on value ranges
        try:
            value = float(value)
            min_val = params.get("min_value", float('-inf'))
            max_val = params.get("max_value", float('inf'))
            
            return value < min_val or value > max_val
        except (ValueError, TypeError):
            return False
    
    def _get_nested_value(self, data: Dict[str, Any], field_path: str) -> Any:
        """Get value from nested dictionary using dot notation"""
        keys = field_path.split('.')
        current = data
        
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        
        return current
    
    def _calculate_confidence(self, data: Dict[str, Any], params: Dict[str, Any]) -> float:
        """Calculate confidence score for detected red flag"""
        # This is a simplified implementation
        # In a real system, you might use more sophisticated methods
        base_confidence = params.get("base_confidence", 0.5)
        
        # Adjust confidence based on data quality
        field = params.get("field")
        if field:
            value = self._get_nested_value(data, field)
            if value is not None:
                base_confidence += 0.2
        
        return min(base_confidence, 1.0)
    
    def _determine_severity(self, data: Dict[str, Any], params: Dict[str, Any]) -> str:
        """Determine severity level for detected red flag"""
        # This is a simplified implementation
        # In a real system, you might use more sophisticated methods
        base_severity = params.get("severity", "medium")
        
        # Adjust severity based on data characteristics
        field = params.get("field")
        if field:
            value = self._get_nested_value(data, field)
            if isinstance(value, (int, float)):
                if value > 1000000:  # High value threshold
                    return "high"
                elif value > 100000:  # Medium value threshold
                    return "medium"
                else:
                    return "low"
        
        return base_severity 