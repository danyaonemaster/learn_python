# Task 1
def greet():
    print("Hello world!")
# Task 2
def square(x):
    return x * x
# Task 3
def add(a, b):
    return a + b

# Task 4
def repeat(message, times= 2):
    print(f"Task 4: {message * times}")

# Task 5
def operations(a, b):
    return a + b, a - b, a * b

# Task 6
def calculate_and_print(x, y):
    print(f"Task 6: {add(x, y)}")


greet()
print(f"Task 2: {square(2)}")
print(f"Task 3: {add(2,3)}")
repeat("Black")
print(f"Task 5: {operations(4,2)}")
calculate_and_print(2, 5)


