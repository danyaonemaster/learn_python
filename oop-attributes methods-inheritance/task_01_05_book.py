class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f'{self.author}: {self.title}'

    @classmethod
    def from_string(cls, book_str):
        author, title = book_str.split(' - ')
        return cls(title, author)

