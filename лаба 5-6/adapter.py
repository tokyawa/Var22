from abc import ABC, abstractmethod
import unittest
from unittest.mock import MagicMock

# Тест для Адаптера
class TestAdapter(unittest.TestCase):
    def test_payment_adapter(self):
        # Создаем Mock-объект для первого стороннего сервиса
        service_mock_1 = MagicMock()
        service_mock_1.process_payment.return_value = "Payment processed by Service 1"

        # Создаем Mock-объект для второго стороннего сервиса
        service_mock_2 = MagicMock()
        service_mock_2.make_payment.return_value = "Payment processed by Service 2"

        # Используем Mock-объекты в адаптерах
        adapter_1 = PaymentAdapter(service_mock_1, "process_payment")
        adapter_2 = PaymentAdapter(service_mock_2, "make_payment")

        # Проверяем вызовы методов через адаптеры
        self.assertEqual(adapter_1.process_payment(), "Processed via Adapter: Payment processed by Service 1")
        service_mock_1.process_payment.assert_called_once()

        self.assertEqual(adapter_2.process_payment(), "Processed via Adapter: Payment processed by Service 2")
        service_mock_2.make_payment.assert_called_once()

# Целевой интерфейс нашей системы платежей
class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self):
        pass

# Адаптер для интеграции сторонних сервисов с нашей системой
class PaymentAdapter(PaymentSystem):
    def __init__(self, third_party_service, method_name):
        self.third_party_service = third_party_service
        self.method_name = method_name

    def process_payment(self):
        method = getattr(self.third_party_service, self.method_name)
        return f"Processed via Adapter: {method()}"

# Использование
# Представление двух различных сторонних сервисов
class ThirdPartyService1:
    def process_payment(self):
        return "Payment processed successfully by Service 1"

class ThirdPartyService2:
    def make_payment(self):
        return "Payment processed successfully by Service 2"

service1 = ThirdPartyService1()
service2 = ThirdPartyService2()

adapter1 = PaymentAdapter(service1, "process_payment")
adapter2 = PaymentAdapter(service2, "make_payment")

print(adapter1.process_payment())
print(adapter2.process_payment())

# Запуск тестов
if __name__ == '__main__':
    unittest.main()