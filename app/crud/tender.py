from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.crud.base import CRUDBase
from app.models.tender import TenderItem, TenderRequirement, TenderEvaluationCriteria, TenderResponse
from app.schemas.tender import (
    TenderItemCreate, TenderItemUpdate,
    TenderRequirementCreate, TenderRequirementUpdate,
    TenderEvaluationCriteriaCreate, TenderEvaluationCriteriaUpdate,
    TenderResponseCreate, TenderResponseUpdate
)


class CRUDTenderItem(CRUDBase[TenderItem, TenderItemCreate, TenderItemUpdate]):
    """CRUD operations for TenderItem model"""

    def get_by_contracting_process(self, db: Session, *, contracting_process_id: str, skip: int = 0, limit: int = 100) -> List[TenderItem]:
        """Get tender items by contracting process"""
        return db.query(TenderItem).filter(TenderItem.contracting_process_id == contracting_process_id).offset(skip).limit(limit).all()

    def get_by_status(self, db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[TenderItem]:
        """Get tender items by status"""
        return db.query(TenderItem).filter(TenderItem.status == status).offset(skip).limit(limit).all()

    def get_by_tender_type(self, db: Session, *, tender_type: str, skip: int = 0, limit: int = 100) -> List[TenderItem]:
        """Get tender items by tender type"""
        return db.query(TenderItem).filter(TenderItem.tender_type == tender_type).offset(skip).limit(limit).all()

    def get_by_value_range(self, db: Session, *, min_value: float, max_value: float, skip: int = 0, limit: int = 100) -> List[TenderItem]:
        """Get tender items by value range"""
        return db.query(TenderItem).filter(
            and_(
                TenderItem.estimated_value >= min_value,
                TenderItem.estimated_value <= max_value
            )
        ).offset(skip).limit(limit).all()

    def get_by_date_range(self, db: Session, *, start_date: str, end_date: str, skip: int = 0, limit: int = 100) -> List[TenderItem]:
        """Get tender items by date range"""
        return db.query(TenderItem).filter(
            and_(
                TenderItem.publication_date >= start_date,
                TenderItem.submission_deadline <= end_date
            )
        ).offset(skip).limit(limit).all()


class CRUDTenderRequirement(CRUDBase[TenderRequirement, TenderRequirementCreate, TenderRequirementUpdate]):
    """CRUD operations for TenderRequirement model"""

    def get_by_tender_item(self, db: Session, *, tender_item_id: str) -> List[TenderRequirement]:
        """Get requirements by tender item"""
        return db.query(TenderRequirement).filter(TenderRequirement.tender_item_id == tender_item_id).all()

    def get_by_type(self, db: Session, *, type: str, skip: int = 0, limit: int = 100) -> List[TenderRequirement]:
        """Get requirements by type"""
        return db.query(TenderRequirement).filter(TenderRequirement.type == type).offset(skip).limit(limit).all()

    def get_by_category(self, db: Session, *, category: str, skip: int = 0, limit: int = 100) -> List[TenderRequirement]:
        """Get requirements by category"""
        return db.query(TenderRequirement).filter(TenderRequirement.category == category).offset(skip).limit(limit).all()


class CRUDTenderEvaluationCriteria(CRUDBase[TenderEvaluationCriteria, TenderEvaluationCriteriaCreate, TenderEvaluationCriteriaUpdate]):
    """CRUD operations for TenderEvaluationCriteria model"""

    def get_by_tender_item(self, db: Session, *, tender_item_id: str) -> List[TenderEvaluationCriteria]:
        """Get evaluation criteria by tender item"""
        return db.query(TenderEvaluationCriteria).filter(TenderEvaluationCriteria.tender_item_id == tender_item_id).all()

    def get_by_scoring_method(self, db: Session, *, scoring_method: str, skip: int = 0, limit: int = 100) -> List[TenderEvaluationCriteria]:
        """Get evaluation criteria by scoring method"""
        return db.query(TenderEvaluationCriteria).filter(TenderEvaluationCriteria.scoring_method == scoring_method).offset(skip).limit(limit).all()


class CRUDTenderResponse(CRUDBase[TenderResponse, TenderResponseCreate, TenderResponseUpdate]):
    """CRUD operations for TenderResponse model"""

    def get_by_tender_item(self, db: Session, *, tender_item_id: str) -> List[TenderResponse]:
        """Get responses by tender item"""
        return db.query(TenderResponse).filter(TenderResponse.tender_item_id == tender_item_id).all()

    def get_by_supplier(self, db: Session, *, supplier_id: str, skip: int = 0, limit: int = 100) -> List[TenderResponse]:
        """Get responses by supplier"""
        return db.query(TenderResponse).filter(TenderResponse.supplier_id == supplier_id).offset(skip).limit(limit).all()

    def get_by_status(self, db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[TenderResponse]:
        """Get responses by status"""
        return db.query(TenderResponse).filter(TenderResponse.status == status).offset(skip).limit(limit).all()

    def get_by_price_range(self, db: Session, *, min_price: float, max_price: float, skip: int = 0, limit: int = 100) -> List[TenderResponse]:
        """Get responses by price range"""
        return db.query(TenderResponse).filter(
            and_(
                TenderResponse.price >= min_price,
                TenderResponse.price <= max_price
            )
        ).offset(skip).limit(limit).all()


# Create CRUD instances
tender_item = CRUDTenderItem(TenderItem)
tender_requirement = CRUDTenderRequirement(TenderRequirement)
tender_evaluation_criteria = CRUDTenderEvaluationCriteria(TenderEvaluationCriteria)
tender_response = CRUDTenderResponse(TenderResponse)

# Convenience functions for TenderItem
def get_tender_item(db: Session, id: str) -> Optional[TenderItem]:
    return tender_item.get(db, id=id)


def get_tender_items(db: Session, skip: int = 0, limit: int = 100) -> List[TenderItem]:
    return tender_item.get_multi(db, skip=skip, limit=limit)


def create_tender_item(db: Session, *, obj_in: TenderItemCreate) -> TenderItem:
    return tender_item.create(db, obj_in=obj_in)


def update_tender_item(db: Session, *, db_obj: TenderItem, obj_in: TenderItemUpdate) -> TenderItem:
    return tender_item.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_tender_item(db: Session, *, id: str) -> TenderItem:
    return tender_item.remove(db, id=id)


def get_tender_items_by_contracting_process(db: Session, *, contracting_process_id: str, skip: int = 0, limit: int = 100) -> List[TenderItem]:
    return tender_item.get_by_contracting_process(db, contracting_process_id=contracting_process_id, skip=skip, limit=limit)


def get_tender_items_by_status(db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[TenderItem]:
    return tender_item.get_by_status(db, status=status, skip=skip, limit=limit)


def get_tender_items_by_tender_type(db: Session, *, tender_type: str, skip: int = 0, limit: int = 100) -> List[TenderItem]:
    return tender_item.get_by_tender_type(db, tender_type=tender_type, skip=skip, limit=limit)


def get_tender_items_by_value_range(db: Session, *, min_value: float, max_value: float, skip: int = 0, limit: int = 100) -> List[TenderItem]:
    return tender_item.get_by_value_range(db, min_value=min_value, max_value=max_value, skip=skip, limit=limit)


# Convenience functions for TenderRequirement
def get_tender_requirement(db: Session, id: str) -> Optional[TenderRequirement]:
    return tender_requirement.get(db, id=id)


def get_tender_requirements(db: Session, skip: int = 0, limit: int = 100) -> List[TenderRequirement]:
    return tender_requirement.get_multi(db, skip=skip, limit=limit)


def create_tender_requirement(db: Session, *, obj_in: TenderRequirementCreate) -> TenderRequirement:
    return tender_requirement.create(db, obj_in=obj_in)


def update_tender_requirement(db: Session, *, db_obj: TenderRequirement, obj_in: TenderRequirementUpdate) -> TenderRequirement:
    return tender_requirement.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_tender_requirement(db: Session, *, id: str) -> TenderRequirement:
    return tender_requirement.remove(db, id=id)


def get_requirements_by_tender_item(db: Session, *, tender_item_id: str) -> List[TenderRequirement]:
    return tender_requirement.get_by_tender_item(db, tender_item_id=tender_item_id)


# Convenience functions for TenderEvaluationCriteria
def get_tender_evaluation_criteria(db: Session, id: str) -> Optional[TenderEvaluationCriteria]:
    return tender_evaluation_criteria.get(db, id=id)


def get_tender_evaluation_criterias(db: Session, skip: int = 0, limit: int = 100) -> List[TenderEvaluationCriteria]:
    return tender_evaluation_criteria.get_multi(db, skip=skip, limit=limit)


def create_tender_evaluation_criteria(db: Session, *, obj_in: TenderEvaluationCriteriaCreate) -> TenderEvaluationCriteria:
    return tender_evaluation_criteria.create(db, obj_in=obj_in)


def update_tender_evaluation_criteria(db: Session, *, db_obj: TenderEvaluationCriteria, obj_in: TenderEvaluationCriteriaUpdate) -> TenderEvaluationCriteria:
    return tender_evaluation_criteria.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_tender_evaluation_criteria(db: Session, *, id: str) -> TenderEvaluationCriteria:
    return tender_evaluation_criteria.remove(db, id=id)


def get_evaluation_criterias_by_tender_item(db: Session, *, tender_item_id: str) -> List[TenderEvaluationCriteria]:
    return tender_evaluation_criteria.get_by_tender_item(db, tender_item_id=tender_item_id)


# Convenience functions for TenderResponse
def get_tender_response(db: Session, id: str) -> Optional[TenderResponse]:
    return tender_response.get(db, id=id)


def get_tender_responses(db: Session, skip: int = 0, limit: int = 100) -> List[TenderResponse]:
    return tender_response.get_multi(db, skip=skip, limit=limit)


def create_tender_response(db: Session, *, obj_in: TenderResponseCreate) -> TenderResponse:
    return tender_response.create(db, obj_in=obj_in)


def update_tender_response(db: Session, *, db_obj: TenderResponse, obj_in: TenderResponseUpdate) -> TenderResponse:
    return tender_response.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_tender_response(db: Session, *, id: str) -> TenderResponse:
    return tender_response.remove(db, id=id)


def get_responses_by_tender_item(db: Session, *, tender_item_id: str) -> List[TenderResponse]:
    return tender_response.get_by_tender_item(db, tender_item_id=tender_item_id)


def get_responses_by_supplier(db: Session, *, supplier_id: str, skip: int = 0, limit: int = 100) -> List[TenderResponse]:
    return tender_response.get_by_supplier(db, supplier_id=supplier_id, skip=skip, limit=limit) 