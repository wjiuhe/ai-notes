import pytest
from fastapi import HTTPException


def test_get_current_user_valid_key(db_session):
    from app.auth import get_current_user
    from app.models import User

    user = User(api_key="valid_api_key_123")
    db_session.add(user)
    db_session.commit()

    result = get_current_user("valid_api_key_123", db_session)
    assert result.id == user.id
    assert result.api_key == "valid_api_key_123"


def test_get_current_user_invalid_key(db_session):
    from app.auth import get_current_user

    with pytest.raises(HTTPException) as exc_info:
        get_current_user("invalid_key", db_session)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid API key"
