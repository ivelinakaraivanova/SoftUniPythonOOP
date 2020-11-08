class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count//4)

    def add_photo(self, label: str):
        for i, p in enumerate(self.photos):
            if len(p) < 4:
                p.append(label)
                return f"{label} photo added successfully " \
                       f"on page {i + 1} slot {len(p)}"
        return "No more free spots"

    def display(self):
        result = f"{'-' * 11}\n"
        for page in self.photos:
            result += f"{('[] ' * len(page)).rstrip()}\n"
            result += f"{'-' * 11}\n"
        return result


album = PhotoAlbum(4)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())