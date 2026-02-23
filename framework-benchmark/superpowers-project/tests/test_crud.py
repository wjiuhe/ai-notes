import pytest
from decimal import Decimal
from datetime import date, timedelta
from uuid import uuid4

from app.models import User, Expense, ExpenseCategory


def test_create_expense(db_session):
    from app.crud import create_expense
    from app.schemas import ExpenseCreate

    user = User(api_key="test_crud_key")
    db_session.add(user)
    db_session.commit()

    expense_in = ExpenseCreate(
        amount=Decimal("50.00"),
        category=ExpenseCategory.TRANSPORT,
        description="Bus ticket",
        date=date.today()
    )

    expense = create_expense(db_session, expense_in, user.id)

    assert expense.amount == Decimal("50.00")
    assert expense.category == ExpenseCategory.TRANSPORT
    assert expense.user_id == user.id


def test_get_expense(db_session):
    from app.crud import get_expense, create_expense
    from app.schemas import ExpenseCreate

    user = User(api_key="test_crud_key2")
    db_session.add(user)
    db_session.commit()

    expense_in = ExpenseCreate(
        amount=Decimal("25.00"),
        category=ExpenseCategory.FOOD,
        date=date.today()
    )
    created = create_expense(db_session, expense_in, user.id)

    fetched = get_expense(db_session, created.id, user.id)
    assert fetched is not None
    assert fetched.id == created.id


def test_get_expense_wrong_user(db_session):
    from app.crud import get_expense, create_expense
    from app.schemas import ExpenseCreate

    user1 = User(api_key="user1_key")
    user2 = User(api_key="user2_key")
    db_session.add_all([user1, user2])
    db_session.commit()

    expense_in = ExpenseCreate(
        amount=Decimal("25.00"),
        category=ExpenseCategory.FOOD,
        date=date.today()
    )
    created = create_expense(db_session, expense_in, user1.id)

    fetched = get_expense(db_session, created.id, user2.id)
    assert fetched is None


def test_get_expenses_pagination(db_session):
    from app.crud import get_expenses

    user = User(api_key="test_pagination")
    db_session.add(user)
    db_session.commit()

    # Create 5 expenses
    for i in range(5):
        expense = Expense(
            user_id=user.id,
            amount=Decimal("10.00"),
            category=ExpenseCategory.FOOD,
            date=date.today()
        )
        db_session.add(expense)
    db_session.commit()

    expenses, total = get_expenses(db_session, user.id, skip=0, limit=3)
    assert len(expenses) == 3
    assert total == 5


def test_update_expense(db_session):
    from app.crud import update_expense, create_expense
    from app.schemas import ExpenseCreate, ExpenseUpdate

    user = User(api_key="test_update")
    db_session.add(user)
    db_session.commit()

    expense_in = ExpenseCreate(
        amount=Decimal("25.00"),
        category=ExpenseCategory.FOOD,
        date=date.today()
    )
    created = create_expense(db_session, expense_in, user.id)

    update_data = ExpenseUpdate(amount=Decimal("30.00"))
    updated = update_expense(db_session, created, update_data)

    assert updated.amount == Decimal("30.00")


def test_delete_expense(db_session):
    from app.crud import delete_expense, create_expense, get_expense
    from app.schemas import ExpenseCreate

    user = User(api_key="test_delete")
    db_session.add(user)
    db_session.commit()

    expense_in = ExpenseCreate(
        amount=Decimal("25.00"),
        category=ExpenseCategory.FOOD,
        date=date.today()
    )
    created = create_expense(db_session, expense_in, user.id)

    delete_expense(db_session, created)

    fetched = get_expense(db_session, created.id, user.id)
    assert fetched is None


def test_get_expenses_with_filters(db_session):
    from app.crud import get_expenses

    user = User(api_key="test_filters")
    db_session.add(user)
    db_session.commit()

    # Create expenses with different categories
    expense1 = Expense(
        user_id=user.id,
        amount=Decimal("10.00"),
        category=ExpenseCategory.FOOD,
        date=date.today()
    )
    expense2 = Expense(
        user_id=user.id,
        amount=Decimal("20.00"),
        category=ExpenseCategory.TRANSPORT,
        date=date.today()
    )
    db_session.add_all([expense1, expense2])
    db_session.commit()

    expenses, total = get_expenses(
        db_session, user.id,
        category=ExpenseCategory.FOOD
    )
    assert len(expenses) == 1
    assert expenses[0].category == ExpenseCategory.FOOD


def test_get_monthly_summary(db_session):
    from app.crud import get_monthly_summary

    user = User(api_key="test_summary")
    db_session.add(user)
    db_session.commit()

    today = date.today()

    # Create expenses for this month
    expense1 = Expense(
        user_id=user.id,
        amount=Decimal("50.00"),
        category=ExpenseCategory.FOOD,
        date=today
    )
    expense2 = Expense(
        user_id=user.id,
        amount=Decimal("30.00"),
        category=ExpenseCategory.FOOD,
        date=today
    )
    expense3 = Expense(
        user_id=user.id,
        amount=Decimal("20.00"),
        category=ExpenseCategory.TRANSPORT,
        date=today
    )
    db_session.add_all([expense1, expense2, expense3])
    db_session.commit()

    summary = get_monthly_summary(db_session, user.id, today.year, today.month)

    assert summary.year == today.year
    assert summary.month == today.month
    assert len(summary.categories) == 2

    food_total = next(c for c in summary.categories if c.category == ExpenseCategory.FOOD)
    assert food_total.total == Decimal("80.00")

    assert summary.grand_total == Decimal("100.00")
