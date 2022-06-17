from fastapi import FastAPI
from core.config import settings
from apis.general.route_home import home_router


def include_router(app):
    app.include_router(home_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    return app


app = start_application()
