from OOP.first_steps_in_oop.first_steps_in_oop_exercise.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, current_pokemon):
        poke_info = current_pokemon.pokemon_details().split()
        if {poke_info[0]: poke_info[-1]} not in self.pokemons:
            self.pokemons.append({poke_info[0]: poke_info[-1]})
            return f"Caught {current_pokemon.pokemon_details()}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, name):
        for i in range(len(self.pokemons)):
            if name in self.pokemons[i]:
                self.pokemons.remove(self.pokemons[i])
                return f"You have released {name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        final_result = []
        final_result.append(f"Pokemon Trainer {self.name}")
        final_result.append(f"Pokemon count {len(self.pokemons)}")
        for i in self.pokemons:
            for key, value in i.items():
                current_poke = Pokemon(key, value)
                final_result.append(f"- {current_poke.pokemon_details()}")

        return "\n".join(final_result)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
