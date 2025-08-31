from src.product import Product

class Smartphone(Product):
    """
    Attributes:
        efficiency (float): производительность
        model (str): модель
        memory (int): объем встроенной памяти
        color (str): цвет
    """
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """
        Инициализирует экземпляр смартфона.

        :param name: название телефона
        :param description: описание
        :param price: цена
        :param quantity: количество
        :param efficiency: производительность
        :param model: модель
        :param memory: объем встроенной памяти
        :param color: цвет
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color