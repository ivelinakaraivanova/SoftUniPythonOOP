class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        workers = [w for w in self.workers if w.name == worker_name]
        if workers:
            self.workers.remove(workers[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salaries = [w.salary for w in self.workers]
        total_salary = sum(workers_salaries)
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_needs = [a.get_needs() for a in self.animals]
        total_needs = sum(animals_needs)
        if self.__budget >= total_needs:
            self.__budget -= total_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        lions = [a.__repr__() for a in self.animals if isinstance(a, Lion)]
        tigers = [a.__repr__() for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a.__repr__() for a in self.animals if isinstance(a, Cheetah)]
        lions_count = len(lions)
        tigers_count = len(tigers)
        cheetahs_count = len(cheetahs)
        delimiter = '\n'
        result = f"You have {total_animals_count} animals" + delimiter
        result += f"----- {lions_count} Lions:" + delimiter
        result += f"{delimiter.join(lions)}" + delimiter
        result += f"----- {tigers_count} Tigers:" + delimiter
        result += f"{delimiter.join(tigers)}" + delimiter
        result += f"----- {cheetahs_count} Cheetahs:" + delimiter
        result += f"{delimiter.join(cheetahs)}"
        return result

    def workers_status(self):
        total_workers_count = len(self.workers)
        keepers = [w.__repr__() for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w.__repr__() for w in self.workers if isinstance(w, Caretaker)]
        vets = [w.__repr__() for w in self.workers if isinstance(w, Vet)]
        keepers_count = len(keepers)
        caretakers_count = len(caretakers)
        vets_count = len(vets)
        delimiter = '\n'
        result = f"You have {total_workers_count} workers" + delimiter
        result += f"----- {keepers_count} Keepers:" + delimiter
        result += f"{delimiter.join(keepers)}" + delimiter
        result += f"----- {caretakers_count} Caretakers:" + delimiter
        result += f"{delimiter.join(caretakers)}" + delimiter
        result += f"----- {vets_count} Vets:" + delimiter
        result += f"{delimiter.join(vets)}"
        return result


from wild_cat_zoo_01.project.caretaker import Caretaker
from wild_cat_zoo_01.project.cheetah import Cheetah
from wild_cat_zoo_01.project.keeper import Keeper
from wild_cat_zoo_01.project.lion import Lion
from wild_cat_zoo_01.project.tiger import Tiger
from wild_cat_zoo_01.project.vet import Vet

zoo = Zoo("Zootopia", 3000, 5, 8)
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1),
           Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3),
           Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
prices = [200, 190, 204, 156, 211, 140]
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80),
           Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140),
           Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

for worker in workers:
    print(zoo.hire_worker(worker))

print(zoo.tend_animals())
print(zoo.pay_workers())
print(zoo.fire_worker("Adam"))
print(zoo.animals_status())
print(zoo.workers_status())
