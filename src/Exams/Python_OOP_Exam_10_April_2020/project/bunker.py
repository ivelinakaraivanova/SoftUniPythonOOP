from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []
        # self.food = []
        # self.water = []
        # self.painkillers = []
        # self.salves = []
        
    @property
    def food(self):
        foods = [f for f in self.supplies if f.__class__.__name__ == "FoodSupply"]
        if len(foods) == 0:
            raise IndexError("There are no food supplies left!")
        return foods
    
    @property
    def water(self):
        waters = [w for w in self.supplies if w.__class__.__name__ == "WaterSupply"]
        if len(waters) == 0:
            raise IndexError("There are no water supplies left!")
        return waters

    @property
    def painkillers(self):
        painkillers = [pk for pk in self.medicine if pk.__class__.__name__ == "Painkiller"]
        if len(painkillers) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = [sv for sv in self.medicine if sv.__class__.__name__ == "Salve"]
        if len(salves) == 0:
            raise IndexError("There are no salves left!")
        return self.salves

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        else:
            self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == "Painkiller":
                medicine_to_apply = self.painkillers[-1]
            else:
                medicine_to_apply = self.salves[-1]
            del self.medicine[-1]
            medicine_to_apply.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == "FoodSupply":
                sustenance_to_apply = self.food[-1]
            else:
                sustenance_to_apply = self.water[-1]
            del self.supplies[-1]
            sustenance_to_apply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")



