from OOP.inheritence.inheritence_exercise.project_players_and_monsters.hero import Hero


class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)