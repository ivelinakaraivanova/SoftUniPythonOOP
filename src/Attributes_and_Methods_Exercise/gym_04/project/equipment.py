class Equipment:
    class_id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.class_id
        Equipment.class_id += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.class_id
