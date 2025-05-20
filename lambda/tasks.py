from functools import reduce

def make_multiplier(n):
    return lambda x: x * n

# Task 1
square_number = lambda x: x * x
print(f"Task 1: {square_number(5)}")

#Task 2
is_even = lambda x: x % 2 == 0
number_list = [10, 5, 23, 4, 5]

print(f"Task 2: {list(filter(is_even, number_list))}")

# Task 3
double = lambda x: x * 2

print(f"Task 3: {list(map(double, number_list))}")

# Task 4
users = [{'name': 'Tom', 'age': 25}, {'name': 'Ann', 'age': 20}]
sorted_users = sorted(users, key=lambda user: user["age"])

print(f"Task 4: {sorted_users}")

#Task 5
triple = make_multiplier(3)

print(f"Task 5: {triple(4)}")

#Task 6
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x + y, numbers)

print(f"Task 6: {product}")

