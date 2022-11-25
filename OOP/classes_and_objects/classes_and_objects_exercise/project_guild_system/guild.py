from OOP.classes_and_objects.classes_and_objects_exercise.project_guild_system.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, current_player):
        current_name = current_player.name
        current_guild = current_player.guild

        if current_player in self.players:
            return f"Player {current_name} is already in the guild."
        elif current_guild != "Unaffiliated":
            return f"Player {current_name} is in another guild."

        self.players.append(current_player)
        current_player.guild = self.name
        return f"Welcome player {current_name} to the guild {self.name}"

    def kick_player(self, player_name):
        try:
            current_player = next(filter(lambda x: player_name == x.name, self.players))
            self.players.remove(current_player)
            current_player.guild = "Unaffiliated"
            return f"Player {current_player.name} has been removed from the guild."

        except StopIteration:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        final_result = [f"Guild: {self.name}"]
        for i in self.players:
            final_result.append(i.player_info())

        return "\n".join(final_result)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())

