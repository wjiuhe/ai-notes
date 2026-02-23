from datetime import date
from decimal import Decimal
from typing import Optional
from uuid import UUID

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models import Expense, ExpenseCategory
from app.schemas import ExpenseCreate, ExpenseUpdate, MonthlySummary, MonthlySummaryItem


def create_expense(db: Session, expense_in: ExpenseCreate, user_id: UUID) -> Expense:
    db_expense = Expense(
        user_id=user_id,
        amount=expense_in.amount,
        category=expense_in.category,
        description=expense_in.description,
        date=expense_in.date
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


def get_expense(db: Session, expense_id: UUID, user_id: UUID) -> Optional[Expense]:
    return db.query(Expense).filter(
        Expense.id == expense_id,
        Expense.user_id == user_id
    ).first()


def get_expenses(
    db: Session,
    user_id: UUID,
    skip: int = 0,
    limit: int = 100,
    category: Optional[ExpenseCategory] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
) -> tuple[list[Expense], int]:
    query = db.query(Expense).filter(Expense.user_id == user_id)

    if category:
        query = query.filter(Expense.category == category)
    if start_date:
        query = query.filter(Expense.date >= start_date)
    if end_date:
        query = query.filter(Expense.date <= end_date)

    total = query.count()
    expenses = query.order_by(Expense.date.desc()).offset(skip).limit(limit).all()

    return expenses, total


def update_expense(db: Session, db_expense: Expense, expense_in: ExpenseUpdate) -> Expense:
    update_data = expense_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_expense, field, value)

    db.commit()
    db.refresh(db_expense)
    return db_expense


def delete_expense(db: Session, db_expense: Expense) -> None:
    db.delete(db_expense)
    db.commit()


def get_monthly_summary(
    db: Session,
    user_id: UUID,
    year: int,
    month: int
) -> MonthlySummary:
    from sqlalchemy import extract

    results = db.query(
        Expense.category,
        func.sum(Expense.amount).label('total')
    ).filter(
        Expense.user_id == user_id,
        extract('year', Expense.date) == year,
        extract('month', Expense.date) == month
    ).group_by(Expense.category).all()

    categories = [
        MonthlySummaryItem(category=cat, total=Decimal(str(total)))
        for cat, total in results
    ]

    grand_total = sum(c.total for c in categories)

    return MonthlySummary(
        year=year,
        month=month,
        categories=categories,
        grand_total=grand_total
    )
