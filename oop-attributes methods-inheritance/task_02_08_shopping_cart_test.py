from task_02_08_shopping_cart import ShoppingCart


def test_shopping_cart_class():
    shopping_cart = ShoppingCart({"phone": 120, "cpu": 100})

    assert shopping_cart.total_price() == 220
