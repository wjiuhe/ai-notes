import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.config import settings

# Import models to register them with Base.metadata
from app import models  # noqa: F401


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(settings.test_database_url)
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)
