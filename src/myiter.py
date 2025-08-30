from src.category import Category

class MyIter:
    """Вспомогательный класс, с помощью которого можно перебирать товары одной категории
    Attributes:
        category (Category): Объект категории, содержащей товары
        index (int): Текущий индекс для итерации
    """
    def __init__(self, category: Category):
        """
        Инициализирует экзем
        :param category: Категория товаров, по которой будет производиться итерация
        """
        self.category = category
        self.index = 0

    def __iter__(self):
        """
        Возвращает сам объект итератора.
        :return: MyIter: Текущий объект итератора со сброшенным индексом
        """
        self.index = 0
        return self

    def __next__(self):
        """
        Возвращает следующий товар из категории.
        :return: (str) Строка с описанием следующего товара

        Raises:
            StopIteration: Когда все товары в категории были перебраны
        """
        product_list = self.category.products.split('\n')
        if self.index < len(product_list):
            product = product_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration