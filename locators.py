from selenium.webdriver.common.by import By


class FAQPageLocators:

    @staticmethod
    def QUESTION(q_id):
        # пример: id='accordion__heading-8'
        return (By.ID, f"accordion__heading-{q_id}")

    @staticmethod
    def ANSWER(q_id):
        # пример: id='accordion__panel-8'
        return (By.ID, f"accordion__panel-{q_id}")


class L:
    # ==================================================
    # Главная страница
    # ==================================================

    ORDER_BUTTON_TOP = (
        By.XPATH,
        "(//button[normalize-space(text())='Заказать'])[1]"
    )
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "(//button[normalize-space(text())='Заказать'])[2]"
    )

    # ==================================================
    # Форма заказа — шаг 1 (персональные данные)
    # ==================================================

    ORDER_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    ORDER_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ORDER_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    ORDER_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    ORDER_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    ORDER_NEXT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Далее']")

    # --------------------------------------------------
    # Метро — выпадающий список (ДОБАВЛЕНО)
    # --------------------------------------------------

    @staticmethod
    def ORDER_METRO_OPTION(metro_name):
        return (
            By.XPATH,
            f"//div[contains(@class,'select-search__select')]"
            f"//div[normalize-space(text())='{metro_name}']"
        )

    # ==================================================
    # Форма заказа — шаг 2 (параметры аренды)
    # ==================================================

    ORDER_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    ORDER_RENT_PERIOD = (
        By.XPATH,
        "//div[normalize-space(text())='* Срок аренды']"
    )

    ORDER_RENT_PERIOD_TWO_DAYS = (
        By.XPATH,
        "//div[contains(@class,'Dropdown-placeholder') "
        "and normalize-space(text())='двое суток']"
    )

    ORDER_COLOR_BLACK = (
        By.XPATH,
        "//label[normalize-space(text())='чёрный жемчуг']"
    )

    ORDER_SUBMIT_BUTTON = (
        By.XPATH,
        "(//button[normalize-space(text())='Заказать'])[last()]"
    )



    # ==================================================
    # Модальное окно подтверждения
    # ==================================================

    
    ORDER_CONFIRM_YES_BUTTON = (
        By.XPATH,
        "//button[normalize-space(text())='Да']"
    )

    # ==================================================
    # Успешное оформление заказа
    # ==================================================

    ORDER_SUCCESS_TITLE = (
        By.XPATH,
        "//*[normalize-space(text())='Заказ оформлен']"
    )

    ORDER_SUCCESS_TEXT = (
        By.XPATH,
        "//div[contains(text(),'Номер заказа')]"
    )

    ORDER_VIEW_STATUS_BUTTON = (
        By.CSS_SELECTOR,
        ".Order_NextButton__1_rCA > button"
    )

    # ==================================================
    # Логотипы
    # ==================================================

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

        # ---------- Динамические локаторы ----------

    @staticmethod
    def get_rent_period_locator(period):
        return (
            By.XPATH,
            f"//div[contains(@class,'Dropdown-menu')]//div[normalize-space(text())='{period}']"
        )

    @staticmethod
    def get_color_locator(color):
        return (
            By.XPATH,
            f"//label[normalize-space(text())='{color}']"
        )

# ==================================================
# Cookie banner
# ==================================================

COOKIE_ACCEPT_BUTTON = (
    By.XPATH,
    "//button[normalize-space(text())='да все привыкли']"
)
