from project_unfinished.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def __init__(self, budget):
        super().__init__(budget)

    @property
    def expenses_per_race(self):
        return 250000

    def calculate_revenue_after_race(self, race_pos):
        pass


red = RedBullTeam(5000000)
