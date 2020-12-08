from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([room.expenses + room.room_cost for room in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        results = []
        for room in self.rooms:
            room_exp = room.expenses + room.room_cost
            if room_exp <= room.budget:
                room.budget -= room_exp
                result = f"{room.family_name} paid {room_exp:.2f}$ and have {room.budget:.2f}$ left."
            else:
                result = f"{room.family_name} does not have enough budget and must leave the hotel."
                self.rooms.remove(room)
            results.append(result)
        return "\n".join(results)

    def status(self):
        results = []
        total_people = sum([room.members_count for room in self.rooms])
        result = f"Total population: {total_people}"
        results.append(result)
        for room in self.rooms:
            room_info = f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$"
            results.append(room_info)
            if len(room.children) > 0:
                for child in room.children:
                    child_info = f"--- Child {room.children.index(child)+1} monthly cost: {child.get_monthly_expense():.2f}$"
                    results.append(child_info)
            if len(room.appliances) > 0:
                appliances_info = f"--- Appliances monthly cost: {sum([appl.get_monthly_expense() for appl in room.appliances]):.2f}$"
                results.append(appliances_info)
        return "\n".join(results)
