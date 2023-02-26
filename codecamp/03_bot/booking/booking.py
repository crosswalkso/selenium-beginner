import booking.constants as const

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class Booking(webdriver.Chrome):
    # constructor
    def __init__(self, teardown=False):
        self.teardown = teardown
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options,
        )
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)
