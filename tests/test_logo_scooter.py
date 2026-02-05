from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import L
from pages.main_page import MainPage

def test_click_scooter_logo_opens_main_page(driver):
    page = MainPage(driver)
    page.open()

    page.click_scooter_logo()

    assert driver.current_url == BASE_URL
