from src.product import Product
import pytest

def test_init(product_phone):
    assert product_phone.name == "Samsung"
    assert product_phone.description == "You can call your friends"
    assert product_phone.price == 100000.0
    assert product_phone.quantity == 4
    with pytest.raises(ValueError, match='Товар с нулевым или отрицательным количеством не может быть добавлен'):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_new_product(product_phone, products_list):
    exist_prod = Product.new_product(
        {
            "name": product_phone.name,
            "description": product_phone.description,
            "price": product_phone.price,
            "quantity": product_phone.quantity,
        },
        products_list,
    )
    assert exist_prod.quantity == 9
    assert exist_prod.price == 150000.0
    assert exist_prod.description != "You can call your friends"
    assert exist_prod.description == "Has Android OS"

    expensive_prod = Product.new_product(
        {"name": "Apple", "description": "Hello", "price": 250000.0, "quantity": 3}, products_list
    )

    assert expensive_prod.price == 250000.0
    assert expensive_prod.quantity == 5
    assert expensive_prod.description != "Hello"
    assert expensive_prod.description == "Has IOS"

    new_prod = Product.new_product(
        {"name": "Galaxy", "description": "Samsung but more expensive", "price": 122000.0, "quantity": 4},
        products_list,
    )

    assert new_prod.price == 122000.0
    assert new_prod.quantity == 4
    assert new_prod.description == "Samsung but more expensive"
    assert new_prod.name == "Galaxy"


def test_product_price_property(product_phone):
    assert product_phone.price == 100000.0


def test_price_setter(product_phone):
    product_phone.price = 0
    assert "Цена не должна быть нулевая или отрицательная"
    product_phone.price = -20
    assert "Цена не должна быть нулевая или отрицательная"


def test_product_str(product_phone):
    assert str(product_phone) == "Samsung, 100000.0 руб. Остаток: 4 шт."


def test_product_add(product_phone, product_phone2):
    assert product_phone + product_phone2 == 1150000.0
