import logging
from app.core.settings.app import AppSettings
from pydantic import PostgresDsn, SecretStr


class TestAppSettings(AppSettings):
    title: str = "Test FastAPI example application"
    secret_key: SecretStr
    database_url: PostgresDsn
    logging_level: int = logging.DEBUG

    class Config:
        env_file = ".\env"
