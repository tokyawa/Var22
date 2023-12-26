from abc import ABC, abstractmethod
import unittest

# Тест для Фабричного метода
class TestFactoryMethod(unittest.TestCase):
    def test_product_creation(self):
        # Создаем магазин книг и проверяем создание книги
        book_store = BookStore()
        book_product = book_store.create_product()
        self.assertIsInstance(book_product, Book)
        self.assertEqual(book_product.display_info(), "Book: 1984 by George Orwell")

        # Создаем магазин электроники и проверяем создание электронного устройства
        electronics_store = ElectronicsStore()
        electronics_product = electronics_store.create_product()
        self.assertIsInstance(electronics_product, ElectronicDevice)
        self.assertEqual(electronics_product.display_info(), "Electronic Device: Apple Smartphone")


# Продукт - Товар в интернет-магазине
class Product(ABC):
    @abstractmethod
    def display_info(self):
        pass

# Конкретный продукт - Книга
class Book(Product):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Book: {self.title} by {self.author}"

# Конкретный продукт - Электронное устройство
class ElectronicDevice(Product):
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def display_info(self):
        return f"Electronic Device: {self.brand} {self.name}"

# Создатель - Интернет-магазин
class OnlineStore(ABC):
    @abstractmethod
    def create_product(self):
        pass

    def sell_product(self):
        product = self.create_product()
        result = f"{self.store_type} sold: {product.display_info()}"
        return result

# Конкретный создатель - Интернет-магазин книг
class BookStore(OnlineStore):
    store_type = "BookStore"

    def create_product(self):
        return Book("1984", "George Orwell")

# Конкретный создатель - Интернет-магазин электронных устройств
class ElectronicsStore(OnlineStore):
    store_type = "ElectronicsStore"

    def create_product(self):
        return ElectronicDevice("Smartphone", "Apple")

# Использование
book_store = BookStore()
book_result = book_store.sell_product()
print(book_result)

electronics_store = ElectronicsStore()
electronics_result = electronics_store.sell_product()
print(electronics_result)

# Запуск тестов
if __name__ == "__main__":
    unittest.main()