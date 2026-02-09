from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import L

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(BASE_URL)

    def click_scooter_logo(self):
        self.wait.until(
            EC.element_to_be_clickable(L.SCOOTER_LOGO)
        ).click()

    def click_yandex_logo(self):
        self.wait.until(
            EC.element_to_be_clickable(L.YANDEX_LOGO)
        ).click()

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self, original_window):
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = [
            window for window in self.driver.window_handles
            if window != original_window
        ][0]
        self.driver.switch_to.window(new_window)

    def wait_for_dzen_page(self):
        self.wait.until(EC.url_contains("dzen.ru"))

    def get_current_url(self):
        return self.driver.current_url