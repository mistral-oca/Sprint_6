from urls import BASE_URL
from pages.main_page import MainPage

class TestMainPage:

    def test_click_scooter_logo_opens_main_page(self, driver):
        page = MainPage(driver)
        page.open()

        page.click_scooter_logo()

        assert driver.current_url == BASE_URL
