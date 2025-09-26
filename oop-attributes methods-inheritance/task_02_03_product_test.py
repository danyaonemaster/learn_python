from task_02_03_product import Product

def test_product_class():
    milk = Product("milk", 120)

    milk.apply_discount()

    assert milk.price == 120 * 0.99


