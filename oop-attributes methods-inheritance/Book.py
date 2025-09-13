class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f'{self.author}: {self.title}')

    @classmethod
    def from_string(cls, book_str):
        list_ = book_str.split(' - ')
        book = cls(list_[1], list_[0])

