import os

import uvicorn
from api.routes.api import router as api_router
from core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from core.events import create_start_app_handler
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router, prefix=API_PREFIX)
    pre_load = False
    if pre_load:
        application.add_event_handler("startup", create_start_app_handler(application))
    return application


app = get_application()

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = os.environ.get("PORT", 8080)
    reload = os.environ.get("RELOAD", False)
    debug = os.environ.get("DEBUG", False)
    uvicorn.run("main:app", host=host, port=int(port), reload=reload, debug=debug)
