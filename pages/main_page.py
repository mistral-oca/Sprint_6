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
