from fastapi import FastAPI                        # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from src.model import IngredientsPayload
from src.recommender import RecommendByIngredients

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

recommender = RecommendByIngredients()

@app.post('/recipes')
async def get_recipes_by_ingredients(payload: IngredientsPayload):
    recipe_recommendations = recommender.get_recipe_recommendations(payload.ingredients)
    return { "data" : recipe_recommendations }