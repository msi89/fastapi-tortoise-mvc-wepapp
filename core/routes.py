from fastapi import APIRouter
from core.controllers import auth, home
from core.middlewares import exceptions
router = APIRouter()

router.include_router(exceptions.router)
router.include_router(home.router, tags=home.tags)
router.include_router(auth.router, prefix='/auth', tags=auth.tags)
