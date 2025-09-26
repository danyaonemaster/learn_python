from task_04_09_transport import *


def test_plane_ship(capsys):
    ship = Ship("keril")

    ship.sail()

    plane = Plane("jorj")

    plane.fly()

    res = capsys.readouterr().out.strip()

    assert res == f"{ship.name} is sailing on the water!\n{plane.name} is flying in the sky!"
