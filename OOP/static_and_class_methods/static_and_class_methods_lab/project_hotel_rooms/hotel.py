from OOP.static_and_class_methods.static_and_class_methods_lab.project_hotel_rooms.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        current_room = [i for i in self.rooms if i.number == room_number]
        if not current_room[0].is_taken and people <= current_room[0].capacity:
            self.guests += people
        current_room[0].take_room(people)

    def free_room(self, room_number):
        current_room = list(filter(lambda r: r.number == room_number, self.rooms))
        if current_room[0].is_taken:
            self.guests -= current_room[0].guests
        current_room[0].free_room()

    def status(self):
        all_free_rooms = [str(i.number) for i in self.rooms if not i.is_taken]
        all_taken_rooms = [str(i.number) for i in self.rooms if i.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(all_free_rooms)}\n" \
               f"Taken rooms: {', '.join(all_taken_rooms)}"


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())

