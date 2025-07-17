from typing import List, Optional
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.red_flag import RedFlag, RedFlagRule
from app.schemas.red_flag import RedFlagCreate, RedFlagUpdate, RedFlagRuleCreate, RedFlagRuleUpdate


class CRUDRedFlag(CRUDBase[RedFlag, RedFlagCreate, RedFlagUpdate]):
    """CRUD operations for RedFlag model"""

    def get_by_category(self, db: Session, *, category: str) -> List[RedFlag]:
        """Get red flags by category"""
        return db.query(RedFlag).filter(RedFlag.category == category).all()

    def get_by_severity(self, db: Session, *, severity: str) -> List[RedFlag]:
        """Get red flags by severity"""
        return db.query(RedFlag).filter(RedFlag.severity == severity).all()

    def get_active(self, db: Session) -> List[RedFlag]:
        """Get active red flags"""
        return db.query(RedFlag).filter(RedFlag.is_active == True).all()


class CRUDRedFlagRule(CRUDBase[RedFlagRule, RedFlagRuleCreate, RedFlagRuleUpdate]):
    """CRUD operations for RedFlagRule model"""

    def get_by_type(self, db: Session, *, rule_type: str) -> List[RedFlagRule]:
        """Get red flag rules by type"""
        return db.query(RedFlagRule).filter(RedFlagRule.rule_type == rule_type).all()

    def get_active(self, db: Session) -> List[RedFlagRule]:
        """Get active red flag rules"""
        return db.query(RedFlagRule).filter(RedFlagRule.is_active == True).all()


# Create CRUD instances
red_flag = CRUDRedFlag(RedFlag)
red_flag_rule = CRUDRedFlagRule(RedFlagRule)

# Convenience functions for RedFlag
def get_red_flag(db: Session, id: int) -> Optional[RedFlag]:
    return red_flag.get(db, id=id)


def get_red_flags(db: Session, skip: int = 0, limit: int = 100):
    return red_flag.get_multi(db, skip=skip, limit=limit)


def create_red_flag(db: Session, *, obj_in: RedFlagCreate) -> RedFlag:
    return red_flag.create(db, obj_in=obj_in)


def update_red_flag(db: Session, *, db_obj: RedFlag, obj_in: RedFlagUpdate) -> RedFlag:
    return red_flag.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_red_flag(db: Session, *, id: int) -> RedFlag:
    return red_flag.remove(db, id=id)


def get_red_flags_by_category(db: Session, *, category: str) -> List[RedFlag]:
    return red_flag.get_by_category(db, category=category)


def get_red_flags_by_severity(db: Session, *, severity: str) -> List[RedFlag]:
    return red_flag.get_by_severity(db, severity=severity)


def get_active_red_flags(db: Session) -> List[RedFlag]:
    return red_flag.get_active(db)


# Convenience functions for RedFlagRule
def get_red_flag_rule(db: Session, id: int) -> Optional[RedFlagRule]:
    return red_flag_rule.get(db, id=id)


def get_red_flag_rules(db: Session, skip: int = 0, limit: int = 100):
    return red_flag_rule.get_multi(db, skip=skip, limit=limit)


def create_red_flag_rule(db: Session, *, obj_in: RedFlagRuleCreate) -> RedFlagRule:
    return red_flag_rule.create(db, obj_in=obj_in)


def update_red_flag_rule(db: Session, *, db_obj: RedFlagRule, obj_in: RedFlagRuleUpdate) -> RedFlagRule:
    return red_flag_rule.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_red_flag_rule(db: Session, *, id: int) -> RedFlagRule:
    return red_flag_rule.remove(db, id=id)


def get_red_flag_rules_by_type(db: Session, *, rule_type: str) -> List[RedFlagRule]:
    return red_flag_rule.get_by_type(db, rule_type=rule_type)


def get_active_red_flag_rules(db: Session) -> List[RedFlagRule]:
    return red_flag_rule.get_active(db) 