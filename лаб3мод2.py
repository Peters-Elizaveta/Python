class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    def name(self):
        return self._name

    def author(self):
        return self._author

    def __str__(self):
        return f"Book: {self.name} by {self.author}"

    def __repr__(self):
        return f"Book(name='{self.name}', author='{self.author}')"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self._pages = pages

    def pages(self):
        return self._pages

    def __str__(self):
        return f"PaperBook: {self.name} by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"PaperBook(name='{self.name}', author='{self.author}', pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self._duration = duration

    def duration(self):
        return self._duration

    def __str__(self):
        return f"AudioBook: {self.name} by {self.author}, duration: {self.duration} hours"

    def __repr__(self):
        return f"AudioBook(name='{self.name}', author='{self.author}', duration={self.duration})"