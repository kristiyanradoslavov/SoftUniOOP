from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for x in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label):

        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                page_num = page + 1
                slot_num = len(self.photos[page])
                return f"{label} photo added successfully on page {page_num} slot {slot_num}"

        else:
            return "No more free slots"

    def display(self):
        result = ["-----------"]
        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append("-----------")

        return '\n'.join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
