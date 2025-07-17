from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, red_flags, ocds, analytics

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(red_flags.router, prefix="/red-flags", tags=["red-flags"])
api_router.include_router(ocds.router, prefix="/ocds", tags=["ocds"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"]) 