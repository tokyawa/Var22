from abc import ABC, abstractmethod
import unittest
from unittest.mock import Mock

# Наблюдатель
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Субъект - Корзина покупок
class ShoppingCart:
    def __init__(self):
        self._observers = []
        self._items = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

    def add_item(self, item):
        self._items.append(item)
        self.notify_observers(f"Товар добавлен: {item}")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            self.notify_observers(f"Товар удален: {item}")

    def display_items(self):
        return self._items

# Конкретный наблюдатель - Клиент магазина
class Customer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} получил/а уведомление! {message}")

# Тест для Наблюдателя
cart = ShoppingCart()

customer1 = Customer("Никита")
customer2 = Customer("Екатерина")

# Добавляем клиентов в качестве наблюдателей
cart.add_observer(customer1)
cart.add_observer(customer2)

# Добавляем товары в корзину
cart.add_item("Баскетбольный мяч")
cart.add_item("Ноутбук")

# Удаляем товар из корзины
cart.remove_item("Ноутбук")

# Отображаем текущие товары в корзине
print("Товар в корзине:", cart.display_items())