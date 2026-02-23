import pytest
from decimal import Decimal
from datetime import date

from fastapi.testclient import TestClient


@pytest.fixture
def test_user(db_session):
    from app.models import User
    user = User(api_key="test_api_key_12345")
    db_session.add(user)
    db_session.commit()
    return user


@pytest.fixture
def client(db_session, test_user):
    from app.main import app
    from app.database import get_db

    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


def test_create_expense_endpoint(client, test_user):
    response = client.post(
        "/api/v1/expenses",
        headers={"X-API-Key": test_user.api_key},
        json={
            "amount": "25.50",
            "category": "Food",
            "description": "Lunch",
            "date": date.today().isoformat()
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["amount"] == "25.50"
    assert data["category"] == "Food"
    assert data["description"] == "Lunch"


def test_create_expense_invalid_amount(client, test_user):
    response = client.post(
        "/api/v1/expenses",
        headers={"X-API-Key": test_user.api_key},
        json={
            "amount": "-10.00",
            "category": "Food",
            "date": date.today().isoformat()
        }
    )
    assert response.status_code == 422


def test_create_expense_invalid_api_key(client):
    response = client.post(
        "/api/v1/expenses",
        headers={"X-API-Key": "invalid_key"},
        json={
            "amount": "25.50",
            "category": "Food",
            "date": date.today().isoformat()
        }
    )
    assert response.status_code == 401


def test_list_expenses_endpoint(client, test_user, db_session):
    from app.models import Expense, ExpenseCategory

    # Create test expenses
    for i in range(3):
        expense = Expense(
            user_id=test_user.id,
            amount=Decimal("10.00"),
            category=ExpenseCategory.FOOD,
            date=date.today()
        )
        db_session.add(expense)
    db_session.commit()

    response = client.get(
        "/api/v1/expenses",
        headers={"X-API-Key": test_user.api_key}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 3
    assert data["meta"]["total"] == 3


def test_list_expenses_with_pagination(client, test_user, db_session):
    from app.models import Expense, ExpenseCategory

    for i in range(5):
        expense = Expense(
            user_id=test_user.id,
            amount=Decimal("10.00"),
            category=ExpenseCategory.FOOD,
            date=date.today()
        )
        db_session.add(expense)
    db_session.commit()

    response = client.get(
        "/api/v1/expenses?page=1&per_page=3",
        headers={"X-API-Key": test_user.api_key}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 3
    assert data["meta"]["total_pages"] == 2


def test_list_expenses_filtered_by_category(client, test_user, db_session):
    from app.models import Expense, ExpenseCategory

    expense1 = Expense(
        user_id=test_user.id,
        amount=Decimal("10.00"),
        category=ExpenseCategory.FOOD,
        date=date.today()
    )
    expense2 = Expense(
        user_id=test_user.id,
        amount=Decimal("20.00"),
        category=ExpenseCategory.TRANSPORT,
        date=date.today()
    )
    db_session.add_all([expense1, expense2])
    db_session.commit()

    response = client.get(
        "/api/v1/expenses?category=Food",
        headers={"X-API-Key": test_user.api_key}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 1
    assert data["data"][0]["category"] == "Food"


def test_get_expense_endpoint(client, test_user, db_session):
    from app.models import Expense, ExpenseCategory

    expense = Expense(
        user_id=test_user.id,
        amount=Decimal("25.00"),
        category=ExpenseCategory.FOOD,
        date=date.today()
    )
    db_session.add(expense)
    db_session.commit()

    response = client.get(
        f"/api/v1/expenses/{expense.id}",
        headers={"X-API-Key": test_user.api_key}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == "25.00"


def test_get_expense_not_found(client, test_user):
    from uuid import uuid4
    response = client.get(
        f"/api/v1/expenses/{uuid4()}",
        headers={"X-API-Key": test_user.api_key}
    )
    assert response.status_code == 404


def test_update_expense_endpoint(client, test_user, db_session):
    from app.models import Expense, ExpenseCategory

    expense = Expense(
        user_id=test_user.id,
        amount=Decimal("25.00"),
        category=ExpenseCategory.FOOD,
        date=date.today()
    )
    db_session.add(expense)
    db_session.commit()

    response = client.put(
        f"/api/v1/expenses/{expense.id}",
        headers={"X-API-Key": test_user.api_key},
        json={"amount": "30.00"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == "30.00"


def test_delete_expense_endpoint(client, test_user, db_session):
    from app.models import Expense, ExpenseCategory

    expense = Expense(
        user_id=test_user.id,
        amount=Decimal("25.00"),
        category=ExpenseCategory.FOOD,
        date=date.today()
    )
    db_session.add(expense)
    db_session.commit()

    response = client.delete(
        f"/api/v1/expenses/{expense.id}",
        headers={"X-API-Key": test_user.api_key}
    )
    assert response.status_code == 204

    # Verify deletion
    response = client.get(
        f"/api/v1/expenses/{expense.id}",
        headers={"X-API-Key": test_user.api_key}
    )
    assert response.status_code == 404


def test_monthly_summary_endpoint(client, test_user, db_session):
    from app.models import Expense, ExpenseCategory

    today = date.today()
    expense1 = Expense(
        user_id=test_user.id,
        amount=Decimal("50.00"),
        category=ExpenseCategory.FOOD,
        date=today
    )
    expense2 = Expense(
        user_id=test_user.id,
        amount=Decimal("30.00"),
        category=ExpenseCategory.FOOD,
        date=today
    )
    db_session.add_all([expense1, expense2])
    db_session.commit()

    response = client.get(
        f"/api/v1/summary/monthly?year={today.year}&month={today.month}",
        headers={"X-API-Key": test_user.api_key}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["year"] == today.year
    assert data["month"] == today.month
    assert data["grand_total"] == "80.00"
    assert len(data["categories"]) == 1
    assert data["categories"][0]["total"] == "80.00"
