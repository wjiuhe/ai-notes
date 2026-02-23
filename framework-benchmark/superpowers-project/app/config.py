from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg2://postgres:password@localhost:5432/expenses"
    test_database_url: str = "postgresql+psycopg2://postgres:password@localhost:5432/expenses_test"

    class Config:
        env_file = ".env"


settings = Settings()
