from app.core.config import get_app_settings
from fastapi import HTTPException, Header, Request, status
from typing import Annotated


async def secret_key_dep(secret: Annotated[str | None, Header()] = None):
    settings = get_app_settings()

    if (settings.app_env.name != "prod") and (not secret):
        return {"secret": settings.secret_key}

    if not secret:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorized"
        )

    if secret != settings.secret_key.get_secret_value():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorized"
        )
