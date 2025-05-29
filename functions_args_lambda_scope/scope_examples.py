# Task 1
def test_scope():
    x = 10
    print(x)

# Task 2
counter = 0

def increment():
    global counter
    counter += 1

#Task 3
def outer_nonlocal():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    return x

#Task 4
global_value = 5

def conflict_names():
    global global_value
    local_value = 10
    return global_value, local_value

#Task 5
def mutate_list():
    lst = [1, 2, 3]
    def add_item(l):
        l.append(4)
    add_item(lst)
    return lst

#Task 6
def lambda_scope(x):
    outer_x = 5
    func = lambda y, val=outer_x: y + val
    outer_x = 10
    return func(x)

