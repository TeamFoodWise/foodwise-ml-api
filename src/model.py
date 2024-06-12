from typing import List
from pydantic import BaseModel

class IngredientsPayload(BaseModel):
    ingredients: List[str] = []