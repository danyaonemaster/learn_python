def sum_all(*args):
    return sum(args)

def print_args(*args):
    for argument in args:
        print(argument)

def print_kwargs(**kwargs):
    for key, argument in kwargs.items():
        print(f"{key}: {argument}")

def show_all(*args, **kwargs):
    print_args(*args)
    print_kwargs(**kwargs)

def describe_person(**kwargs):
    if "name" and "age" in kwargs.keys():
        print(f"Name: {kwargs.get("name")}\n"
              f"Age: {kwargs.get("age")}")
    else:
        print("There are no such keys")

def sum_numbers(*args, **kwargs):
    num_sum = 0

    for item in args:
        if type(item) == int:
            num_sum += item

    for key, value in kwargs.items():
        if  type(value) == int:
            num_sum += value

    return num_sum


print(sum_all(10, 5, 2))

print_args("Goha", 10, "Niga")
print_kwargs(first=10, second= 4)
show_all(10, 23, first= 3, second= 4)
describe_person(name="Goha")
print(sum_numbers(10, 2, "Goha", first= 3, second= "Niga"))