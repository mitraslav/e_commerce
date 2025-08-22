import pytest
from src.product import Product
from src.category import Category

@pytest.fixture
def product_phone():
    return Product('Samsung', 'You can call your friends', 100000.0, 4)

@pytest.fixture
def category_phones():
    return Category('Phones', 'You can call your friends', [Product('Samsung', 'Has Android OS', 150000.0, 5),
                                                            Product('Apple', 'Has IOS', 190000.0, 2),
                                                            Product('Xiaomi', 'Has HyperOS', 70000.0, 8)])
@pytest.fixture
def category_tvs():
    return Category('TVs', 'You can watch propaganda', [Product('Samsung OLED', 'It is a Smart TV', 150000.0, 5),
                                                        Product('Apple TV', 'Model number A2737', 190000.0, 2)])