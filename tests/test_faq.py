import pytest
from pages.faq_page import FAQPage

@pytest.mark.usefixtures("driver")
class TestFAQ:

    @pytest.mark.parametrize("question_id", ["0", "1", "2", "3", "4", "5", "6"])
    def test_faq_question_expands(self, driver, question_id):
        page = FAQPage(driver)
        page.open()

        assert page.is_collapsed(question_id)
        page.click_question(question_id)

        assert page.is_expanded(question_id)
        assert page.get_answer(question_id).is_displayed()
