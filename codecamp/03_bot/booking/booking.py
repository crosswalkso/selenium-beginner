import time
import booking.constants as const

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class Booking(webdriver.Chrome):
    # constructor
    def __init__(self, teardown=False):
        # super(Booking, self).__init__() 2.x
        super().__init__(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options,
        )  # 3.x
        self.teardown = teardown
        self.implicitly_wait(5)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)
        try:
            login_guide_button = self.find_element(
                By.CSS_SELECTOR,
                "button[aria-label='로그인 혜택 안내 창 닫기.']",
            )
            login_guide_button.click()
        except Exception as error:
            pass

    def __enter__(self):
        self.land_first_page()
        return self

    def __exit__(self, exc_type, exc, traceback):
        # browser quit()을 teardown으로 관리
        if self.teardown:
            time.sleep(2)
            print("Browser successfuly ended.")
            self.quit()

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="header-currency-picker-trigger"]',
        )
        currency_element.click()
        selected_currency_element = self.find_element(
            By.XPATH,
            f"//*[@class='cf67405157']//*[text()='{currency}']",  # {currency} => EUR, not 'EUR'
        )
        selected_currency_element.click()
