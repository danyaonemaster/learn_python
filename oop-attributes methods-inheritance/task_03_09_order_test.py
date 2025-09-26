from task_03_09_order import Order


def test_order_class():
    order = Order.from_dict({"price": 10, "quantity": 3})

    assert order.quantity == 3
    assert order.price == 10