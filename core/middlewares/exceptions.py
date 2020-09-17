from fastapi import APIRouter, Request
from core.shortcuts import view

router = APIRouter()


@router.get('404')
async def error404(request: Request):
    return view(request, template='error/404.html')
