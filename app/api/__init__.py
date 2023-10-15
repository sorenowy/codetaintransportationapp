from fastapi import FastAPI

from app.config.constants import API_PREFIX
from .v1.events.events import event_handler
from .v1.controllers.user_controller import users_router
from .v1.controllers.route_controller import route_router
from .v1.controllers.login_controller import login_router
from .v1.controllers.register_controller import register_router

def initialize_api(app: FastAPI):
    app.title = "Codetain Transportation API"
    app.description = "This is an application provider interface for transport routes and overall logic behind users"
    app.version = "1.0.0"
    app.include_router(event_handler)
    app.include_router(users_router, prefix=API_PREFIX)
    app.include_router(route_router, prefix=API_PREFIX)
    app.include_router(register_router, prefix=API_PREFIX)
    app.include_router(login_router, prefix=API_PREFIX)
