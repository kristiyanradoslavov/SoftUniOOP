from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUTS = ["Biologist", "Geodesist", "Meteorologist"]

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def check_astronaut_name(self, name):
        current_astronaut = [x for x in self.astronaut_repository.astronauts if x.name == name]
        if current_astronaut:
            return True
        else:
            return False

    def check_planet_name(self, name):
        current_planet = [x for x in self.planet_repository.planets if x.name == name]
        if current_planet:
            return True
        else:
            return False

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type not in SpaceStation.VALID_ASTRONAUTS:
            raise Exception("Astronaut type is not valid!")

        if self.check_astronaut_name(name):
            return f"{name} is already added."

        if astronaut_type == "Biologist":
            new_astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            new_astronaut = Geodesist(name)
        else:
            new_astronaut = Meteorologist(name)

        self.astronaut_repository.astronauts.append(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        if self.check_planet_name(name):
            return f"{name} is already added."

        new_planet = Planet(name)
        all_items = items.split(", ")
        for item in all_items:
            new_planet.items.append(item)

        self.planet_repository.planets.append(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        if not self.check_astronaut_name(name):
            raise Exception(f"Astronaut {name} doesn't exist!")

        for repo in self.astronaut_repository.astronauts:
            if repo.name == name:
                self.astronaut_repository.astronauts.remove(repo)
                return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        pass

    def report(self):
        pass


station = SpaceStation()
print(station.add_astronaut("Geodesist", "ivan"))
print(station.add_astronaut("Geodesist", "ivan"))
print(station.add_planet("venera", "metal, kamak, med, oro, goske"))
print(station.add_planet("venera", "metal, kamak, med, oro, goske"))
print(station.retire_astronaut("ivan"))
