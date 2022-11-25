class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, current_album):
        if current_album in self.albums:
            return f"Band {self.name} already has {current_album.name} in their library."

        self.albums.append(current_album)
        return f"Band {self.name} has added their newest album {current_album.name}."

    def remove_album(self, album_name):
        try:
            current_album = next(filter(lambda x: album_name == x.name, self.albums))
            if current_album.published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(current_album)
            return f"Album {album_name} has been removed."

        except StopIteration:
            return f"Album {album_name} is not found."

    def details(self):
        final_result = [f"Band {self.name}"]
        for i in self.albums:
            final_result.append(i.details())

        return '\n'.join(final_result)

