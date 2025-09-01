from src.product import Product


class LawnGrass(Product):
    """
    Attributes:
        country (str): страна-производитель
        germination_period (str): срок прорастания
        color (str): цвет
    """

    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """
        Инициализирует экземпляр травы газонной.

        :param name: название травы газонной
        :param description: описание
        :param price: цена
        :param quantity: количество
        :param country: страна-производитель
        :param germination_period: срок прорастания
        :param color: цвет
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
