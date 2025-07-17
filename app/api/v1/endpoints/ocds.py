from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.crud.ocds import (
    get_ocds_contract, get_ocds_contracts, create_ocds_contract,
    get_ocds_party, get_ocds_parties, create_ocds_party,
    get_ocds_tender, get_ocds_tenders, create_ocds_tender
)
from app.schemas.ocds import (
    OCDSContract, OCDSContractCreate, OCDSParty, OCDSPartyCreate,
    OCDSTender, OCDSTenderCreate
)

router = APIRouter()


# Contract endpoints
@router.get("/contracts/", response_model=List[OCDSContract])
def read_ocds_contracts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Retrieve OCDS contracts"""
    contracts = get_ocds_contracts(db, skip=skip, limit=limit)
    return contracts


@router.post("/contracts/", response_model=OCDSContract)
def create_ocds_contract_endpoint(
    contract_in: OCDSContractCreate,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Create new OCDS contract"""
    contract = create_ocds_contract(db, obj_in=contract_in)
    return contract


@router.get("/contracts/{contract_id}", response_model=OCDSContract)
def read_ocds_contract(
    contract_id: str,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get OCDS contract by ID"""
    contract = get_ocds_contract(db, contract_id=contract_id)
    if not contract:
        raise HTTPException(
            status_code=404,
            detail="OCDS contract not found"
        )
    return contract


# Party endpoints
@router.get("/parties/", response_model=List[OCDSParty])
def read_ocds_parties(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Retrieve OCDS parties"""
    parties = get_ocds_parties(db, skip=skip, limit=limit)
    return parties


@router.post("/parties/", response_model=OCDSParty)
def create_ocds_party_endpoint(
    party_in: OCDSPartyCreate,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Create new OCDS party"""
    party = create_ocds_party(db, obj_in=party_in)
    return party


@router.get("/parties/{party_id}", response_model=OCDSParty)
def read_ocds_party(
    party_id: str,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get OCDS party by ID"""
    party = get_ocds_party(db, party_id=party_id)
    if not party:
        raise HTTPException(
            status_code=404,
            detail="OCDS party not found"
        )
    return party


# Tender endpoints
@router.get("/tenders/", response_model=List[OCDSTender])
def read_ocds_tenders(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Retrieve OCDS tenders"""
    tenders = get_ocds_tenders(db, skip=skip, limit=limit)
    return tenders


@router.post("/tenders/", response_model=OCDSTender)
def create_ocds_tender_endpoint(
    tender_in: OCDSTenderCreate,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Create new OCDS tender"""
    tender = create_ocds_tender(db, obj_in=tender_in)
    return tender


@router.get("/tenders/{tender_id}", response_model=OCDSTender)
def read_ocds_tender(
    tender_id: str,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get OCDS tender by ID"""
    tender = get_ocds_tender(db, tender_id=tender_id)
    if not tender:
        raise HTTPException(
            status_code=404,
            detail="OCDS tender not found"
        )
    return tender 