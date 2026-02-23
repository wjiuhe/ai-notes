from datetime import date
from typing import Optional
from uuid import UUID

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db, Base, engine
from app.models import User
from app.auth import get_current_user
from app import crud, schemas

app = FastAPI(title="Personal Expense Tracker API", version="1.0.0")


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)


@app.post("/api/v1/expenses", response_model=schemas.ExpenseOut, status_code=201)
def create_expense(
    expense_in: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_expense(db, expense_in, current_user.id)


@app.get("/api/v1/expenses", response_model=schemas.PaginatedExpenses)
def list_expenses(
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    category: Optional[schemas.ExpenseCategory] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    skip = (page - 1) * per_page
    expenses, total = crud.get_expenses(
        db, current_user.id, skip=skip, limit=per_page,
        category=category, start_date=start_date, end_date=end_date
    )

    total_pages = (total + per_page - 1) // per_page

    return schemas.PaginatedExpenses(
        data=[schemas.ExpenseOut.model_validate(e) for e in expenses],
        meta=schemas.PaginationMeta(
            page=page,
            per_page=per_page,
            total=total,
            total_pages=total_pages
        )
    )


@app.get("/api/v1/expenses/{expense_id}", response_model=schemas.ExpenseOut)
def get_expense(
    expense_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    expense = crud.get_expense(db, expense_id, current_user.id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


@app.put("/api/v1/expenses/{expense_id}", response_model=schemas.ExpenseOut)
def update_expense(
    expense_id: UUID,
    expense_in: schemas.ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    expense = crud.get_expense(db, expense_id, current_user.id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return crud.update_expense(db, expense, expense_in)


@app.delete("/api/v1/expenses/{expense_id}", status_code=204)
def delete_expense(
    expense_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    expense = crud.get_expense(db, expense_id, current_user.id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    crud.delete_expense(db, expense)
    return None


@app.get("/api/v1/summary/monthly", response_model=schemas.MonthlySummary)
def monthly_summary(
    year: int = Query(..., ge=2000, le=2100),
    month: int = Query(..., ge=1, le=12),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.get_monthly_summary(db, current_user.id, year, month)
