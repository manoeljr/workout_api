from fastapi import APIRouter, status

from src.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post('', summary='Criar novo atleta', status_code=status.HTTP_201_CREATED)
async def post(db_session: DatabaseDependency):
    ...
