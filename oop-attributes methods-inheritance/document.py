class Document:
    def __init__(self, filename):
        self.filename = filename

    def open(self):
        raise NotImplementedError()

class PDF(Document):
    def open(self):
        print(f"Opening PDF file: {self.filename} with a PDF reader.")

class Word(Document):
    def open(self):
        print(f"Opening Word file: {self.filename} with Microsoft Word.")