def even_odd():
    value = "even"
    while True:
        yield value
        if value == "even":
            value = "odd"
        else:
            value = "even"

parity = even_odd()
for a in range(10):
    print(parity.__next__())