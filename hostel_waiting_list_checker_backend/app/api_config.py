from fastapi import FastAPI, APIRouter
from decouple import config
from .routes import student_router

api_router = APIRouter()


def get_application() -> FastAPI:
    application = FastAPI(title=config("API_TITLE"), debug=True)

    api_router.include_router(student_router.router, prefix="/student")

    application.include_router(api_router, prefix="")

    return application


app = get_application()
