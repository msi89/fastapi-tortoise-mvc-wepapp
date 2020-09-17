from fastapi import APIRouter, Request
from core.shortcuts import view


router = APIRouter()

tags = ['home']


@router.get("/")
async def index(request: Request):
    return view(request, template='index.html', context={"users": "asdhajsdhja"})
