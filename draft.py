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

# service = Service(executable_path="~/Documents/TravelMatcher/chromedriver")
# driver = webdriver.Chrome(service=service)


driver.get("https://booking.com")

# init_button = driver.find_element(By.XPATH, value='//*[@id="b2indexPage"]/div[18]/div/div/div/div[1]/div[1]/div/button')
# init_button.click()

#  = driver.find_element(By.XPATH, value='//button[@id="b2indexPage"]')
# init_button = driver.find_element(By.XPATH, value="//*[@aria-label='Dismiss sign-in info.']")
# init_button.click()

height = driver.execute_script('return document.documentElement.scrollHeight')
width  = driver.execute_script('return document.documentElement.scrollWidth')
driver.set_window_size(width, height)  # the trick
time.sleep(2)
driver.save_screenshot("screenshot1.png")

driver.quit()

# time.sleep(10)




# IN RYANAIR, WHILE CLICKING ON ONE WAY TRIP RADIO BUTTON
# from selenium.common.exceptions import TimeoutException
# def click_by_xpath(NameOfObject):
#     try:
#         item = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, NameOfObject)))
#         item.click()
#     except TimeoutException as e:
#         print("Couldn't Click by name on: " + str(NameOfObject))
#         pass

# # driver.find_element('xpath', '//ry-radio-button//input[@id="ry-radio-button--0"]').click()
# # one_way = driver.find_element('xpath', '//*[@id="ry-radio-button--0"]]')
# # one_way = driver.find_element('xpath', '//ry-radio-button')
# html = driver.page_source
# with open("html.txt", 'w') as file:
#     file.write(html)
# # one_way = driver.find_element('xpath', '//*[@id="main-content"]/fsw-flight-search-widget-container/fsw-flight-search-widget/fsw-trip-type-container/fsw-trip-type/ry-radio-button[2]')
# # print(one_way.get_attribute("innetHTML"))
# # .click()
# one_way_flight = driver.find_element(By.ID, value='ry-radio-button--0')
# # one_way_flight = driver.find_elements(By.XPATH, value='//*[@id="main-content"]')
# one_way_flight = driver.find_elements(By.XPATH, value='//ry-radio-button//input')
# print(len(one_way_flight))
# print(one_way_flight[1].get_attribute('id'))
# one_way_flight.click()
# driver.execute_script("arguments[0].click();", one_way_flight)




# dest_airport_idx
# airport_select(driver, 12, is_origin=False)
# len(find_airports(driver))
# a = driver.find_elements('xpath','//fsw-airport-item//span[@data-ref="airport-item__name"]')
# a[0].click()
# driver.execute_script("arguments[0].click();", a[0])
# ActionChains(driver).move_to_element(a[5]).click().perform()
# a = driver.find_elements('xpath','//fsw-airport-item//span[contains(@data-ref,"airport-item")]')
# len(a)

# driver = init_driver(options)
# driver.get("http://ryanair.com")
# accept_cookies(driver)
# click_origin_box(driver)
# driver.find_element(By.XPATH, '//*[@id="input-button__departure"]').click()
# countries = find_countries(driver)
# len(countries)
# driver.quit()


# df1 = pd.read_csv('origin_destination_pair2.csv')[['origin_country_name', 'origin_airport_code',
#        'origin_airport_name', 'dest_country_name', 'dest_airport_code',
#        'dest_airport_name']]
# df2 = pd.read_csv('origin_destination_pair4.csv')[['origin_country_name', 'origin_airport_code',
#        'origin_airport_name', 'dest_country_name', 'dest_airport_code',
#        'dest_airport_name']]
# df = pd.concat([df1,df2])
# df.to_csv('origin_destination_pair.csv', index=False)



#######################################
###### CHECK THE AIRPORT PAIRS ########
#######################################

import pandas as pd
pd.read_csv('origin_destination_pairs.csv')