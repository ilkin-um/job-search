from fastapi import APIRouter
from apis.v1 import route_general_pages, route_users, route_jobs, route_login


api_router = APIRouter()

api_router.include_router(route_general_pages.router, prefix="", tags=["general_pages"])

api_router.include_router(route_users.router, prefix="/users", tags=["users"])

api_router.include_router(route_jobs.router, prefix="/jobs", tags=["jobs"])

api_router.include_router(route_login.router, prefix="/login", tags=["login"])
