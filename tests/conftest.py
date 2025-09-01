import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.myiter import MyIter
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product_phone():
    return Product("Samsung", "You can call your friends", 100000.0, 4)


@pytest.fixture
def category_phones():
    return Category(
        "Phones",
        "You can call your friends",
        [
            Product("Samsung", "Has Android OS", 150000.0, 5),
            Product("Apple", "Has IOS", 190000.0, 2),
            Product("Xiaomi", "Has HyperOS", 70000.0, 8),
        ],
    )


@pytest.fixture
def category_tvs():
    return Category(
        "TVs",
        "You can watch propaganda",
        [
            Product("Samsung OLED", "It is a Smart TV", 150000.0, 5),
            Product("Apple TV", "Model number A2737", 190000.0, 2),
        ],
    )


@pytest.fixture
def products_list():
    return [
        Product("Samsung", "Has Android OS", 150000.0, 5),
        Product("Apple", "Has IOS", 190000.0, 2),
        Product("Xiaomi", "Has HyperOS", 70000.0, 8),
    ]


@pytest.fixture
def category_iterator(category_phones):
    return MyIter(category_phones)


@pytest.fixture
def product_phone2():
    return Product("Samsung", "Has Android OS", 150000.0, 5)


@pytest.fixture
def smartphone1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def lawngrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_headphones():
    return Category

@pytest.fixture
def category_without_products():
    return Category("Пустая категория", "Категория без продуктов", [])
