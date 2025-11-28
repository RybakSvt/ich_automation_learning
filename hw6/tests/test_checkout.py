from ..pages.login_page import LoginPage
from ..pages.cart_page import CartPage
from ..pages.checkout_page import CheckoutPage
from ..pages.inventory_page import InventoryPage


class TestCheckout:
    def test_checkout_total_price(self, driver):  # driver из conftest.py
        """
        Тест проверяет итоговую стоимость заказа после добавления товаров в корзину
        """
        # Инициализация Page Objects
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # 1. Открытие сайта и авторизация
        login_page.login_as_standard_user()

        # 2. Добавление товаров в корзину
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")

        # 3. Переход в корзину
        inventory_page.go_to_cart()

        # 4. Начало оформления заказа
        cart_page.proceed_to_checkout()

        # 5. Заполнение формы данными
        checkout_page.fill_checkout_form("Svitlana", "Rybak", "12345")
        checkout_page.click_continue()

        # 6. Проверка итоговой стоимости
        total_price = checkout_page.get_total_price()

        # 7. Проверка утверждения
        assert total_price == "$58.29", f"Ожидалась сумма $58.29, но получено {total_price}"

        print(f"Тест пройден! Итоговая стоимость: {total_price}")