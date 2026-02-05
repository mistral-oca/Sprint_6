import pytest
from pages.order_page import OrderPage

# ---------- Тестовые данные ----------
test_data = [
    # формат: name, surname, address, metro, phone, date, rent_period, color
    ("Мария", "Пономарева", "ул. Ленина, 1", "Сокольники", "+79161234567", "01.03.2026", "двое суток", "чёрный жемчуг"),
    ("Иван", "Иванов", "ул. Пушкина, 10", "Красносельская", "+79261234567", "02.03.2026", "двое суток", "чёрный жемчуг")
]

# ---------- Параметризация кнопки заказа ----------
@pytest.mark.parametrize("order_button_position", ["top", "bottom"])
@pytest.mark.parametrize("name,surname,address,metro,phone,date,rent_period,color", test_data)
def test_order_flow(driver, order_button_position, name, surname, address, metro, phone, date, rent_period, color):
    """Позитивный сценарий: заказ через верхнюю или нижнюю кнопку"""
    page = OrderPage(driver)
    page.open()

    # ---------- Клик по нужной кнопке ----------
    if order_button_position == "top":
        page.click_order_top()
    else:
        page.click_order_bottom()

    # ---------- Шаг 1: данные клиента ----------
    page.fill_step1(name, surname, address, metro, phone)

    # ---------- Шаг 2: детали заказа + кнопка "Заказать" ----------
    page.fill_step2(date, rent_period, color)

    # ---------- Подтверждение заказа на баннере ----------
    page.confirm_order()

    # ---------- Проверка успешного заказа ----------
    assert page.is_order_successful(), "Заказ не был оформлен"

    
