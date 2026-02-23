import pytest
from decimal import Decimal
from datetime import date


def test_expense_category_enum():
    from app.schemas import ExpenseCategory
    assert ExpenseCategory.FOOD == "Food"


def test_expense_create_valid():
    from app.schemas import ExpenseCreate, ExpenseCategory

    data = ExpenseCreate(
        amount=Decimal("25.50"),
        category=ExpenseCategory.FOOD,
        description="Lunch",
        date=date.today()
    )
    assert data.amount == Decimal("25.50")
    assert data.category == ExpenseCategory.FOOD


def test_expense_create_invalid_amount():
    from app.schemas import ExpenseCreate, ExpenseCategory
    from pydantic import ValidationError

    with pytest.raises(ValidationError) as exc_info:
        ExpenseCreate(
            amount=Decimal("-10.00"),
            category=ExpenseCategory.FOOD,
            date=date.today()
        )
    assert "greater than 0" in str(exc_info.value)


def test_expense_create_description_too_long():
    from app.schemas import ExpenseCreate, ExpenseCategory
    from pydantic import ValidationError

    with pytest.raises(ValidationError) as exc_info:
        ExpenseCreate(
            amount=Decimal("10.00"),
            category=ExpenseCategory.FOOD,
            description="x" * 256,
            date=date.today()
        )
    assert "at most 255 characters" in str(exc_info.value)
