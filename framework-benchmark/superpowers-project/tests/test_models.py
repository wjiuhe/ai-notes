import pytest
from decimal import Decimal
from datetime import date

from app.models import User, Expense, ExpenseCategory


def test_expense_category_values():
    assert ExpenseCategory.FOOD.value == "Food"
    assert ExpenseCategory.TRANSPORT.value == "Transport"
    assert ExpenseCategory.ENTERTAINMENT.value == "Entertainment"
    assert ExpenseCategory.UTILITIES.value == "Utilities"
    assert ExpenseCategory.HEALTHCARE.value == "Healthcare"
    assert ExpenseCategory.SHOPPING.value == "Shopping"
    assert ExpenseCategory.OTHER.value == "Other"


def test_user_creation(db_session):
    from app.models import User
    user = User(api_key="test_key_123")
    db_session.add(user)
    db_session.commit()

    assert user.id is not None
    assert user.api_key == "test_key_123"
    assert user.created_at is not None


def test_expense_creation(db_session):
    from app.models import User, Expense, ExpenseCategory
    from datetime import date
    from decimal import Decimal

    user = User(api_key="test_key_456")
    db_session.add(user)
    db_session.commit()

    expense = Expense(
        user_id=user.id,
        amount=Decimal("25.50"),
        category=ExpenseCategory.FOOD,
        description="Lunch",
        date=date.today()
    )
    db_session.add(expense)
    db_session.commit()

    assert expense.id is not None
    assert expense.user_id == user.id
    assert expense.amount == Decimal("25.50")
