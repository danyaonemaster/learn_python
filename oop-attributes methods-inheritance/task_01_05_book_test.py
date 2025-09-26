from task_01_05_book import Book

def test_book_class():
    book = Book('Doctor Who', 'Justin Richards')

    assert book.info() == 'Justin Richards: Doctor Who'

