from typing import Annotated

from pydantic import Field
from pydantic.v1 import PositiveFloat

from src.contrib.schemas import BaseSchema


class AtletaSchema(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", exemple='Joao', max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", exemple='12312312312', max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", exemple='25')]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", exemple='75.5')]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", exemple='1.70')]
    sexo: Annotated[str, Field(description="Sexo do atleta", exemple='M', max_length=1)]
