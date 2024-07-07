from pydantic import BaseModel
from typing import Dict, List

class Recipe(BaseModel):
    title: str
    slugs: str
    ingredients: str
    preparation: str
    calories: str
    carb: str
    fat: str
    types: str
    category: str
    isdairy: int
    img: str
    
class Ingredients(BaseModel):
    ingredients: Dict[str, float]
    recommendations: List[Recipe]