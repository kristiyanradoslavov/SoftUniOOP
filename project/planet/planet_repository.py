class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet):
        self.planets.append(planet)

    def remove(self, planet):
        # if planet in self.planets:
        self.planets.remove(planet)

    def find_by_name(self, name):
        planet_instance = [p for p in self.planets if p.name == name]

        if planet_instance:
            return planet_instance[0]

