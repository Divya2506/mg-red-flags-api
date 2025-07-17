from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.crud.base import CRUDBase
from app.models.award import AwardItem, AwardEvaluation, AwardApproval
from app.schemas.award import (
    AwardItemCreate, AwardItemUpdate,
    AwardEvaluationCreate, AwardEvaluationUpdate,
    AwardApprovalCreate, AwardApprovalUpdate
)


class CRUDAwardItem(CRUDBase[AwardItem, AwardItemCreate, AwardItemUpdate]):
    """CRUD operations for AwardItem model"""

    def get_by_contracting_process(self, db: Session, *, contracting_process_id: str, skip: int = 0, limit: int = 100) -> List[AwardItem]:
        """Get award items by contracting process"""
        return db.query(AwardItem).filter(AwardItem.contracting_process_id == contracting_process_id).offset(skip).limit(limit).all()

    def get_by_status(self, db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[AwardItem]:
        """Get award items by status"""
        return db.query(AwardItem).filter(AwardItem.status == status).offset(skip).limit(limit).all()

    def get_by_supplier(self, db: Session, *, supplier_id: str, skip: int = 0, limit: int = 100) -> List[AwardItem]:
        """Get award items by supplier"""
        return db.query(AwardItem).filter(AwardItem.supplier_id == supplier_id).offset(skip).limit(limit).all()

    def get_by_tender(self, db: Session, *, tender_id: str, skip: int = 0, limit: int = 100) -> List[AwardItem]:
        """Get award items by tender"""
        return db.query(AwardItem).filter(AwardItem.tender_id == tender_id).offset(skip).limit(limit).all()

    def get_by_value_range(self, db: Session, *, min_value: float, max_value: float, skip: int = 0, limit: int = 100) -> List[AwardItem]:
        """Get award items by value range"""
        return db.query(AwardItem).filter(
            and_(
                AwardItem.award_value >= min_value,
                AwardItem.award_value <= max_value
            )
        ).offset(skip).limit(limit).all()

    def get_by_date_range(self, db: Session, *, start_date: str, end_date: str, skip: int = 0, limit: int = 100) -> List[AwardItem]:
        """Get award items by date range"""
        return db.query(AwardItem).filter(
            and_(
                AwardItem.award_date >= start_date,
                AwardItem.award_date <= end_date
            )
        ).offset(skip).limit(limit).all()


class CRUDAwardEvaluation(CRUDBase[AwardEvaluation, AwardEvaluationCreate, AwardEvaluationUpdate]):
    """CRUD operations for AwardEvaluation model"""

    def get_by_award_item(self, db: Session, *, award_item_id: str) -> List[AwardEvaluation]:
        """Get evaluations by award item"""
        return db.query(AwardEvaluation).filter(AwardEvaluation.award_item_id == award_item_id).all()

    def get_by_evaluator(self, db: Session, *, evaluator_id: str, skip: int = 0, limit: int = 100) -> List[AwardEvaluation]:
        """Get evaluations by evaluator"""
        return db.query(AwardEvaluation).filter(AwardEvaluation.evaluator_id == evaluator_id).offset(skip).limit(limit).all()

    def get_by_supplier(self, db: Session, *, supplier_id: str, skip: int = 0, limit: int = 100) -> List[AwardEvaluation]:
        """Get evaluations by supplier"""
        return db.query(AwardEvaluation).filter(AwardEvaluation.supplier_id == supplier_id).offset(skip).limit(limit).all()

    def get_by_score_range(self, db: Session, *, min_score: float, max_score: float, skip: int = 0, limit: int = 100) -> List[AwardEvaluation]:
        """Get evaluations by score range"""
        return db.query(AwardEvaluation).filter(
            and_(
                AwardEvaluation.score >= min_score,
                AwardEvaluation.score <= max_score
            )
        ).offset(skip).limit(limit).all()


class CRUDAwardApproval(CRUDBase[AwardApproval, AwardApprovalCreate, AwardApprovalUpdate]):
    """CRUD operations for AwardApproval model"""

    def get_by_award_item(self, db: Session, *, award_item_id: str) -> List[AwardApproval]:
        """Get approvals by award item"""
        return db.query(AwardApproval).filter(AwardApproval.award_item_id == award_item_id).all()

    def get_by_status(self, db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[AwardApproval]:
        """Get approvals by status"""
        return db.query(AwardApproval).filter(AwardApproval.status == status).offset(skip).limit(limit).all()

    def get_by_approver(self, db: Session, *, approver_id: str, skip: int = 0, limit: int = 100) -> List[AwardApproval]:
        """Get approvals by approver"""
        return db.query(AwardApproval).filter(AwardApproval.approver_id == approver_id).offset(skip).limit(limit).all()

    def get_by_order(self, db: Session, *, award_item_id: str, order: int) -> Optional[AwardApproval]:
        """Get approval by order"""
        return db.query(AwardApproval).filter(
            and_(
                AwardApproval.award_item_id == award_item_id,
                AwardApproval.order == order
            )
        ).first()

    def get_pending_approvals(self, db: Session, *, award_item_id: str) -> List[AwardApproval]:
        """Get pending approvals for an award item"""
        return db.query(AwardApproval).filter(
            and_(
                AwardApproval.award_item_id == award_item_id,
                AwardApproval.status == "PENDING"
            )
        ).order_by(AwardApproval.order).all()


# Create CRUD instances
award_item = CRUDAwardItem(AwardItem)
award_evaluation = CRUDAwardEvaluation(AwardEvaluation)
award_approval = CRUDAwardApproval(AwardApproval)

# Convenience functions for AwardItem
def get_award_item(db: Session, id: str) -> Optional[AwardItem]:
    return award_item.get(db, id=id)


def get_award_items(db: Session, skip: int = 0, limit: int = 100) -> List[AwardItem]:
    return award_item.get_multi(db, skip=skip, limit=limit)


def create_award_item(db: Session, *, obj_in: AwardItemCreate) -> AwardItem:
    return award_item.create(db, obj_in=obj_in)


def update_award_item(db: Session, *, db_obj: AwardItem, obj_in: AwardItemUpdate) -> AwardItem:
    return award_item.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_award_item(db: Session, *, id: str) -> AwardItem:
    return award_item.remove(db, id=id)


def get_award_items_by_contracting_process(db: Session, *, contracting_process_id: str, skip: int = 0, limit: int = 100) -> List[AwardItem]:
    return award_item.get_by_contracting_process(db, contracting_process_id=contracting_process_id, skip=skip, limit=limit)


def get_award_items_by_status(db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[AwardItem]:
    return award_item.get_by_status(db, status=status, skip=skip, limit=limit)


def get_award_items_by_supplier(db: Session, *, supplier_id: str, skip: int = 0, limit: int = 100) -> List[AwardItem]:
    return award_item.get_by_supplier(db, supplier_id=supplier_id, skip=skip, limit=limit)


def get_award_items_by_tender(db: Session, *, tender_id: str, skip: int = 0, limit: int = 100) -> List[AwardItem]:
    return award_item.get_by_tender(db, tender_id=tender_id, skip=skip, limit=limit)


def get_award_items_by_value_range(db: Session, *, min_value: float, max_value: float, skip: int = 0, limit: int = 100) -> List[AwardItem]:
    return award_item.get_by_value_range(db, min_value=min_value, max_value=max_value, skip=skip, limit=limit)


def get_award_items_by_date_range(db: Session, *, start_date: str, end_date: str, skip: int = 0, limit: int = 100) -> List[AwardItem]:
    return award_item.get_by_date_range(db, start_date=start_date, end_date=end_date, skip=skip, limit=limit)


# Convenience functions for AwardEvaluation
def get_award_evaluation(db: Session, id: str) -> Optional[AwardEvaluation]:
    return award_evaluation.get(db, id=id)


def get_award_evaluations(db: Session, skip: int = 0, limit: int = 100) -> List[AwardEvaluation]:
    return award_evaluation.get_multi(db, skip=skip, limit=limit)


def create_award_evaluation(db: Session, *, obj_in: AwardEvaluationCreate) -> AwardEvaluation:
    return award_evaluation.create(db, obj_in=obj_in)


def update_award_evaluation(db: Session, *, db_obj: AwardEvaluation, obj_in: AwardEvaluationUpdate) -> AwardEvaluation:
    return award_evaluation.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_award_evaluation(db: Session, *, id: str) -> AwardEvaluation:
    return award_evaluation.remove(db, id=id)


def get_evaluations_by_award_item(db: Session, *, award_item_id: str) -> List[AwardEvaluation]:
    return award_evaluation.get_by_award_item(db, award_item_id=award_item_id)


def get_evaluations_by_evaluator(db: Session, *, evaluator_id: str, skip: int = 0, limit: int = 100) -> List[AwardEvaluation]:
    return award_evaluation.get_by_evaluator(db, evaluator_id=evaluator_id, skip=skip, limit=limit)


def get_evaluations_by_supplier(db: Session, *, supplier_id: str, skip: int = 0, limit: int = 100) -> List[AwardEvaluation]:
    return award_evaluation.get_by_supplier(db, supplier_id=supplier_id, skip=skip, limit=limit)


def get_evaluations_by_score_range(db: Session, *, min_score: float, max_score: float, skip: int = 0, limit: int = 100) -> List[AwardEvaluation]:
    return award_evaluation.get_by_score_range(db, min_score=min_score, max_score=max_score, skip=skip, limit=limit)


# Convenience functions for AwardApproval
def get_award_approval(db: Session, id: str) -> Optional[AwardApproval]:
    return award_approval.get(db, id=id)


def get_award_approvals(db: Session, skip: int = 0, limit: int = 100) -> List[AwardApproval]:
    return award_approval.get_multi(db, skip=skip, limit=limit)


def create_award_approval(db: Session, *, obj_in: AwardApprovalCreate) -> AwardApproval:
    return award_approval.create(db, obj_in=obj_in)


def update_award_approval(db: Session, *, db_obj: AwardApproval, obj_in: AwardApprovalUpdate) -> AwardApproval:
    return award_approval.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_award_approval(db: Session, *, id: str) -> AwardApproval:
    return award_approval.remove(db, id=id)


def get_approvals_by_award_item(db: Session, *, award_item_id: str) -> List[AwardApproval]:
    return award_approval.get_by_award_item(db, award_item_id=award_item_id)


def get_approvals_by_status(db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[AwardApproval]:
    return award_approval.get_by_status(db, status=status, skip=skip, limit=limit)


def get_approvals_by_approver(db: Session, *, approver_id: str, skip: int = 0, limit: int = 100) -> List[AwardApproval]:
    return award_approval.get_by_approver(db, approver_id=approver_id, skip=skip, limit=limit)


def get_approval_by_order(db: Session, *, award_item_id: str, order: int) -> Optional[AwardApproval]:
    return award_approval.get_by_order(db, award_item_id=award_item_id, order=order)


def get_pending_approvals(db: Session, *, award_item_id: str) -> List[AwardApproval]:
    return award_approval.get_pending_approvals(db, award_item_id=award_item_id) 