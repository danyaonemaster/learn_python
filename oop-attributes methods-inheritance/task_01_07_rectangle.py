class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @classmethod
    def from_square(cls, size):
        return cls(size, size)