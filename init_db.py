#!/usr/bin/env python3
"""
Database initialization script
"""

import asyncio
from sqlalchemy.orm import Session

from app.core.database import SessionLocal, init_db
from app.crud.user import create_user
from app.schemas.user import UserCreate
from app.crud.red_flag import create_red_flag_rule
from app.schemas.red_flag import RedFlagRuleCreate
import json


def create_initial_data():
    """Create initial data for the application"""
    db = SessionLocal()
    
    try:
        # Create admin user
        admin_user = UserCreate(
            email="admin@mygets.com",
            username="admin",
            password="admin123",
            is_active=True,
            is_superuser=True
        )
        
        try:
            create_user(db, obj_in=admin_user)
            print("✅ Admin user created successfully")
        except Exception as e:
            print(f"⚠️  Admin user already exists or error: {e}")
        
        # Create sample red flag rules
        sample_rules = [
            {
                "name": "High Value Contract",
                "description": "Detect contracts with unusually high values",
                "rule_type": "threshold",
                "parameters": json.dumps({
                    "field": "value_amount",
                    "threshold": 1000000,
                    "operator": ">",
                    "category": "financial",
                    "severity": "high",
                    "base_confidence": 0.8
                })
            },
            {
                "name": "Suspicious Company Name",
                "description": "Detect suspicious patterns in company names",
                "rule_type": "pattern",
                "parameters": json.dumps({
                    "field": "title",
                    "pattern": "suspicious",
                    "category": "compliance",
                    "severity": "medium",
                    "base_confidence": 0.6
                })
            },
            {
                "name": "Anomalous Contract Value",
                "description": "Detect contracts with values outside normal range",
                "rule_type": "anomaly",
                "parameters": json.dumps({
                    "field": "value_amount",
                    "min_value": 1000,
                    "max_value": 10000000,
                    "category": "financial",
                    "severity": "medium",
                    "base_confidence": 0.7
                })
            }
        ]
        
        for rule_data in sample_rules:
            try:
                rule = RedFlagRuleCreate(**rule_data)
                create_red_flag_rule(db, obj_in=rule)
                print(f"✅ Red flag rule '{rule_data['name']}' created successfully")
            except Exception as e:
                print(f"⚠️  Rule '{rule_data['name']}' already exists or error: {e}")
        
        print("\n🎉 Database initialization completed!")
        print("📝 Default admin credentials:")
        print("   Email: admin@mygets.com")
        print("   Password: admin123")
        print("\n⚠️  Remember to change these credentials in production!")
        
    finally:
        db.close()


async def main():
    """Main initialization function"""
    print("🚀 Initializing MyGets Red Flags API database...")
    
    # Initialize database tables
    await init_db()
    print("✅ Database tables created successfully")
    
    # Create initial data
    create_initial_data()


if __name__ == "__main__":
    asyncio.run(main()) 