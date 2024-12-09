import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title="Learning FastAPI",
    summary="Изучаем FastAPI",
    version="0.1.0",
    debug=True,
    docs_url="/swagger",
    description="Пробный проект с целью изучить FastAPI",
)


if __name__ == "__main__":
    uvicorn.run(app="app:app", reload=True, workers=1)
