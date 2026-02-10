import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture
def driver():
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    # Если нужен headless:
    # options.add_argument("-headless")

    service = FirefoxService()

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()

    yield driver
    driver.quit()
