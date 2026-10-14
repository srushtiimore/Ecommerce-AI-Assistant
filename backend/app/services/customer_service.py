from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import customer_repository
from app.schemas.customer import CustomerCreate, CustomerUpdate


def create_customer(db: Session, customer_data: CustomerCreate):
    return customer_repository.create_customer(db, customer_data)


def get_customers(db: Session):
    return customer_repository.get_customers(db)


def get_customer(db: Session, customer_id: int):
    customer = customer_repository.get_customer_by_id(
        db,
        customer_id
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


def update_customer(
    db: Session,
    customer_id: int,
    customer_data: CustomerUpdate
):
    customer = customer_repository.get_customer_by_id(
        db,
        customer_id
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer_repository.update_customer(
        db,
        customer,
        customer_data
    )


def delete_customer(db: Session, customer_id: int):
    customer = customer_repository.get_customer_by_id(
        db,
        customer_id
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    customer_repository.delete_customer(db, customer)

    return {"message": "Customer deleted successfully"}