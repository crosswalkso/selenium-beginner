from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

KEYWORD = "iron man"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options,
)

driver.get("https://google.com")

# 검색창, 검색
search_bar = driver.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys(KEYWORD + Keys.ENTER)

# search_results = WebDriverWait(driver, 2000).until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME, "g"))
# )


# array
search_results = driver.find_elements(By.CLASS_NAME, "g")
child_results = search_results.find_elements(By.CSS_SELECTOR, "*")

for index, child_result in enumerate(child_results):
    print(child_result)
    # child_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")


# v5yQqb
# driver.quit()
