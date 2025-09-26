class Animal:
    def __init__(self, name, sound = None):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.sound}")


class Cat(Animal):
    def meow(self):
        print("meow")
