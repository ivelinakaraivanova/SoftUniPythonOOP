class PizzaDelivery:
    ordered = False

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if not self.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity
            else:
                self.ingredients[ingredient] = quantity
            self.price += ingredient_price * quantity
        else:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if not self.ordered:
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            if quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"
            self.ingredients[ingredient] -= quantity
            self.price -= ingredient_price * quantity
        else:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

    def pizza_ordered(self):
        self.ordered = True
        pizza_info = f"You've ordered pizza {self.name} prepared with "
        ingredients_list =[f"{ingredient}: {quantity}" for ingredient, quantity in self.ingredients.items()]
        ingredients_info = ", ".join(ingredients_list)
        price_info = f" and the price will be {self.price}lv."
        result = pizza_info + ingredients_info + price_info
        return result


Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
Margarita.add_extra('mozzarella', 1, 0.5)
Margarita.add_extra('cheese', 1, 1)
Margarita.remove_ingredient('cheese', 1, 1)
print(Margarita.remove_ingredient('bacon', 1, 2.5))
print(Margarita.remove_ingredient('tomatoes', 2, 0.5))
Margarita.remove_ingredient('cheese', 2, 1)
print(Margarita.pizza_ordered())
print(Margarita.add_extra('cheese', 1, 1))