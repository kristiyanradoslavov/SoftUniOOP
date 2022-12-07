class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def get_all_supplies_per_specific_type(self, type):
        final_result = []
        for supply_idx in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[supply_idx].__class__.__name__ == type:
                final_result.append(self.supplies[supply_idx])
                self.supplies.pop(supply_idx)
                break

        return final_result

    def add_player(self, *args):
        existing_players = [p.name for p in self.players]
        new_players_names = []
        for player in args:
            if (player.name not in existing_players) and player.name not in new_players_names:
                self.players.append(player)
                new_players_names.append(player.name)

        return f"Successfully added: {', '.join(new_players_names)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name, sustenance_type):
        player_inst = [p for p in self.players if p.name == player_name]
        if sustenance_type == "Food" or sustenance_type == "Drink":
            if player_inst:
                if player_inst[0].need_sustenance is False:
                    return f"{player_name} have enough stamina."

                supply_result = self.get_all_supplies_per_specific_type(sustenance_type)
                if not supply_result and sustenance_type == "Food":
                    raise Exception("There are no food supplies left!")
                elif not supply_result and sustenance_type == "Drink":
                    raise Exception("There are no drink supplies left!")

                if player_inst[0].stamina + supply_result[0].energy < 100:
                    player_inst[0].stamina += supply_result[0].energy
                else:
                    player_inst[0].stamina = 100

                return f"{player_name} sustained successfully with {supply_result[0].name}."

    def duel(self, first_player_name, second_player_name):
        f_player_instance = [p for p in self.players if p.name == first_player_name][0]
        s_player_instance = [b for b in self.players if b.name == second_player_name][0]

        if f_player_instance.stamina <= 0 and s_player_instance.stamina <= 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."

        elif f_player_instance.stamina <= 0:
            return f"Player {first_player_name} does not have enough stamina."

        elif s_player_instance.stamina <= 0:
            return f"Player {second_player_name} does not have enough stamina."

        if f_player_instance.stamina < s_player_instance.stamina:
            first = f_player_instance
            second = s_player_instance
        else:
            first = s_player_instance
            second = f_player_instance

        attacker_value = first.stamina / 2

        winner = []
        if second.stamina - attacker_value <= 0:
            second.stamina = 0
            winner.append(first.name)
        else:
            second.stamina -= attacker_value

        defender_value = second.stamina / 2

        if first.stamina - defender_value <= 0:
            first.stamina = 0
            winner.append(second.name)
        else:
            first.stamina -= defender_value

        if winner:
            return f"Winner: {winner[0]}"

        else:
            if first.stamina > second.stamina:
                return f"Winner: {first.name}"
            else:
                return f"Winner: {second.name}"

    def next_day(self):
        for player in self.players:
            result = player.age * 2
            if player.stamina - result <= 0:
                player.stamina = 0
            else:
                player.stamina -= result

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        final_result = []

        for player in self.players:
            final_result.append(str(player))

        for supply in self.supplies:
            final_result.append(supply.details())

        return '\n'.join(final_result)
