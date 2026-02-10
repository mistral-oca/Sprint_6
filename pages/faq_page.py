from urls import BASE_URL
from locators import FAQPageLocators as L
from pages.base_page import BasePage


class FAQPage(BasePage):

    # ---------- Открытие страницы ----------
    def open(self):
        super().open(BASE_URL)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    # ---------- Действия ----------
    def click_question(self, q_id):
        question = self._get_question(q_id)
        self.scroll_to_element(question)
        question.click()
        return question

    # ---------- Проверки ----------
    def is_collapsed(self, q_id):
        return self._get_question(q_id).get_attribute(
            "aria-expanded"
        ) == "false"

    def is_expanded(self, q_id):
        return self._get_question(q_id).get_attribute(
            "aria-expanded"
        ) == "true"

    # ---------- Получение элементов ----------
    def get_question(self, q_id):
        return self._get_question(q_id)

    def get_answer(self, q_id):
        answer = self.find_visible_element(L.ANSWER(q_id))
        self.scroll_to_element(answer)
        return answer

    def wait_for_answer_visible(self, q_id):
        return self.find_visible_element(L.ANSWER(q_id))

    # ---------- Внутренние методы ----------
    def _get_question(self, q_id):
        question = self.find_element(L.QUESTION(q_id))
        self.scroll_to_element(question)
        return question
