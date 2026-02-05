from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import L
from pages.main_page import MainPage

def test_click_yandex_logo_opens_dzen(driver):
    page = MainPage(driver)
    page.open()

    original_window = driver.current_window_handle

    page.click_yandex_logo()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    new_window = [
        window for window in driver.window_handles
        if window != original_window
    ][0]

    driver.switch_to.window(new_window)

    WebDriverWait(driver, 10).until(
        EC.url_contains("dzen.ru")
    )

    assert "dzen.ru" in driver.current_url
