import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException, StarletteHTTPException

from tortoise.contrib.fastapi import register_tortoise
from core import settings
from core.routes import router
from core.shortcuts import redirect

app = FastAPI()


register_tortoise(app, config=settings.TORTOISE_ORM, generate_schemas=True,
                  add_exception_handlers=True)

app.mount(settings.STATIC_FILES, StaticFiles(
    directory=settings.STATIC_FOLDER), name='static')

app.include_router(router)


@app.on_event('startup')
async def onstartup():
    logging.info('app is started...')


@app.on_event('shutdown')
async def onshutdown():
    logging.info('app is stopped...')


@app.exception_handler(HTTPException)
async def http_exception_handler(request, ex):
    if ex.status_code == 401:
        return redirect('/auth/signup')
    return redirect('/404')


@app.exception_handler(StarletteHTTPException)
async def starlette_exception_handler(request, ex):
    return redirect('/404')


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return HTMLResponse(str(exc) + '\nValidation Error: ', status_code=400)
