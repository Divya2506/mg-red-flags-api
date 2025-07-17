from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.crud.base import CRUDBase
from app.models.planning import PlanningItem, PlanningMilestone, PlanningStakeholder, PlanningRisk
from app.schemas.planning import (
    PlanningItemCreate, PlanningItemUpdate,
    PlanningMilestoneCreate, PlanningMilestoneUpdate,
    PlanningStakeholderCreate, PlanningStakeholderUpdate,
    PlanningRiskCreate, PlanningRiskUpdate
)


class CRUDPlanningItem(CRUDBase[PlanningItem, PlanningItemCreate, PlanningItemUpdate]):
    """CRUD operations for PlanningItem model"""

    def get_by_organization(self, db: Session, *, organization_id: str, skip: int = 0, limit: int = 100) -> List[PlanningItem]:
        """Get planning items by organization"""
        return db.query(PlanningItem).filter(PlanningItem.organization_id == organization_id).offset(skip).limit(limit).all()

    def get_by_status(self, db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[PlanningItem]:
        """Get planning items by status"""
        return db.query(PlanningItem).filter(PlanningItem.status == status).offset(skip).limit(limit).all()

    def get_by_priority(self, db: Session, *, priority: str, skip: int = 0, limit: int = 100) -> List[PlanningItem]:
        """Get planning items by priority"""
        return db.query(PlanningItem).filter(PlanningItem.priority == priority).offset(skip).limit(limit).all()

    def get_by_approval_status(self, db: Session, *, approval_status: str, skip: int = 0, limit: int = 100) -> List[PlanningItem]:
        """Get planning items by approval status"""
        return db.query(PlanningItem).filter(PlanningItem.approval_status == approval_status).offset(skip).limit(limit).all()

    def get_by_date_range(self, db: Session, *, start_date: str, end_date: str, skip: int = 0, limit: int = 100) -> List[PlanningItem]:
        """Get planning items by date range"""
        return db.query(PlanningItem).filter(
            and_(
                PlanningItem.start_date >= start_date,
                PlanningItem.end_date <= end_date
            )
        ).offset(skip).limit(limit).all()


class CRUDPlanningMilestone(CRUDBase[PlanningMilestone, PlanningMilestoneCreate, PlanningMilestoneUpdate]):
    """CRUD operations for PlanningMilestone model"""

    def get_by_planning_item(self, db: Session, *, planning_item_id: str) -> List[PlanningMilestone]:
        """Get milestones by planning item"""
        return db.query(PlanningMilestone).filter(PlanningMilestone.planning_item_id == planning_item_id).all()

    def get_by_status(self, db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[PlanningMilestone]:
        """Get milestones by status"""
        return db.query(PlanningMilestone).filter(PlanningMilestone.status == status).offset(skip).limit(limit).all()

    def get_by_assigned_to(self, db: Session, *, assigned_to: str, skip: int = 0, limit: int = 100) -> List[PlanningMilestone]:
        """Get milestones by assigned person"""
        return db.query(PlanningMilestone).filter(PlanningMilestone.assigned_to == assigned_to).offset(skip).limit(limit).all()


class CRUDPlanningStakeholder(CRUDBase[PlanningStakeholder, PlanningStakeholderCreate, PlanningStakeholderUpdate]):
    """CRUD operations for PlanningStakeholder model"""

    def get_by_planning_item(self, db: Session, *, planning_item_id: str) -> List[PlanningStakeholder]:
        """Get stakeholders by planning item"""
        return db.query(PlanningStakeholder).filter(PlanningStakeholder.planning_item_id == planning_item_id).all()

    def get_by_role(self, db: Session, *, role: str, skip: int = 0, limit: int = 100) -> List[PlanningStakeholder]:
        """Get stakeholders by role"""
        return db.query(PlanningStakeholder).filter(PlanningStakeholder.role == role).offset(skip).limit(limit).all()

    def get_by_email(self, db: Session, *, email: str) -> Optional[PlanningStakeholder]:
        """Get stakeholder by email"""
        return db.query(PlanningStakeholder).filter(PlanningStakeholder.email == email).first()


class CRUDPlanningRisk(CRUDBase[PlanningRisk, PlanningRiskCreate, PlanningRiskUpdate]):
    """CRUD operations for PlanningRisk model"""

    def get_by_planning_item(self, db: Session, *, planning_item_id: str) -> List[PlanningRisk]:
        """Get risks by planning item"""
        return db.query(PlanningRisk).filter(PlanningRisk.planning_item_id == planning_item_id).all()

    def get_by_status(self, db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[PlanningRisk]:
        """Get risks by status"""
        return db.query(PlanningRisk).filter(PlanningRisk.status == status).offset(skip).limit(limit).all()

    def get_by_assigned_to(self, db: Session, *, assigned_to: str, skip: int = 0, limit: int = 100) -> List[PlanningRisk]:
        """Get risks by assigned person"""
        return db.query(PlanningRisk).filter(PlanningRisk.assigned_to == assigned_to).offset(skip).limit(limit).all()


# Create CRUD instances
planning_item = CRUDPlanningItem(PlanningItem)
planning_milestone = CRUDPlanningMilestone(PlanningMilestone)
planning_stakeholder = CRUDPlanningStakeholder(PlanningStakeholder)
planning_risk = CRUDPlanningRisk(PlanningRisk)

# Convenience functions for PlanningItem
def get_planning_item(db: Session, id: str) -> Optional[PlanningItem]:
    return planning_item.get(db, id=id)


def get_planning_items(db: Session, skip: int = 0, limit: int = 100) -> List[PlanningItem]:
    return planning_item.get_multi(db, skip=skip, limit=limit)


def create_planning_item(db: Session, *, obj_in: PlanningItemCreate) -> PlanningItem:
    return planning_item.create(db, obj_in=obj_in)


def update_planning_item(db: Session, *, db_obj: PlanningItem, obj_in: PlanningItemUpdate) -> PlanningItem:
    return planning_item.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_planning_item(db: Session, *, id: str) -> PlanningItem:
    return planning_item.remove(db, id=id)


def get_planning_items_by_organization(db: Session, *, organization_id: str, skip: int = 0, limit: int = 100) -> List[PlanningItem]:
    return planning_item.get_by_organization(db, organization_id=organization_id, skip=skip, limit=limit)


def get_planning_items_by_status(db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[PlanningItem]:
    return planning_item.get_by_status(db, status=status, skip=skip, limit=limit)


def get_planning_items_by_priority(db: Session, *, priority: str, skip: int = 0, limit: int = 100) -> List[PlanningItem]:
    return planning_item.get_by_priority(db, priority=priority, skip=skip, limit=limit)


def get_planning_items_by_approval_status(db: Session, *, approval_status: str, skip: int = 0, limit: int = 100) -> List[PlanningItem]:
    return planning_item.get_by_approval_status(db, approval_status=approval_status, skip=skip, limit=limit)


# Convenience functions for PlanningMilestone
def get_planning_milestone(db: Session, id: str) -> Optional[PlanningMilestone]:
    return planning_milestone.get(db, id=id)


def get_planning_milestones(db: Session, skip: int = 0, limit: int = 100) -> List[PlanningMilestone]:
    return planning_milestone.get_multi(db, skip=skip, limit=limit)


def create_planning_milestone(db: Session, *, obj_in: PlanningMilestoneCreate) -> PlanningMilestone:
    return planning_milestone.create(db, obj_in=obj_in)


def update_planning_milestone(db: Session, *, db_obj: PlanningMilestone, obj_in: PlanningMilestoneUpdate) -> PlanningMilestone:
    return planning_milestone.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_planning_milestone(db: Session, *, id: str) -> PlanningMilestone:
    return planning_milestone.remove(db, id=id)


def get_milestones_by_planning_item(db: Session, *, planning_item_id: str) -> List[PlanningMilestone]:
    return planning_milestone.get_by_planning_item(db, planning_item_id=planning_item_id)


# Convenience functions for PlanningStakeholder
def get_planning_stakeholder(db: Session, id: str) -> Optional[PlanningStakeholder]:
    return planning_stakeholder.get(db, id=id)


def get_planning_stakeholders(db: Session, skip: int = 0, limit: int = 100) -> List[PlanningStakeholder]:
    return planning_stakeholder.get_multi(db, skip=skip, limit=limit)


def create_planning_stakeholder(db: Session, *, obj_in: PlanningStakeholderCreate) -> PlanningStakeholder:
    return planning_stakeholder.create(db, obj_in=obj_in)


def update_planning_stakeholder(db: Session, *, db_obj: PlanningStakeholder, obj_in: PlanningStakeholderUpdate) -> PlanningStakeholder:
    return planning_stakeholder.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_planning_stakeholder(db: Session, *, id: str) -> PlanningStakeholder:
    return planning_stakeholder.remove(db, id=id)


def get_stakeholders_by_planning_item(db: Session, *, planning_item_id: str) -> List[PlanningStakeholder]:
    return planning_stakeholder.get_by_planning_item(db, planning_item_id=planning_item_id)


# Convenience functions for PlanningRisk
def get_planning_risk(db: Session, id: str) -> Optional[PlanningRisk]:
    return planning_risk.get(db, id=id)


def get_planning_risks(db: Session, skip: int = 0, limit: int = 100) -> List[PlanningRisk]:
    return planning_risk.get_multi(db, skip=skip, limit=limit)


def create_planning_risk(db: Session, *, obj_in: PlanningRiskCreate) -> PlanningRisk:
    return planning_risk.create(db, obj_in=obj_in)


def update_planning_risk(db: Session, *, db_obj: PlanningRisk, obj_in: PlanningRiskUpdate) -> PlanningRisk:
    return planning_risk.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_planning_risk(db: Session, *, id: str) -> PlanningRisk:
    return planning_risk.remove(db, id=id)


def get_risks_by_planning_item(db: Session, *, planning_item_id: str) -> List[PlanningRisk]:
    return planning_risk.get_by_planning_item(db, planning_item_id=planning_item_id) 