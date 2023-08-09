from nwon_baseline.typings import AnyDict
from pydantic import BaseModel

def pydantic_model_to_dict(model: BaseModel) -> AnyDict: ...
