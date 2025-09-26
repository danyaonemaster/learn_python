from task_04_10_document import *


def test_pdf_word_class(capsys):
    pdf = Pdf("book.pdf")

    pdf.open()

    word = Word("Doha.docx")

    word.open()

    res = capsys.readouterr().out.strip()

    assert res == f"Opening PDF file: {pdf.filename} with a PDF reader.\nOpening Word file: {word.filename} with Microsoft Word."