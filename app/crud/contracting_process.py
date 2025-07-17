from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.crud.base import CRUDBase
from app.models.contracting_process import ContractingProcess
from app.schemas.contracting_process import ContractingProcessCreate, ContractingProcessUpdate


class CRUDContractingProcess(CRUDBase[ContractingProcess, ContractingProcessCreate, ContractingProcessUpdate]):
    """CRUD operations for ContractingProcess model"""

    def get_by_buyer(self, db: Session, *, buyer_id: str, skip: int = 0, limit: int = 100) -> List[ContractingProcess]:
        """Get contracting processes by buyer"""
        return db.query(ContractingProcess).filter(ContractingProcess.buyer_id == buyer_id).offset(skip).limit(limit).all()

    def get_by_status(self, db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[ContractingProcess]:
        """Get contracting processes by status"""
        return db.query(ContractingProcess).filter(ContractingProcess.status == status).offset(skip).limit(limit).all()

    def get_by_procurement_method(self, db: Session, *, procurement_method: str, skip: int = 0, limit: int = 100) -> List[ContractingProcess]:
        """Get contracting processes by procurement method"""
        return db.query(ContractingProcess).filter(ContractingProcess.procurement_method == procurement_method).offset(skip).limit(limit).all()

    def get_by_value_range(self, db: Session, *, min_value: float, max_value: float, skip: int = 0, limit: int = 100) -> List[ContractingProcess]:
        """Get contracting processes by value range"""
        return db.query(ContractingProcess).filter(
            and_(
                ContractingProcess.value_amount >= min_value,
                ContractingProcess.value_amount <= max_value
            )
        ).offset(skip).limit(limit).all()

    def get_by_date_range(self, db: Session, *, start_date: str, end_date: str, skip: int = 0, limit: int = 100) -> List[ContractingProcess]:
        """Get contracting processes by date range"""
        return db.query(ContractingProcess).filter(
            and_(
                ContractingProcess.date_published >= start_date,
                ContractingProcess.date_published <= end_date
            )
        ).offset(skip).limit(limit).all()


# Create CRUD instance
contracting_process = CRUDContractingProcess(ContractingProcess)

# Convenience functions
def get_contracting_process(db: Session, id: str) -> Optional[ContractingProcess]:
    return contracting_process.get(db, id=id)


def get_contracting_processes(db: Session, skip: int = 0, limit: int = 100) -> List[ContractingProcess]:
    return contracting_process.get_multi(db, skip=skip, limit=limit)


def create_contracting_process(db: Session, *, obj_in: ContractingProcessCreate) -> ContractingProcess:
    return contracting_process.create(db, obj_in=obj_in)


def update_contracting_process(db: Session, *, db_obj: ContractingProcess, obj_in: ContractingProcessUpdate) -> ContractingProcess:
    return contracting_process.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_contracting_process(db: Session, *, id: str) -> ContractingProcess:
    return contracting_process.remove(db, id=id)


def get_contracting_processes_by_buyer(db: Session, *, buyer_id: str, skip: int = 0, limit: int = 100) -> List[ContractingProcess]:
    return contracting_process.get_by_buyer(db, buyer_id=buyer_id, skip=skip, limit=limit)


def get_contracting_processes_by_status(db: Session, *, status: str, skip: int = 0, limit: int = 100) -> List[ContractingProcess]:
    return contracting_process.get_by_status(db, status=status, skip=skip, limit=limit)


def get_contracting_processes_by_procurement_method(db: Session, *, procurement_method: str, skip: int = 0, limit: int = 100) -> List[ContractingProcess]:
    return contracting_process.get_by_procurement_method(db, procurement_method=procurement_method, skip=skip, limit=limit)


def get_contracting_processes_by_value_range(db: Session, *, min_value: float, max_value: float, skip: int = 0, limit: int = 100) -> List[ContractingProcess]:
    return contracting_process.get_by_value_range(db, min_value=min_value, max_value=max_value, skip=skip, limit=limit)


def get_contracting_processes_by_date_range(db: Session, *, start_date: str, end_date: str, skip: int = 0, limit: int = 100) -> List[ContractingProcess]:
    return contracting_process.get_by_date_range(db, start_date=start_date, end_date=end_date, skip=skip, limit=limit) 