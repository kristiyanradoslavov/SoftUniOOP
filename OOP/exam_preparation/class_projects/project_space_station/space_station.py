from OOP.exam_preparation.class_projects.project_space_station.astronaut.astronaut_repository import AstronautRepository
from OOP.exam_preparation.class_projects.project_space_station.astronaut.biologist import Biologist
from OOP.exam_preparation.class_projects.project_space_station.astronaut.geodesist import Geodesist
from OOP.exam_preparation.class_projects.project_space_station.astronaut.meteorologist import Meteorologist
from OOP.exam_preparation.class_projects.project_space_station.planet.planet import Planet
from OOP.exam_preparation.class_projects.project_space_station.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUTS = ["Biologist", "Geodesist", "Meteorologist"]

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type not in SpaceStation.VALID_ASTRONAUTS:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type == "Biologist":
            new_astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            new_astronaut = Geodesist(name)
        else:
            new_astronaut = Meteorologist(name)

        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        new_planet = Planet(name)
        all_items = items.split(", ")
        for item in all_items:
            new_planet.items.append(item)

        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        if not self.astronaut_repository.find_by_name(name):
            raise Exception(f"Astronaut {name} doesn't exist!")

        for repo in self.astronaut_repository.astronauts:
            if repo.name == name:
                self.astronaut_repository.remove(repo)
                return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")

        filtered_astronauts = [x for x in self.astronaut_repository.astronauts if x.oxygen > 30]
        sorted_astronauts = sorted(filtered_astronauts, key=lambda x: -x.oxygen)[:5]

        if not sorted_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        planet = self.planet_repository.find_by_name(planet_name)
        participated = 0

        for astronaut in sorted_astronauts:
            if planet.items:
                participated += 1
            while planet.items:
                item = planet.items.pop()
                astronaut.backpack.append(item)
                astronaut.breathe()
                if astronaut.oxygen <= 0:
                    break

        if planet.items:
            self.unsuccessful_missions += 1
            return "Mission is not completed."
        else:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {participated} " \
                   f"astronauts participated in collecting items."  # the len here, might be different

    def report(self):
        final_result = [f"{self.successful_missions} successful missions!",
                        f"{self.unsuccessful_missions} missions were not completed!", "Astronauts' info:"]

        for astronaut in self.astronaut_repository.astronauts:
            final_result.append(str(astronaut))

        return '\n'.join(final_result)


# station = SpaceStation()
# print(station.add_astronaut("Geodesist", "ivan"))
# print(station.add_astronaut("Geodesist", "pesho"))
# print(station.add_astronaut("Biologist", "gosho"))
# print(station.add_astronaut("Meteorologist", "stanimir"))
# print(station.add_astronaut("Biologist", "ceci"))
# print(station.add_astronaut("Geodesist", "stoqn"))
# print(station.add_astronaut("Meteorologist", "rangel"))
# station.astronaut_repository.astronauts[0].oxygen = 20
#
# print(station.add_planet("venera", "metal, kamak, med, oro, goske, sirene, buchka, qdene, qica, belo, treva, sopoli"))
# print(station.add_planet("venera", "metal, kamak, med, oro, goske"))
# print(station.retire_astronaut("ivan"))
# print(station.send_on_mission("venera"))
#
# print(station.report())
