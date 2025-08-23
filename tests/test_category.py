def test_init(category_phones, category_tvs):
    assert category_phones.name == "Phones"
    assert category_phones.description == "You can call your friends"

    assert category_phones.category_count == 2
    assert category_tvs.category_count == 2

    assert category_phones.product_count == 5
    assert category_tvs.product_count == 5
