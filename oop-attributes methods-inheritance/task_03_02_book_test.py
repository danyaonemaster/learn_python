from task_01_05_book import Book


def test_book_class():
    book = Book.from_string("Goha - Black")

    assert isinstance(book, Book)
    assert book.title == "Black"
    assert book.author == "Goha"
