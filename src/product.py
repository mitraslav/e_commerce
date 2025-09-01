from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для представления товара в интернет-магазине.

    Attributes:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара
        quantity (int): Количество товара на складе
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализирует экземпляр товара.

        Args:
            name (str): Название товара
            description (str): Описание товара
            price (float): Цена товара. Должна быть положительной
            quantity (int): Количество товара на складе. Неотрицательное значение

        Note:
            Цена валидируется через setter свойства price
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        """

        :return: строка с информацией о продукте формата Название продукта, 80 руб. Остаток: 15 шт.
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """

        :param other: Другой объект класса Product
        :return: Сумма произведения стоимостей товара и их количества
        """
        if type(self) is not type(other):
            raise TypeError("Продукты должны быть одинакового класса!")
        return self.__price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None):
        """Создает новый товар или обновляет существующий с таким же названием.

            Если товар с таким названием уже существует в переданном списке:
            - Увеличивает количество существующего товара
            - Обновляет цену, если новая цена выше текущей

            Args:
                product_data (dict): Словарь с данными товара. Должен содержать ключи:
                    - 'name': название товара
                    - 'description': описание товара
                    - 'price': цена товара
                    - 'quantity': количество товара
                products_list (list, optional): Список существующих товаров для проверки дубликатов

            Returns:
                Product: Новый объект товара или обновленный существующий товар
            Raises:
        KeyError: Если в product_data отсутствуют обязательные ключи
        """

        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if products_list:
            for existing_product in products_list:
                if existing_product.name == name:
                    existing_product.quantity += quantity
                    if price > existing_product.price:
                        existing_product.price = price
                    return existing_product
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """float: Возвращает цену товара.

        Getter для получения текущей цены товара.
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """Устанавливает новую цену товара с валидацией.

            Валидирует новую цену и запрашивает подтверждение при понижении цены.

            Args:
                new_price (float): Новая цена товара

            Rules:
                - Цена не может быть ≤ 0
                - При понижении цены требуется подтверждение пользователя
                - Повышение цены применяется автоматически
            Behavior:
        - При невалидной цене выводит сообщение об ошибке
        - При понижении цены запрашивает подтверждение через консоль
        - При подтверждении применяет новую цену
        - При отмене оставляет старую цену
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirmation = input(f"Цена понижается с {self.__price} до {new_price}. Подтвердите действие (y/n): ")
            if confirmation.lower() == "y":
                self.__price = new_price
                print("Цена успешно изменена")
            else:
                print("Изменение цены отменено")
        else:
            self.__price = new_price
