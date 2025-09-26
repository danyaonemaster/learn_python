from task_02_02_timer import Timer


def test_timer_class():

    timer = Timer()

    for _ in range(100):
        timer.tick()

    assert timer.seconds == 100

