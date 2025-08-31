import pytest


def test_myiter(category_iterator):
    assert category_iterator.index == 0
    assert next(category_iterator) == "Samsung, 150000.0 руб. Остаток: 5 шт."
    assert next(category_iterator) == "Apple, 190000.0 руб. Остаток: 2 шт."
    assert next(category_iterator) == "Xiaomi, 70000.0 руб. Остаток: 8 шт."

    with pytest.raises(StopIteration):
        next(category_iterator)
