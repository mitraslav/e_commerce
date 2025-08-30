from src.product import Product


class Category:
    """Класс отслеживает общее количество категорий и товаров во всех категориях,
    а также предоставляет методы для работы с товарами конкретной категории.

    Attributes:
        name (str): Название категории
        description (str): Описание категории
        category_count (int): Счетчик общего количества созданных категорий (классовый атрибут)
        product_count (int): Счетчик общего количества товаров во всех категориях (классовый атрибут)
    """

    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализирует экземпляр категории товаров.

        Args:
            name (str): Название категории
            description (str): Описание категории
            products (list): Список объектов товаров (класс Product), принадлежащих категории
        """
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """

        :return: Строка о категории следующего вида: 'Название категории, количество продуктов: 200 шт.'
        """
        return f'{self.name}, количество продуктов: {self.product_count}'


    def add_product(self, product: Product):
        """Добавляет товар в категорию.
        Args:
            product(Product): Объект товара для добавления в категорию

        Increases:
            Увеличивает общий счетчик товаров (product_count) на 1
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает форматированную строку с информацией о товарах категории.

        Returns:
            str: Строка с информацией о каждом товаре в формате: '<Название продукта>, <цена продукта> руб. Остаток: <количество>.'
                Каждый товар на отдельной строке.
        """
        product_list = []
        for product in self.__products:
            product_list.append(str(product))
        return "\n".join(product_list)
