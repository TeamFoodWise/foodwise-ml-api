import os
import pandas as pd
import ast
import time

class RecommendByIngredients:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        """Ensures only one instance of RecommendByIngredients exists."""
        if not cls.__instance:
            cls.__instance = super(RecommendByIngredients, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
    
    def __init__(self):
        # start = time.time()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, '..', 'data')
        
        self.data = self.load_df_from_csv(data_dir, 'clean_data.csv')
        # end = time.time()
        # print('init elapsed time: ', end - start)
    
    def load_df_from_csv(self, directory, filename):
        # start = time.time()
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)
        
        # change format to list
        df['ingredients'] = df['ingredients'].apply(lambda x: ast.literal_eval(x))
        df['nutrition'] = df['nutrition'].apply(lambda x : ast.literal_eval(x))
        df['steps'] = df['steps'].apply(lambda x : ast.literal_eval(x))
        df['tags'] = df['tags'].apply(lambda x : ast.literal_eval(x))
        
        # end = time.time()
        # print('load from csv elapsed time: ', end - start)
        
        return df
    
    def get_recipe_recommendations(self, ingredients_input):
        # start = time.time()
        recommendation_df = self.top_recipes_by_ingredients(ingredients_input)
        # end = time.time()
        # print('get_recipe_recommendations elapsed time: ', end - start)
        return self.recommendation_to_list(recommendation_df)
        
    def top_recipes_by_ingredients(self, ingredients_input):
        # start = time.time()
        # Copy dataset
        top_recipes = self.data.copy()
        
        # Convert ingredients input to a set for faster operation
        ingredients_set = set(ingredients_input)

        # Define a function to count how many input ingredients are in each recipe
        def ingredient_match_count(recipe_ingredients):
            recipe_ingredients_set = set(recipe_ingredients)
            return len(ingredients_set.intersection(recipe_ingredients_set))

        # Apply the function to count matches and add a new column 'match_count'
        top_recipes['match_count'] = top_recipes['ingredients'].apply(ingredient_match_count)

        # Aggregate data to avoid duplicates and sort by 'match_count'
        aggregated_data = top_recipes.groupby('name').agg(
            {'match_count': 'max',
             'ingredients': 'first',
             'n_ingredients': 'first',
             'steps': 'first',
             'minutes': 'first',
             'description' : 'first',
             'date' : 'first',
             'rating': 'first',
            }).reset_index()
        
        # Filter out rows with match_count equal to 0
        aggregated_data = aggregated_data[aggregated_data['match_count'] > 0]

        # Find the maximum match_count
        max_match_count = aggregated_data['match_count'].max()

        # Show top recipes
        top_recipes = (aggregated_data
                        .sort_values(by='match_count', ascending=False)
                        .head(max_match_count * 10))
        
        # end = time.time()
        # print('top_recipes_by_ingredients elapsed time: ', end - start)
        
        return top_recipes
    
    def recommendation_to_list(self, recipe_dataframe):
        # start = time.time()
        list_of_recipes = []
        
        for index, row in recipe_dataframe.iterrows():
            recipe = row.to_dict()
            data = {
                'index': index,
                'name' : recipe['name'].title(),
                'ingredients' : recipe['ingredients'],
                'n_ingredients': recipe['n_ingredients'],
                'steps' : recipe['steps'],
                'minutes': recipe['minutes'],
                'description' : recipe['description'],
                'date' : recipe['date'],
                'rating': recipe['rating'],
            }
            
            list_of_recipes.append(data)
        
        # end = time.time()
        # print('recommendation_to_list elapsed time: ', end - start)
        return list_of_recipes