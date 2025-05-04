def get_infinite_square_generator():
    number = 1
    while True:
        yield number**2
        number +=1
a = 1
infinite_square_generator = get_infinite_square_generator()
while a <= 10:
    print(infinite_square_generator.__next__())
    a += 1