class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


class Timer:
    def __init__(self, timer):
        self.timer = timer

    def reset(self):
        self.timer = 0

    def tick(self):
        self.timer += 1


class Product:
    def __init__(self, prise):
        self.price = prise

    def apply_discount(self):
        self.price = self.price * 0.01


class TodoList:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(task)

    def show_tasks(self):
        for task in self.todos:
            print(task)


class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello " + self.name)


class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 9 / 5) + 32


class DogL:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Bark")


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def total_price(self):
        return sum(item['price'] for item in self.items)


class Door:
    def __init__(self):
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False


class Account:
    def transfer_to(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def transfer_from(self, other_account, amount):

        if self.owner == other_account:
            self.balance -= amount
            other_account.balance -= amount

