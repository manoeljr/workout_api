from pydantic import Field
from sqlalchemy.sql.annotation import Annotated

from src.contrib.schemas import BaseSchema


class CategoriaSchema(BaseSchema):
    nome: Annotated[str, Field(description="Categoria do atleta", exemple='Scale', max_length=10)]
