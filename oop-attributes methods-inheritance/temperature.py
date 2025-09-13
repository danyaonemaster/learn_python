class Temperature():
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        self.temperature = (self.temperature * 9/5) + 32

    @classmethod
    def from_fahrenheit(cls, f):
        temperature = float(f) - 32
        return cls(temperature)