from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import BASE_URL
from locators import FAQPageLocators as L


class FAQPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # ---------- Открытие страницы ----------
    def open(self):
        self.driver.get(BASE_URL)
        # Скроллим в самый низ, чтобы FAQ подгрузился
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # ---------- Действия ----------
    def click_question(self, q_id):
        question = self._scroll_to_question(q_id)
        question.click()
        return question

    # ---------- Проверки ----------
    def is_collapsed(self, q_id):
        question = self._scroll_to_question(q_id)
        return question.get_attribute("aria-expanded") == "false"

    def is_expanded(self, q_id):
        question = self._scroll_to_question(q_id)
        return question.get_attribute("aria-expanded") == "true"

    # ---------- Получение элементов ----------
    def get_question(self, q_id):
        return self._scroll_to_question(q_id)

    def get_answer(self, q_id):
        locator = L.ANSWER(q_id)
        # Ждём, пока ответ станет видимым
        answer = self.wait.until(EC.visibility_of_element_located(locator))
        # Скроллим к ответу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", answer)
        return answer

    # ---------- Вспомогательные методы ----------
    def _scroll_to_question(self, q_id):
        """Ждём появления вопроса и скроллим к нему"""
        locator = L.QUESTION(q_id)
        question = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question)
        return question

    def wait_for_answer_visible(self, q_id):
        """Ждём, пока ответ станет видимым (отдельный метод, если нужно в тесте)"""
        return self.wait.until(EC.visibility_of_element_located(L.ANSWER(q_id)))
