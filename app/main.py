from fastapi import FastAPI

from app.routes import (
    summarize,
    translate,
    email_generator
)

from app.core.config import (
    APP_NAME,
    VERSION
)

from app.exceptions.handlers import (
    generic_exception_handler
)

app = FastAPI(
    title=APP_NAME,
    version=VERSION
)

app.include_router(
    summarize.router
)

app.include_router(
    translate.router
)

app.include_router(
    email_generator.router
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)