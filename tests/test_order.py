import pytest
from pages.order_page import OrderPage


class TestOrder:

    @pytest.mark.parametrize("order_button_position", ["top", "bottom"])
    @pytest.mark.parametrize(
        "name,surname,address,metro,phone,date,rent_period,color",
        [
            ("Мария", "Пономарева", "ул. Ленина, 1", "Сокольники", "+79161234567", "01.03.2026", "двое суток", "чёрный жемчуг"),
            ("Иван", "Иванов", "ул. Пушкина, 10", "Красносельская", "+79261234567", "02.03.2026", "двое суток", "чёрный жемчуг"),
        ]
    )
    def test_order_flow(
        self,
        driver,
        order_button_position,
        name,
        surname,
        address,
        metro,
        phone,
        date,
        rent_period,
        color
    ):
        page = OrderPage(driver)
        page.open()

        if order_button_position == "top":
            page.click_order_top()
        else:
            page.click_order_bottom()

        page.fill_step1(name, surname, address, metro, phone)
        page.fill_step2(date, rent_period, color)
        page.confirm_order()

        assert page.is_order_successful(), "Заказ не был оформлен"
