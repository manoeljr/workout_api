from pydantic import Field
from sqlalchemy.sql.annotation import Annotated

from src.contrib.schemas import BaseSchema


class CentroTreinamentoSchema(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Centro de Treinamento", exemple='CT King', max_length=20)]
    endereco: Annotated[str, Field(description="Nome do endereço", exemple='CT King', max_length=60)]
    poprietario: Annotated[str, Field(description="Nome do Proprietario", exemple='CT King', max_length=30)]