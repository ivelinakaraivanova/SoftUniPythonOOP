class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)

    def __repr__(self):
        return self.name + " " + self.surname


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group('Name', self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(p.__repr__() for p in self.people)}"

    def __getitem__(self, key):
        return f"Person {key}: {self.people[key].__repr__()}"
