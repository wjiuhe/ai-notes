from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ExpenseCategory(str, Enum):
    FOOD = "Food"
    TRANSPORT = "Transport"
    ENTERTAINMENT = "Entertainment"
    UTILITIES = "Utilities"
    HEALTHCARE = "Healthcare"
    SHOPPING = "Shopping"
    OTHER = "Other"


class ExpenseBase(BaseModel):
    amount: Decimal = Field(..., gt=0, description="Amount must be greater than 0")
    category: ExpenseCategory
    description: Optional[str] = Field(None, max_length=255)
    date: date

    @field_validator('amount')
    @classmethod
    def validate_amount_positive(cls, v: Decimal) -> Decimal:
        if v <= 0:
            raise ValueError("Amount must be greater than 0")
        return v

    @field_validator('description')
    @classmethod
    def validate_description_length(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and len(v) > 255:
            raise ValueError("Description must be 255 characters or less")
        return v


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    amount: Optional[Decimal] = Field(None, gt=0)
    category: Optional[ExpenseCategory] = None
    description: Optional[str] = Field(None, max_length=255)
    date: Optional[date] = None

    @field_validator('amount')
    @classmethod
    def validate_amount_positive(cls, v: Optional[Decimal]) -> Optional[Decimal]:
        if v is not None and v <= 0:
            raise ValueError("Amount must be greater than 0")
        return v

    @field_validator('description')
    @classmethod
    def validate_description_length(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and len(v) > 255:
            raise ValueError("Description must be 255 characters or less")
        return v


class ExpenseOut(ExpenseBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime


class PaginationMeta(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int


class PaginatedExpenses(BaseModel):
    data: list[ExpenseOut]
    meta: PaginationMeta


class MonthlySummaryItem(BaseModel):
    category: ExpenseCategory
    total: Decimal


class MonthlySummary(BaseModel):
    year: int
    month: int
    categories: list[MonthlySummaryItem]
    grand_total: Decimal
