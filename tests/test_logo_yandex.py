from pages.main_page import MainPage

class TestMainPage:

    def test_click_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        page.open()

        original_window = page.get_current_window()

        page.click_yandex_logo()
        page.switch_to_new_window(original_window)
        page.wait_for_dzen_page()

        assert "dzen.ru" in page.get_current_url()