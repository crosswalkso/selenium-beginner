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
            time.sleep(3)
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

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(
            By.CSS_SELECTOR,
            'input[name="ss"]',
        )
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_result = self.find_element(
            By.XPATH,
            f"//*[@class='f9a8ccdcc6']//*[text()='{place_to_go}']",
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{check_in_date}"]',
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{check_out_date}"]',
        )
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="occupancy-config"]',
        )
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(
                By.XPATH,
                f"//*[@class='df856d97eb']//*[@class='b2b5147b20'][1]//*[@class='e98c626f34']/button[1]",
            )
            decrease_adults_element.click()
            # If the value of adults reaches 1, then we should get out
            # of the while loop
            adults_value_element = self.find_elements(
                By.CSS_SELECTOR,
                'span[class="e615eb5e43"]',
            )[0]
            adults_value = (
                adults_value_element.text
            )  # Should give back the adults count

            if int(adults_value) == 1:
                break

        increase_adults_element = self.find_element(
            By.XPATH,
            f"//*[@class='df856d97eb']//*[@class='b2b5147b20'][1]//*[@class='e98c626f34']/button[2]",
        )

        for _ in range(count - 1):
            increase_adults_element.click()

    def click_search(self):
        search_button = self.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]',
        )
        search_button.click()
