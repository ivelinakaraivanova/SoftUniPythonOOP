from project.software.software import Software


class Hardware:
    def __init__(self, name:str, type:str, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self._free_capacity = capacity
        self._free_memory = memory

    def install(self, software:Software):
        if software.capacity_consumption <= self._free_capacity and software.memory_consumption <= self._free_memory:
            self.software_components.append(software)
            self._free_capacity -= software.capacity_consumption
            self._free_memory -= software.memory_consumption
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software:Software):
        if software in self.software_components:
            self.software_components.remove(software)
            self._free_capacity += software.capacity_consumption
            self._free_memory += software.memory_consumption
