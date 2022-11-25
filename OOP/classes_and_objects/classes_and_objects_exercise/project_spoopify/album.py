from OOP.classes_and_objects.classes_and_objects_exercise.project_spoopify.band import Band
from OOP.classes_and_objects.classes_and_objects_exercise.project_spoopify.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.args = args # check if this should be named differently
        self.published = False
        self.songs = []
        self.check_songs()

    def add_song(self, current_song):
        if current_song.single:
            return f"Cannot add {current_song.name}. It's a single"

        elif self.published:
            return f"Cannot add songs. Album is published."

        elif current_song in self.songs:
            return "Song is already in the album."

        self.songs.append(current_song)
        return f"Song {current_song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."

        try:
            current_song = next(filter(lambda x: song_name == x.name, self.songs))
            self.songs.remove(current_song)
            return f"Removed song {current_song.name} from album {self.name}."

        except StopIteration:
            return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):
        final_result = [f"Album {self.name}"]
        for i in self.songs:
            final_result.append(f"== {i.get_info()}")

        return '\n'.join(final_result)

    def check_songs(self):
        if self.args:
            for i in self.args:
                self.songs.append(i)


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
