from OOP.exam_preparation.class_projects.project_horse_race.horse_race import HorseRace
from OOP.exam_preparation.class_projects.project_horse_race.horse_specification.appaloosa import Appaloosa
from OOP.exam_preparation.class_projects.project_horse_race.horse_specification.thoroughbred import Thoroughbred
from OOP.exam_preparation.class_projects.project_horse_race.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = ["Appaloosa", "Thoroughbred"]

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        if horse_type in self.VALID_HORSE_TYPES:
            all_horse_names = [x.name for x in self.horses]

            if horse_type == "Appaloosa":
                new_horse = Appaloosa(horse_name, horse_speed)

            else:
                new_horse = Thoroughbred(horse_name, horse_speed)

            if horse_name in all_horse_names:
                raise Exception(f"Horse {horse_name} has been already added!")

            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        all_jockeys_names = [x.name for x in self.jockeys]

        if jockey_name in all_jockeys_names:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        all_race_types = [x.race_type for x in self.horse_races]

        if race_type in all_race_types:
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        all_jockeys_names = [x.name for x in self.jockeys]
        if jockey_name not in all_jockeys_names:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        current_horse = []
        for index in range(len(self.horses) - 1, -1, -1):
            if self.horses[index].__class__.__name__ == horse_type and self.horses[index].is_taken is False:
                current_horse.append(self.horses[index])
                break

        if not current_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        current_jockey = list(filter(lambda j: j.name == jockey_name, self.jockeys))[0]

        if current_jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        current_horse[0].is_taken = True
        current_jockey.horse = current_horse[0]
        return f"Jockey {jockey_name} will ride the horse {current_horse[0].name}."

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        available_race_types = [x.race_type for x in self.horse_races]
        if race_type not in available_race_types:
            raise Exception(f"Race {race_type} could not be found!")

        all_jockeys = [j.name for j in self.jockeys]
        if jockey_name not in all_jockeys:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        current_jockey = list(filter(lambda j: j.name == jockey_name, self.jockeys))[0]

        if current_jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        current_race = list(filter(lambda r: r.race_type == race_type, self.horse_races))[0]

        for jokey in current_race.jockeys:
            if jokey.name == jockey_name:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."

        current_race.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        available_race_types = [x.race_type for x in self.horse_races]
        if race_type not in available_race_types:
            raise Exception(f"Race {race_type} could not be found!")

        current_race = list(filter(lambda r: r.race_type == race_type, self.horse_races))[0]

        if len(current_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_horse = None
        winner_jockey = None
        highest_speed = 0

        for player in current_race.jockeys:
            current_horse = player.horse
            if current_horse.speed > highest_speed:
                highest_speed = current_horse.speed
                winner_horse = current_horse
                winner_jockey = player

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h " \
               f"is {winner_jockey.name}! Winner's horse: {winner_horse.name}."

