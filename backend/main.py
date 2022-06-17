from fastapi import FastAPI
from core.config import settings
from apis.general.route_home import home_router
from fastapi.staticfiles import StaticFiles
from db.session import engine  # new
from db.base import Base  # new


def include_router(app):
    app.include_router(home_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()
    return app


app = start_application()
