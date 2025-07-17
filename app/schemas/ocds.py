from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class OCDSContractBase(BaseModel):
    """Base OCDS contract schema"""
    contract_id: str
    title: str
    description: Optional[str] = None
    value_amount: Optional[float] = None
    value_currency: str = "USD"
    procurement_method: Optional[str] = None
    status: Optional[str] = None
    contract_data: Optional[Dict[str, Any]] = None


class OCDSContractCreate(OCDSContractBase):
    """Schema for creating an OCDS contract"""
    pass


class OCDSContractUpdate(BaseModel):
    """Schema for updating an OCDS contract"""
    title: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    value_currency: Optional[str] = None
    procurement_method: Optional[str] = None
    status: Optional[str] = None
    contract_data: Optional[Dict[str, Any]] = None


class OCDSContractInDB(OCDSContractBase):
    """Schema for OCDS contract in database"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class OCDSContract(OCDSContractBase):
    """Schema for OCDS contract response"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class OCDSPartyBase(BaseModel):
    """Base OCDS party schema"""
    party_id: str
    name: str
    party_type: Optional[str] = None
    contact_point: Optional[Dict[str, Any]] = None
    address: Optional[Dict[str, Any]] = None
    party_data: Optional[Dict[str, Any]] = None


class OCDSPartyCreate(OCDSPartyBase):
    """Schema for creating an OCDS party"""
    pass


class OCDSPartyUpdate(BaseModel):
    """Schema for updating an OCDS party"""
    name: Optional[str] = None
    party_type: Optional[str] = None
    contact_point: Optional[Dict[str, Any]] = None
    address: Optional[Dict[str, Any]] = None
    party_data: Optional[Dict[str, Any]] = None


class OCDSPartyInDB(OCDSPartyBase):
    """Schema for OCDS party in database"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class OCDSParty(OCDSPartyBase):
    """Schema for OCDS party response"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class OCDSTenderBase(BaseModel):
    """Base OCDS tender schema"""
    tender_id: str
    title: str
    description: Optional[str] = None
    value_amount: Optional[float] = None
    value_currency: str = "USD"
    procurement_method: Optional[str] = None
    status: Optional[str] = None
    tender_data: Optional[Dict[str, Any]] = None


class OCDSTenderCreate(OCDSTenderBase):
    """Schema for creating an OCDS tender"""
    pass


class OCDSTenderUpdate(BaseModel):
    """Schema for updating an OCDS tender"""
    title: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    value_currency: Optional[str] = None
    procurement_method: Optional[str] = None
    status: Optional[str] = None
    tender_data: Optional[Dict[str, Any]] = None


class OCDSTenderInDB(OCDSTenderBase):
    """Schema for OCDS tender in database"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class OCDSTender(OCDSTenderBase):
    """Schema for OCDS tender response"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 