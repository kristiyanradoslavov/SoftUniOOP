from OOP.inheritence.inheritence_exercise.project_players_and_monsters.dark_knight import DarkKnight


class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        super().__init__(username, level)