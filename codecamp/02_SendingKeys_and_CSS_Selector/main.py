from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Enter, Alt, ..
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import *

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options,
)
KEYWORD = "파이썬"
driver.get("https://google.com")
driver.implicitly_wait(5)

# 파이썬 검색 후 keydown, enter, 검색 element click
search_bar = driver.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys(KEYWORD)
WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element_value(
        (By.CLASS_NAME, "gLFyf"),
        "파이썬",
    )
)
sleep(1)
for i in range(3):
    search_bar.send_keys(Keys.ARROW_DOWN)
sleep(3)
search_bar.send_keys(Keys.ENTER)
btn = driver.find_element(By.CSS_SELECTOR, "button[jsname='Tg7LZd']")
sleep(0.1)
btn.send_keys(Keys.ENTER)
