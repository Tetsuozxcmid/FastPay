from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from core.handlers.pages import views as pages_views
from core.handlers.payment import views as payment_views


from core.config import Config

app = FastAPI()


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
async def startup_event():
    app.state.stripe_customer_id = Config.get_customer_id()

app.include_router(pages_views.router)
app.include_router(payment_views.router)
