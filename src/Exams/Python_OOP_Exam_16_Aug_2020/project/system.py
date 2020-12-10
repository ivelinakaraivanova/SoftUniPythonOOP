from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name:str, capacity, memory):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name:str, capacity, memory):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption, memory_consumption):
        hardware_names = [h.name for h in System._hardware if h.name == hardware_name]
        if hardware_name not in hardware_names:
            return "Hardware does not exist"
        hardware = [h for h in System._hardware if h.name == hardware_name][0]
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except Exception as e:
            return str(e)

    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        hardware_names = [h.name for h in System._hardware if h.name == hardware_name]
        if hardware_name not in hardware_names:
            return "Hardware does not exist"
        hardware = [h for h in System._hardware if h.name == hardware_name][0]
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(light_software)
            System._software.append(light_software)
        except Exception as e:
            return str(e)

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        hardwares = [h for h in System._hardware if h.name == hardware_name]
        softwares = [s for s in System._software if s.name == software_name]
        if hardwares and softwares:
            hardware = hardwares[0]
            software = softwares[0]
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"


    @staticmethod
    def analyze():
        result = ''
        system_analysis = f"System Analysis\n"
        hardware_comps_info = f"Hardware Components: {len(System._hardware)}\n"
        software_comps_info = f"Software Components: {len(System._software)}\n"
        total_used_memory = sum([s.memory_consumption for s in System._software])
        total_memory = sum([h.memory for h in System._hardware])
        total_used_space = sum([s.capacity_consumption for s in System._software])
        total_capacity = sum([h.capacity for h in System._hardware])
        total_memory_info = f"Total Operational Memory: {int(total_used_memory)} / {int(total_memory)}\n"
        total_capacity_info = f"Total Capacity Taken: {int(total_used_space)} / {int(total_capacity)}"
        result = system_analysis + hardware_comps_info + software_comps_info + total_memory_info + total_capacity_info
        return result

    @staticmethod
    def system_split():
        results = []
        for hard in System._hardware:
            result = ''
            hard_name_info = f"Hardware Component - {hard.name}\n"
            express_soft_info = f"Express Software Components: " \
                                 f"{len([s for s in hard.software_components if s.type == 'Express'])}\n"
            light_soft_info = f"Light Software Components: " \
                              f"{len([s for s in hard.software_components if s.type == 'Light'])}\n"
            memory_usage_info = f"Memory Usage: " \
                                f"{int(sum([s.memory_consumption for s in hard.software_components]))} " \
                                f"/ {int(hard.memory)}\n"
            capacity_usage_info = f"Capacity Usage: " \
                                  f"{int(sum([s.capacity_consumption for s in hard.software_components]))} " \
                                  f"/ {int(hard.capacity)}\n"
            type_info = f"Type: {hard.type}\n"
            soft_components_info = f"Software Components: {', '.join([s.name for s in hard.software_components]) or None}"
            result = hard_name_info + express_soft_info + light_soft_info + memory_usage_info\
                        + capacity_usage_info + type_info + soft_components_info
            results.append(result)
        return "".join(results)

