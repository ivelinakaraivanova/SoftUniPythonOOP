from project.appliances.appliance import Appliance


class Laptop(Appliance):
    def __init__(self, cost):
        super().__init__(cost=1)
