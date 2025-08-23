def test_init(product_phone):
    assert product_phone.name == "Samsung"
    assert product_phone.description == "You can call your friends"
    assert product_phone.price == 100000.0
    assert product_phone.quantity == 4
