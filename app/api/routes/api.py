from app.api.dependencies.secret_key import secret_key_dep
from app.api.routes.public import choices, games, scenes
from app.api.routes.secret import (
    choices as secret_choices,
    games as secret_games,
    scenes as secret_scenes,
)
from fastapi import APIRouter, Depends


router = APIRouter()
# router.include_router(test.router)
router.include_router(games.router)
router.include_router(scenes.router)
router.include_router(choices.router)

router.include_router(secret_games.router, dependencies=[Depends(secret_key_dep)])
router.include_router(secret_scenes.router, dependencies=[Depends(secret_key_dep)])
router.include_router(secret_choices.router, dependencies=[Depends(secret_key_dep)])
