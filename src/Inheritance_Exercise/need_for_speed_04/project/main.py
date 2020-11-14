from need_for_speed_04.project.vehicle import Vehicle
from need_for_speed_04.project.car import Car
from need_for_speed_04.project.motorcycle import Motorcycle
from need_for_speed_04.project.sport_car import SportCar
from need_for_speed_04.project.family_car import FamilyCar
from need_for_speed_04.project.race_motorcycle import RaceMotorcycle
from need_for_speed_04.project.cross_motorcycle import CrossMotorcycle


for c in [Vehicle, Car, Motorcycle, FamilyCar, SportCar, CrossMotorcycle, RaceMotorcycle]:
    print(c.__name__, '-->', c.__mro__[1].__name__)

c = Car(30, 50)
print(c.drive(10))
print(c.fuel)