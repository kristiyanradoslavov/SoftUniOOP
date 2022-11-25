from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    @abstractmethod
    def __init__(self, budget):
        self.budget = budget
        self.revenue = self.expenses_per_race

    @abstractmethod
    @property
    def expenses_per_race(self):
        pass

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos):
        pass
