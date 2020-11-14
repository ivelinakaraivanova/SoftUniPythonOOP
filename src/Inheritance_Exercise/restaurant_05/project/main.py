from restaurant_05.project.product import Product
from restaurant_05.project.beverage.beverage import Beverage
from restaurant_05.project.food.food import Food
from restaurant_05.project.beverage.hot_beverage import HotBeverage
from restaurant_05.project.beverage.cold_beverage import ColdBeverage
from restaurant_05.project.beverage.coffee import Coffee
from restaurant_05.project.beverage.tea import Tea
from restaurant_05.project.food.main_dish import MainDish
from restaurant_05.project.food.starter import Starter
from restaurant_05.project.food.dessert import Dessert
from restaurant_05.project.food.cake import Cake
from restaurant_05.project.food.salmon import Salmon
from restaurant_05.project.food.soup import Soup

c = Coffee("Italian", 3, 2, 22)
print(c.name)
print(c.price)
print(c.milliliters)
print(c.caffeine)
