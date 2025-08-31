from src.category import Category


def test_init(category_phones, category_tvs):
    assert category_phones.name == "Phones"
    assert category_phones.description == "You can call your friends"

    assert category_phones.category_count == 2
    assert category_tvs.category_count == 2

    assert category_phones.product_count == 5
    assert category_tvs.product_count == 5


def test_add_product(category_phones, product_phone):
    category_phones.add_product(product_phone)
    assert Category.product_count == 9


def test_products(category_tvs):
    assert (
        category_tvs.products == "Samsung OLED, 150000.0 руб. Остаток: 5 шт.\nApple TV, 190000.0 руб. Остаток: 2 шт."
    )


def test_category_str(category_tvs):
    assert str(category_tvs) == "TVs, количество продуктов: 7"
