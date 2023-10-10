from app.core.settings.app import AppSettings, PostgresDsn, SecretStr
from pathlib import Path


class ProdAppSettings(AppSettings):
    docs_url: str | None = None
    openapi_prefix: str | None = None
    openapi_url: str | None = None
    redoc_url: str | None = None

    debug: bool
    database_url: PostgresDsn
    secret_key: SecretStr

    class Config:
        env_file = ".\env"
