from project.appliances.appliance import Appliance


class Stove(Appliance):
    def __init__(self, cost):
        super().__init__(cost=0.7)
