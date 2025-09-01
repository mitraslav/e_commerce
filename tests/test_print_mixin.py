from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Samsung", "You can call your friends", 100000.0, 4)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung, You can call your friends, 100000.0, 4)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message_2 = capsys.readouterr()
    assert message_2.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message_3 = capsys.readouterr()
    assert message_3.out.strip() == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)"
