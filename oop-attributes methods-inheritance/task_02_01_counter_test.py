from task_02_01_counter import Counter


def test_counter():
    counter = Counter()

    for _ in range(10):
        counter.increment()

    assert counter.count == 10
