import logging
from app.core.settings.app import AppSettings, PostgresDsn, SecretStr


class DevAppSettings(AppSettings):
    title: str = "Storytelling API Swagger Documentation"
    logging_level: int = logging.DEBUG

    debug: bool
    database_url: PostgresDsn
    secret_key: SecretStr

    class Config:
        env_file = ".\env"
