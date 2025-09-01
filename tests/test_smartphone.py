import pytest


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Iphone 15"
    assert smartphone1.description == "512GB, Gray space"
    assert smartphone1.price == 210000.0
    assert smartphone1.quantity == 8

    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == "15"
    assert smartphone1.memory == 512
    assert smartphone1.color == "Gray space"


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 2114000.0

    with pytest.raises(TypeError):
        smartphone1 + "String"
