from typing import List, Optional
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.ocds import OCDSContract, OCDSParty, OCDSTender
from app.schemas.ocds import (
    OCDSContractCreate, OCDSContractUpdate,
    OCDSPartyCreate, OCDSPartyUpdate,
    OCDSTenderCreate, OCDSTenderUpdate
)


class CRUDOCDSContract(CRUDBase[OCDSContract, OCDSContractCreate, OCDSContractUpdate]):
    """CRUD operations for OCDSContract model"""

    def get_by_contract_id(self, db: Session, *, contract_id: str) -> Optional[OCDSContract]:
        """Get contract by contract_id"""
        return db.query(OCDSContract).filter(OCDSContract.contract_id == contract_id).first()

    def get_by_status(self, db: Session, *, status: str) -> List[OCDSContract]:
        """Get contracts by status"""
        return db.query(OCDSContract).filter(OCDSContract.status == status).all()

    def get_by_procurement_method(self, db: Session, *, method: str) -> List[OCDSContract]:
        """Get contracts by procurement method"""
        return db.query(OCDSContract).filter(OCDSContract.procurement_method == method).all()


class CRUDOCDSParty(CRUDBase[OCDSParty, OCDSPartyCreate, OCDSPartyUpdate]):
    """CRUD operations for OCDSParty model"""

    def get_by_party_id(self, db: Session, *, party_id: str) -> Optional[OCDSParty]:
        """Get party by party_id"""
        return db.query(OCDSParty).filter(OCDSParty.party_id == party_id).first()

    def get_by_type(self, db: Session, *, party_type: str) -> List[OCDSParty]:
        """Get parties by type"""
        return db.query(OCDSParty).filter(OCDSParty.party_type == party_type).all()


class CRUDOCDSTender(CRUDBase[OCDSTender, OCDSTenderCreate, OCDSTenderUpdate]):
    """CRUD operations for OCDSTender model"""

    def get_by_tender_id(self, db: Session, *, tender_id: str) -> Optional[OCDSTender]:
        """Get tender by tender_id"""
        return db.query(OCDSTender).filter(OCDSTender.tender_id == tender_id).first()

    def get_by_status(self, db: Session, *, status: str) -> List[OCDSTender]:
        """Get tenders by status"""
        return db.query(OCDSTender).filter(OCDSTender.status == status).all()

    def get_by_procurement_method(self, db: Session, *, method: str) -> List[OCDSTender]:
        """Get tenders by procurement method"""
        return db.query(OCDSTender).filter(OCDSTender.procurement_method == method).all()


# Create CRUD instances
ocds_contract = CRUDOCDSContract(OCDSContract)
ocds_party = CRUDOCDSParty(OCDSParty)
ocds_tender = CRUDOCDSTender(OCDSTender)

# Convenience functions for OCDSContract
def get_ocds_contract(db: Session, id: int) -> Optional[OCDSContract]:
    return ocds_contract.get(db, id=id)


def get_ocds_contract_by_contract_id(db: Session, *, contract_id: str) -> Optional[OCDSContract]:
    return ocds_contract.get_by_contract_id(db, contract_id=contract_id)


def get_ocds_contracts(db: Session, skip: int = 0, limit: int = 100):
    return ocds_contract.get_multi(db, skip=skip, limit=limit)


def create_ocds_contract(db: Session, *, obj_in: OCDSContractCreate) -> OCDSContract:
    return ocds_contract.create(db, obj_in=obj_in)


def update_ocds_contract(db: Session, *, db_obj: OCDSContract, obj_in: OCDSContractUpdate) -> OCDSContract:
    return ocds_contract.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_ocds_contract(db: Session, *, id: int) -> OCDSContract:
    return ocds_contract.remove(db, id=id)


# Convenience functions for OCDSParty
def get_ocds_party(db: Session, id: int) -> Optional[OCDSParty]:
    return ocds_party.get(db, id=id)


def get_ocds_party_by_party_id(db: Session, *, party_id: str) -> Optional[OCDSParty]:
    return ocds_party.get_by_party_id(db, party_id=party_id)


def get_ocds_parties(db: Session, skip: int = 0, limit: int = 100):
    return ocds_party.get_multi(db, skip=skip, limit=limit)


def create_ocds_party(db: Session, *, obj_in: OCDSPartyCreate) -> OCDSParty:
    return ocds_party.create(db, obj_in=obj_in)


def update_ocds_party(db: Session, *, db_obj: OCDSParty, obj_in: OCDSPartyUpdate) -> OCDSParty:
    return ocds_party.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_ocds_party(db: Session, *, id: int) -> OCDSParty:
    return ocds_party.remove(db, id=id)


# Convenience functions for OCDSTender
def get_ocds_tender(db: Session, id: int) -> Optional[OCDSTender]:
    return ocds_tender.get(db, id=id)


def get_ocds_tender_by_tender_id(db: Session, *, tender_id: str) -> Optional[OCDSTender]:
    return ocds_tender.get_by_tender_id(db, tender_id=tender_id)


def get_ocds_tenders(db: Session, skip: int = 0, limit: int = 100):
    return ocds_tender.get_multi(db, skip=skip, limit=limit)


def create_ocds_tender(db: Session, *, obj_in: OCDSTenderCreate) -> OCDSTender:
    return ocds_tender.create(db, obj_in=obj_in)


def update_ocds_tender(db: Session, *, db_obj: OCDSTender, obj_in: OCDSTenderUpdate) -> OCDSTender:
    return ocds_tender.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_ocds_tender(db: Session, *, id: int) -> OCDSTender:
    return ocds_tender.remove(db, id=id) 