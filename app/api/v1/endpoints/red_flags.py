from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.crud.red_flag import (
    get_red_flag, get_red_flags, create_red_flag, 
    update_red_flag, delete_red_flag, get_red_flag_rules
)
from app.schemas.red_flag import RedFlag, RedFlagCreate, RedFlagUpdate, RedFlagRule
from app.services.red_flag_engine import RedFlagEngine

router = APIRouter()


# Retrieve a paginated list of all red flags in the system
@router.get("/", response_model=List[RedFlag])
def read_red_flags(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Retrieve red flags"""
    red_flags = get_red_flags(db, skip=skip, limit=limit)
    return red_flags


# Create a new red flag entry in the system
@router.post("/", response_model=RedFlag)
def create_red_flag_endpoint(
    red_flag_in: RedFlagCreate,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Create new red flag"""
    red_flag = create_red_flag(db, obj_in=red_flag_in)
    return red_flag


# Retrieve a specific red flag by its unique ID
@router.get("/{red_flag_id}", response_model=RedFlag)
def read_red_flag(
    red_flag_id: int,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get red flag by ID"""
    red_flag = get_red_flag(db, id=red_flag_id)
    if not red_flag:
        raise HTTPException(
            status_code=404,
            detail="Red flag not found"
        )
    return red_flag


# Update an existing red flag by its unique ID
@router.put("/{red_flag_id}", response_model=RedFlag)
def update_red_flag_endpoint(
    red_flag_id: int,
    red_flag_in: RedFlagUpdate,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Update red flag"""
    red_flag = get_red_flag(db, id=red_flag_id)
    if not red_flag:
        raise HTTPException(
            status_code=404,
            detail="Red flag not found"
        )
    red_flag = update_red_flag(db, db_obj=red_flag, obj_in=red_flag_in)
    return red_flag


# Delete a red flag from the system by its unique ID
@router.delete("/{red_flag_id}")
def delete_red_flag_endpoint(
    red_flag_id: int,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Delete red flag"""
    red_flag = get_red_flag(db, id=red_flag_id)
    if not red_flag:
        raise HTTPException(
            status_code=404,
            detail="Red flag not found"
        )
    delete_red_flag(db, id=red_flag_id)
    return {"message": "Red flag deleted successfully"}


# Retrieve all red flag rules currently defined in the system
@router.get("/rules/", response_model=List[RedFlagRule])
def read_red_flag_rules(
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get all red flag rules"""
    rules = get_red_flag_rules(db)
    return rules


# Detect red flags in the provided data using the rule engine
@router.post("/detect/")
def detect_red_flags(
    data: dict,
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Detect red flags in given data"""
    engine = RedFlagEngine(db)
    results = engine.detect_red_flags(data)
    return {"red_flags": results} 