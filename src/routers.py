from fastapi import APIRouter

from atleta.controller import router as atletas
from src.centro_treinamento.controller import router as centro_de_treinamento
from categorias.controller import router as categorias

app_router = APIRouter()

app_router.include_router(atletas, prefix="/atletas", tags=["atletas"])
app_router.include_router(categorias, prefix="/categorias", tags=["categorias"])
app_router.include_router(centro_de_treinamento, prefix="/centro-dos-treinamentos", tags=["centro-dos-treinamentos"])
