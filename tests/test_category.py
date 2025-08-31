import pytest
from src.product import Product
from src.smartphone import Smartphone


def test_init(category_phones, category_tvs):
    assert category_phones.name == "Phones"
    assert category_phones.description == "You can call your friends"

    assert category_phones.category_count == 2
    assert category_tvs.category_count == 2

    assert category_phones.product_count == 5
    assert category_tvs.product_count == 5


def test_add_product(product_phone, smartphone1, category_phones):

    assert type(product_phone) == Product
    assert type(smartphone1) == Smartphone
    assert type(4) == int

    assert len([prod for prod in category_phones.products.split('\n')]) == 3
    category_phones.add_product(product_phone)
    assert len([prod for prod in category_phones.products.split('\n')]) == 4
    category_phones.add_product(smartphone1)
    assert len([prod for prod in category_phones.products.split('\n')]) == 5

    with pytest.raises(TypeError):
        category_phones.add_product('String')




def test_products(category_tvs):
    assert (
        category_tvs.products == "Samsung OLED, 150000.0 руб. Остаток: 5 шт.\nApple TV, 190000.0 руб. Остаток: 2 шт."
    )


def test_category_str(category_tvs):
    assert str(category_tvs) == "TVs, количество продуктов: 7"
