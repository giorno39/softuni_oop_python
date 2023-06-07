from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])


    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n"
        result += f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}"
        return result
