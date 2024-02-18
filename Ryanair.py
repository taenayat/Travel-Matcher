from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://ryanair.com")

driver.maximize_window()

## accept cookies
driver.find_element("xpath", '//*[@id="cookie-popup-with-overlay"]/div/div[3]/button[3]').click()

## one-way trip
one_way_flight = driver.find_element(By.ID, value='ry-radio-button--0')
driver.execute_script("arguments[0].click();", one_way_flight)


driver.save_screenshot("screenshot1.png")
driver.quit()