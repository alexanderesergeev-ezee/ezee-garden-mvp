from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.health import router as health_router
from app.web.routes import router as web_router


def create_app() -> FastAPI:
    app = FastAPI(title="ezee-garden-mvp", version="0.1.0")

    app.mount("/static", StaticFiles(directory="app/static"), name="static")

    app.include_router(web_router)
    app.include_router(health_router, prefix="/api")

    return app


app = create_app()
