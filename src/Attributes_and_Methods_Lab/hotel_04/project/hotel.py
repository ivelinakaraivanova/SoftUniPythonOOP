class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        rooms_list = [r for r in self.rooms if r.number == room_number]
        if rooms_list:
            room = rooms_list[0]
            if room.take_room(people) is None:
                self.guests += people
            else:
                room.take_room(people)

    def free_room(self, room_number):
        rooms_list = [r for r in self.rooms if r.number == room_number]
        if rooms_list:
            room = rooms_list[0]
            if room.free_room() is None:
                self.guests -= room.guests
            else:
                room.free_room()

    def print_status(self):
        print(f"Hotel {self.name} has {self.guests} total guests")
        free_rooms = [r.number for r in self.rooms if not r.is_taken]
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        print(f"Free rooms: {', '.join(str(r) for r in free_rooms)}")
        print(f"Taken rooms: {', '.join(str(r) for r in taken_rooms)}")
