import copy
from abc import ABC, abstractmethod


class FreePerson(ABC):
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def walk_north(self, dist):
        ...

    @abstractmethod
    def walk_east(self, dist):
        ...


class UnfreePerson:

    def __init__(self, position):
        self.is_free = False
        self.position = position


class Person(FreePerson):
    def __init__(self, position):
        super().__init__(position)

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(UnfreePerson):
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)

except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")