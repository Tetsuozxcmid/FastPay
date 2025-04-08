from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["PagesCalling"])

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/succes", response_class=HTMLResponse)
async def success(request: Request):
    return templates.TemplateResponse("succes.html", {"request": request})


@router.get("/cancel", response_class=HTMLResponse)
async def cancel(request: Request):
    return templates.TemplateResponse("cancel.html", {"request": request})
