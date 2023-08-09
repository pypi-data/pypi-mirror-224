from nwon_baseline.pydantic.path_to_write_pydantic_model import path_to_write_pydantic_model as path_to_write_pydantic_model
from pydantic import BaseModel as BaseModel
from typing import Type

def save_pydantic_model_schema(pydantic_model: Type[BaseModel], file_path: str) -> str: ...
