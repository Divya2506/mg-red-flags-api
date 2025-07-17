from typing import Optional
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    """CRUD operations for User model"""

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        """Create new user with hashed password"""
        db_obj = User(
            email=obj_in.email,
            username=obj_in.username,
            hashed_password=get_password_hash(obj_in.password),
            is_active=obj_in.is_active,
            is_superuser=obj_in.is_superuser,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: UserUpdate
    ) -> User:
        """Update user with password hashing if needed"""
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        if update_data.get("password"):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        """Authenticate user"""
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        """Check if user is active"""
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        """Check if user is superuser"""
        return user.is_superuser


# Create CRUD instance
user = CRUDUser(User)

# Convenience functions
def get_user(db: Session, id: int) -> Optional[User]:
    return user.get(db, id=id)


def get_user_by_email(db: Session, *, email: str) -> Optional[User]:
    return user.get_by_email(db, email=email)


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return user.get_multi(db, skip=skip, limit=limit)


def create_user(db: Session, *, obj_in: UserCreate) -> User:
    return user.create(db, obj_in=obj_in)


def update_user(db: Session, *, db_obj: User, obj_in: UserUpdate) -> User:
    return user.update(db, db_obj=db_obj, obj_in=obj_in)


def delete_user(db: Session, *, id: int) -> User:
    return user.remove(db, id=id)


def authenticate_user(db: Session, *, email: str, password: str) -> Optional[User]:
    return user.authenticate(db, email=email, password=password) 