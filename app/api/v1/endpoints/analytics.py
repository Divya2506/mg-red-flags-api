from typing import Any, Dict, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.services.analytics_service import AnalyticsService

router = APIRouter()


@router.get("/red-flags/summary")
def get_red_flags_summary(
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get red flags summary statistics"""
    analytics = AnalyticsService(db)
    return analytics.get_red_flags_summary()


@router.get("/red-flags/by-severity")
def get_red_flags_by_severity(
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get red flags grouped by severity"""
    analytics = AnalyticsService(db)
    return analytics.get_red_flags_by_severity()


@router.get("/red-flags/by-category")
def get_red_flags_by_category(
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get red flags grouped by category"""
    analytics = AnalyticsService(db)
    return analytics.get_red_flags_by_category()


@router.get("/ocds/contracts/summary")
def get_ocds_contracts_summary(
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get OCDS contracts summary statistics"""
    analytics = AnalyticsService(db)
    return analytics.get_ocds_contracts_summary()


@router.get("/ocds/contracts/by-value")
def get_ocds_contracts_by_value(
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get OCDS contracts grouped by value ranges"""
    analytics = AnalyticsService(db)
    return analytics.get_ocds_contracts_by_value()


@router.get("/ocds/parties/summary")
def get_ocds_parties_summary(
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get OCDS parties summary statistics"""
    analytics = AnalyticsService(db)
    return analytics.get_ocds_parties_summary()


@router.get("/dashboard/overview")
def get_dashboard_overview(
    db: Session = Depends(get_db),
    current_user: Any = Depends(get_current_user),
) -> Any:
    """Get dashboard overview data"""
    analytics = AnalyticsService(db)
    return analytics.get_dashboard_overview() 