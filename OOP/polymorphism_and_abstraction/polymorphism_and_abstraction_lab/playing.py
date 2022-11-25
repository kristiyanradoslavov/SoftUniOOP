def start_playing(instance):
    return instance.play()


class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))
