from selenium import webdriver  # 브라우저 open 자동화
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options,
)
KEYWORD = "파이썬"
driver.get("https://google.com")
driver.implicitly_wait(1)

search_bar = driver.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys(KEYWORD)
print("search 파이썬")
WebDriverWait(driver, 5).until(  # 특정 element의 행동을 기다림
    EC.text_to_be_present_in_element_value(
        (By.CLASS_NAME, "gLFyf"),
        "파이썬",
    )
)
print("complete")
