import uvicorn
from fastapi import FastAPI
from settings import app_settings


app = FastAPI(
    title="Learning FastAPI",
    summary="Изучаем FastAPI",
    version=app_settings.version,
    debug=app_settings.debug,
    docs_url="/swagger",
    description="Пробный проект с целью изучить FastAPI",
)


if __name__ == "__main__":
    uvicorn.run(app="app:app", reload=True, workers=1)
