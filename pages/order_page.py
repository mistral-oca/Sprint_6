from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import L

class OrderPage:
    URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------- Вспомогательные методы ----------

    def open(self):
        """Открываем страницу и закрываем баннер cookies, если есть"""
        self.driver.get(self.URL)
        self.close_cookie()

    def close_cookie(self):
        try:
            self.wait.until(EC.element_to_be_clickable(L.COOKIE_BUTTON)).click()
        except:
            pass

    def scroll_to(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def js_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    # ---------- Кнопки заказа ----------

    def click_order_top(self):
        self.wait.until(EC.element_to_be_clickable(L.ORDER_BUTTON_TOP)).click()

    def click_order_bottom(self):
        button = self.scroll_to(L.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].click();", button)

    # ---------- Шаг 1: данные клиента ----------

    def fill_step1(self, name, surname, address, metro, phone):
        self.wait.until(EC.visibility_of_element_located(L.ORDER_NAME)).send_keys(name)
        self.driver.find_element(*L.ORDER_SURNAME).send_keys(surname)
        self.driver.find_element(*L.ORDER_ADDRESS).send_keys(address)

        # Метро
        self.driver.find_element(*L.ORDER_METRO).send_keys(metro)
        self.wait.until(EC.element_to_be_clickable(L.ORDER_METRO_OPTION(metro))).click()

        self.driver.find_element(*L.ORDER_PHONE).send_keys(phone)
        self.wait.until(EC.element_to_be_clickable(L.ORDER_NEXT_BUTTON)).click()

    # ---------- Шаг 2: детали заказа ----------

    def fill_step2(self, date, rent_period, color):
        # ---------- Дата ----------
        date_input = self.wait.until(EC.element_to_be_clickable(L.ORDER_DATE))
        date_input.click()
        date_input.clear()
        date_input.send_keys(date)
        self.driver.find_element(By.TAG_NAME, "body").click()  # закрываем календарь

        # ---------- Срок аренды ----------
        self.wait.until(EC.element_to_be_clickable(L.ORDER_RENT_PERIOD)).click()
        self.wait.until(EC.element_to_be_clickable(L.get_rent_period_locator(rent_period))).click()

        # ---------- Цвет ----------
        self.wait.until(EC.element_to_be_clickable(L.get_color_locator(color))).click()

        # ---------- Кнопка "Заказать" ----------
        order_button = self.wait.until(
            EC.presence_of_element_located(L.ORDER_SUBMIT_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", order_button
        )
        self.driver.execute_script("arguments[0].click();", order_button)

    # ---------- Подтверждение заказа на баннере ----------

    def confirm_order(self):
        confirm_button = self.wait.until(
            EC.element_to_be_clickable(L.ORDER_CONFIRM_YES_BUTTON)
        )
        confirm_button.click()

    # ---------- Проверка успешного заказа ----------

    def is_order_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(L.ORDER_SUCCESS_TITLE)
        ).is_displayed()