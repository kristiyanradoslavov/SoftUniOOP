class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        # if astronaut in self.astronauts:
        self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        astronaut_instance = [a for a in self.astronauts if a.name == name]

        if astronaut_instance:
            return astronaut_instance[0]


