from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet_repository import PlanetRepository
from project.space_station import SpaceStation


station = SpaceStation()
print(station.add_astronaut("Geodesist", "ivan"))
print(station.add_astronaut("Geodesist", "ivan"))
