from fastapi import APIRouter
from apis.v1 import route_general_pages
from apis.v1 import route_users


api_router = APIRouter()

api_router.include_router(route_general_pages.router, prefix="", tags=["general_pages"])

api_router.include_router(route_users.router, prefix="/users", tags=["users"])
