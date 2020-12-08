from project.appliances.appliance import Appliance


class TV(Appliance):
    def __init__(self, cost):
        super().__init__(cost=1.5)
