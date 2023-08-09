from nwon_baseline.pydantic.path_to_write_pydantic_model import path_to_write_pydantic_model as path_to_write_pydantic_model
from pydantic import BaseModel as BaseModel

def save_pydantic_model_instance_as_json(pydantic_model: BaseModel, file_path: str) -> str: ...
