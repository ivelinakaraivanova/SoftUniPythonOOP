from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        ingredients_types = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]
        if ingredient_type in ingredients_types:
            if self.can_add(quantity):
                if ingredient_type not in self.ingredients:
                    self.ingredients[ingredient_type] = quantity
                else:
                    self.ingredients[ingredient_type] += quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients:
            if self.ingredients[ingredient_type] >= quantity:
                self.ingredients[ingredient_type] -= quantity
            else:
                raise ValueError("Ingredient quantity cannot be less than zero")
        else:
            raise KeyError("No such product in the factory")

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes:
            raise TypeError("No such recipe")
        else:
            if recipe_name not in self.products:
                self.products[recipe_name] = 1
            else:
                self.products[recipe_name] += 1
            for ingredient_name in self.recipes[recipe_name]:
                self.remove_ingredient(ingredient_name, self.recipes[recipe_name][ingredient_name])
