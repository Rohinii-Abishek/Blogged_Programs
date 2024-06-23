class Ingredient:
   # Class to represent a recipe ingredient.
    def __init__(self, name, quantity, unit="g"):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"
class Recipe:
    # Class to represent a recipe with ingredients, instructions, and other details.
    def __init__(self, name, description="", ingredients=[], instructions=[]):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
    def add_ingredient(self, ingredient):
       # Adds an ingredient to the recipe.
    
        self.ingredients.append(ingredient)
    def add_instruction(self, instruction):
       # Adds an instruction step to the recipe.

        self.instructions.append(instruction)
    def __str__(self):
       # Provides a formatted string representation of the recipe.
        output = f"\n Recipe : {self.name}\n"
        if self.description:
            output += f"Description: {self.description}\n"
        output += "Ingredients:\n"
        for ingredient in self.ingredients:
            output += f"- {ingredient}\n"
        output += "Instructions:\n"
        for step, instruction in enumerate(self.instructions, 1):
            output += f"{step}. {instruction}\n"
        return output
class RecipeManager:
      # Class to manage a collection of recipes, providing methods for adding, searching, and viewing recipes.
    def __init__(self):
        self.recipes = []
    def add_recipe(self, recipe):
      #  Adds a recipe to the recipe manager.
      self.recipes.append(recipe)
    def view_recipes(self):
      # Displays all recipes using enumeration.
        if not self.recipes:
            print("No recipes found.")
        else:
            print("\nAvailable Recipes:")
            for i, recipe in enumerate(self.recipes, 1):
                print(f"{i}. {recipe.name}")
            print("\n")
    def view_recipe_by_index(self, recipe_index):
       # Displays the details of a recipe based on its index in the list.
       # Handles potential index errors.
        if 0 < recipe_index <= len(self.recipes):
            print(self.recipes[recipe_index - 1])  # Access recipe using index-1
        else:
            print(f"Invalid recipe selection. Please choose a number between 1 and {len(self.recipes)}.")
def main():
    recipe_manager = RecipeManager()
    poha_recipe = Recipe("Poha")
    # Adding ingredients and instructions to the Poha recipe
    poha_recipe.add_ingredient(Ingredient("Flattened Rice (Poha)", 2, "cups"))
    poha_recipe.add_ingredient(Ingredient("Onion", 1, "medium"))
    poha_recipe.add_ingredient(Ingredient("Peanuts", 1/4, "cup"))
    poha_recipe.add_ingredient(Ingredient("Curry Leaves", 10))
    poha_recipe.add_ingredient(Ingredient("Mustard Seeds", 1/2, "teaspoon"))
    poha_ingredient = Ingredient("Green Chillies", 1, "optional")  # Optional ingredient
    poha_recipe.add_ingredient(poha_ingredient)
    poha_recipe.add_ingredient(Ingredient("Salt", "to taste"))
    poha_recipe.add_ingredient(Ingredient("Lemon Juice", 1, "tablespoon (optional)"))
    poha_recipe.add_instruction("Wash and rinse the poha in a colander until the water runs clear.")
    poha_recipe.add_instruction("Drain the poha and set it aside in a large bowl.")
    poha_recipe.add_instruction("Heat oil in a pan over medium heat.")
    poha_recipe.add_instruction("Add mustard seeds and let them splutter for a few seconds.")
    recipe_manager.add_recipe(poha_recipe)
    
    orange_juice_recipe = Recipe("Orange Juice")
    # Adding ingredients and instructions to the Orange Juice recipe
    orange_juice_recipe.add_ingredient(Ingredient("Oranges", 4))
    orange_juice_recipe.add_ingredient(Ingredient("Water", 1/2, "cup"))
    orange_juice_recipe.add_ingredient(Ingredient("Sugar", 2, "tablespoons (optional)"))
    orange_juice_recipe.add_instruction("Peel the oranges and remove any seeds.")
    orange_juice_recipe.add_instruction("Place the oranges and water in a blender.")
    orange_juice_recipe.add_instruction("Blend until smooth.")
    orange_juice_recipe.add_instruction("Taste and add sugar if desired, then blend again.")
    orange_juice_recipe.add_instruction("Strain the juice through a fine mesh sieve if a smoother texture is desired.")
    
    # Add the Orange Juice recipe to the manager
    recipe_manager.add_recipe(orange_juice_recipe)
    while True:
        recipe_manager.view_recipes()
        choice = input("Enter the index of the recipe you want to view (or enter 'q' to quit): ")
        if choice.lower() == "q":
            break
        elif choice.isdigit():
            recipe_index = int(choice)
            recipe_manager.view_recipe_by_index(recipe_index)
        else:
            print("Invalid input. Please enter a valid index or 'q' to quit.")
if __name__ == "__main__":
    main()