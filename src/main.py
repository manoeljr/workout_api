from fastapi import FastAPI
from src.routers import app_router


app = FastAPI(
    title='WorkoutAPI'
)
app.include_router(app_router)


if __name__ == '__name__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
