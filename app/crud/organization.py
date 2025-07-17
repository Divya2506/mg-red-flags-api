from typing import Optional, List
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationUpdate


class CRUDOrganization(CRUDBase[Organization, OrganizationCreate, OrganizationUpdate]):
    """CRUD operations for Organization model"""

    def get_by_identifier(self, db: Session, *, identifier: str) -> Optional[Organization]:
        """Get organization by identifier"""
        return db.query(Organization).filter(Organization.identifier == identifier).first()

    def get_by_name(self, db: Session, *, name: str) -> Optional[Organization]:
        """Get organization by name"""
        return db.query(Organization).filter(Organization.name == name).first()

    def get_organizations_by_type(self, db: Session, *, organization_type: str, skip: int = 0, limit: int = 100) -> List[Organization]:
        """Get organizations by type (buyer, supplier, etc.)"""
        return db.query(Organization).filter(Organization.contact_point.contains({"type": organization_type})).offset(skip).limit(limit).all()


# Create CRUD instance
organization = CRUDOrganization(Organization)

# Convenience functions
def get_organization(db: Session, id: str) -> Optional[Organization]:
    return organization.get(db, id=id)


def get_organization_by_identifier(db: Session, *, identifier: str) -> Optional[Organization]:
    return organization.get_by_identifier(db, identifier=identifier)


def get_organization_by_name(db: Session, *, name: str) -> Optional[Organization]:
    return organization.get_by_name(db, name=name)


def get_organizations(db: Session, skip: int = 0, limit: int = 100) -> List[Organization]:
    return organization.get_multi(db, skip=skip, limit=limit)


def create_organization(db: Session, *, obj_in: OrganizationCreate) -> Organization:
    return organization.create(db, obj_in=obj_in)


def update_organization(db: Session, *, db_obj: Organization, obj_in: OrganizationUpdate) -> Organization:
    return organization.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_organization(db: Session, *, id: str) -> Organization:
    return organization.remove(db, id=id)


def get_organizations_by_type(db: Session, *, organization_type: str, skip: int = 0, limit: int = 100) -> List[Organization]:
    return organization.get_organizations_by_type(db, organization_type=organization_type, skip=skip, limit=limit) 