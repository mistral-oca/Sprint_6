from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- Навигация ----------
    def open(self, url):
        self.driver.get(url)

    # ---------- Поиск элементов ----------
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # ---------- Действия ----------
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def fill_input(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)
        return element

    # ---------- Вспомогательные ----------
    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )

    def get_current_url(self):
        return self.driver.current_url
