from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / cls.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for idx, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {idx + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        delimiter = "-" * 11 + "\n"
        result = delimiter
        for page in self.photos:
            result += " ".join(["[]" for _ in page]) + "\n" + delimiter

        return result

