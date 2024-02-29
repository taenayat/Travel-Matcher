from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import pandas as pd

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver.get("http://ryanair.com")

# driver.maximize_window()

# ## accept cookies
# driver.find_element("xpath", '//*[@id="cookie-popup-with-overlay"]/div/div[3]/button[3]').click()

# ## one-way trip
# one_way_flight = driver.find_element(By.ID, value='ry-radio-button--0')
# # driver.execute_script("arguments[0].click();", one_way_flight)
# # driver.execute_script("var event = new Event('change'); arguments[0].dispatchEvent(event);", one_way_flight)
# actions = ActionChains(driver)
# actions.move_to_element(one_way_flight).click().perform()

# ## destinations
# destination = driver.find_element('xpath','//*[@id="input-button__destination"]')
# destination.send_keys('Venecia Treviso')
# airports = driver.find_elements(By.TAG_NAME, 'fsw-airport-item')
# driver.execute_script("arguments[0].click();", airports[1])
# # driver.find_element('xpath','//*[@id="ry-tooltip-3"]/div[2]/hp-app-controls-tooltips/fsw-controls-tooltips-container/fsw-controls-tooltips/fsw-destination-container/fsw-airports/div/fsw-airports-list/div[2]/div[1]/fsw-airport-item[2]').click() # first one in the list

# ## scroll to see better
# # ActionChains(driver).scroll_by_amount(0, 100).perform()

# ## departure date
# departure = driver.find_element('xpath','//*[@id="ry-tooltip-10"]/div[2]/hp-app-controls-tooltips/fsw-controls-tooltips-container/fsw-controls-tooltips/fsw-flexible-datepicker-container/fsw-datepicker/ry-datepicker-desktop/div')
# dates = departure.find_elements(By.CLASS_NAME, 'calendar-body__cell')

# for date in dates: 
#     class_value = date.get_attribute('class')
#     if 'calendar-body__cell--disabled' not in class_value: # available dates
#         date_value = date.get_attribute('data-id')
#         # print(date_value)
#         if date_value == "2024-03-27":
#             print(date_value)
#             chosen_date = date
#             break
# chosen_date.click()


# ## click search button
# driver.find_element('xpath', '//button[contains(@class,"flight-search-widget__start-search-cta")]').click()


# # time.sleep(2)
# # fares = driver.find_elements('xpath', '//carousel-item[@class="ng-star-inserted"]')


# driver.save_screenshot("screenshot1.png")
# driver.quit()







# origin = "MAD"
# destination = "TSF"
# start_date = "2024-02-19" # make it today

# def url_finder(origin, destination, start_date):
#     url = 'https://www.ryanair.com/es/es/trip/flights/select?adults=1&teens=0&children=0&infants=0&'\
#         'dateOut={2}&dateIn=&isConnectedFlight=false&discount=0&isReturn=false&promoCode=&'\
#         'originIata={0}&destinationIata={1}&tpAdults=1&tpTeens=0&tpChildren=0&tpInfants=0&'\
#         'tpStartDate={2}&tpEndDate=&tpDiscount=0&tpPromoCode=&tpOriginIata={0}&tpDestinationIata={1}'
#     return url.format(origin, destination, start_date)

# url = url_finder(origin,destination,start_date)


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get(url)
# driver.find_element("xpath", '//button[@class="cookie-popup-with-overlay__button"]').click()

# # fares = driver.find_elements('xpath', '//button[contains(@class,"date-item")]')
# # fares[0].get_attribute("data-ref")
# # fares[1].find_element(By.CLASS_NAME, value='date-item__day-of-week').get_attribute('innerHTML').strip()

# # fares[1].find_elements(By.XPATH, value='.//span[contains(@class,"price")]')
# # price_arr = [element.get_attribute('innerHTML') for element in fares[1].find_elements(By.XPATH, value='.//span[contains(@class,"price")]')]
# # price = price_arr[1].strip() + '.' + price_arr[3].strip()
# # ''.join(map(lambda x: x.strip(), price_arr))



# fares = driver.find_elements('xpath', '//button[contains(@class,"date-item")]')

# temp_list = []
# for fare in fares:
#     date_value = fare.get_attribute("data-ref")
#     day_of_week = fare.find_element(By.CLASS_NAME, value='date-item__day-of-week').get_attribute('innerHTML').strip()
#     price_arr = [element.get_attribute('innerHTML') for element in fare.find_elements(By.XPATH, value='.//span[contains(@class,"price")]')]
#     price = ''.join(map(lambda x: x.strip(), price_arr))
#     dic = {'date': date_value, 'day_of_week': day_of_week, 'price': price}
#     temp_list.append(dic)

# ## output dataframe of a given page
# def fares_dataframe(driver):

#     fares = driver.find_elements('xpath', '//button[contains(@class,"date-item")]')
#     temp_list = []
#     for fare in fares:
#         date_value = fare.get_attribute("data-ref")
#         day_of_week = fare.find_element(By.CLASS_NAME, value='date-item__day-of-week').get_attribute('innerHTML').strip()
#         price_arr = [element.get_attribute('innerHTML') for element in fare.find_elements(By.XPATH, value='.//span[contains(@class,"price")]')]
#         price = ''.join(map(lambda x: x.strip(), price_arr))
#         dic = {'date': date_value, 'day_of_week': day_of_week, 'price': price}
#         temp_list.append(dic)
#     return pd.DataFrame(temp_list).replace('', None, inplace = True)


# import pandas as pd
# # df = pd.concat([df, pd.DataFrame(temp_list)], ignore_index=True)
# df = pd.DataFrame(temp_list)


# ## next dates
# driver.find_element('xpath', '//button[contains(@class,"carousel-next")]').click()
# df = pd.concat([df, fares_dataframe(driver)])

# driver.save_screenshot("screenshot1.png")
# driver.quit()



###########################################################################
#################### FIND ALL ORIGIN-DESTINATION PAIRS ####################
###########################################################################

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://ryanair.com")

driver.maximize_window()

## accept cookies
driver.find_element("xpath", '//*[@id="cookie-popup-with-overlay"]/div/div[3]/button[3]').click()

## one-way trip
# one_way_flight = driver.find_element(By.ID, value='ry-radio-button--0')
# actions = ActionChains(driver)
# actions.move_to_element(one_way_flight).click().perform()

## origins
driver.find_element('xpath', '//*[@id="input-button__departure"]').click()
# driver.execute_script("arguments[0].click();", origins)

# countries = driver.find_elements('xpath', '//fsw-countries[contains(@class,"countries__country")]')
origins = driver.find_elements('xpath', '//span[contains(@class,"countries__country-inner")]')
print(len(origins))
country = origins[1]
country_name = country.get_attribute("innerHTML")
print(country_name)
# driver.execute_script("arguments[0].click();", country)
country.click()
origin_airports_clickable = driver.find_elements(By.TAG_NAME, 'fsw-airport-item')
origin_airports = driver.find_elements('xpath', '//fsw-airport-item//span[@data-ref="airport-item__name"]')
len(origin_airports)
origin_airport = origin_airports[0]
origin_airport_code = origin_airport.get_attribute("data-id")
print(origin_airport_code)
origin_airport_name = re.sub('[\W_]+', '', origin_airports[0].get_attribute("innerHTML"))
# origin_airports_clickable[0].click()
driver.execute_script("arguments[0].click();", origin_airports_clickable[0])



## destination
destinations =  driver.find_elements('xpath', '//span[contains(@class,"countries__country-inner")]')
print(len(destinations))
destination_country = destinations[3]
print(destination_country.get_attribute("innerHTML"))
'not-available' not in destination_country.get_attribute('class')
destination_country.click()
destination_airports_clickable = driver.find_elements(By.TAG_NAME, 'fsw-airport-item')
len(destination_airports_clickable)
destination_airports = driver.find_elements('xpath', '//fsw-airport-item//span[@data-ref="airport-item__name"]')
destination_airport = destination_airports[0]
destination_airport_code = destination_airport.get_attribute("data-id")
print(destination_airport_code)
destination_airport_name = re.sub('[\W_]+', '', destination_airports[0].get_attribute("innerHTML"))
print(destination_airport_name)





def click_origin_box(driver): 
    driver.find_element('xpath', '//*[@id="input-button__departure"]').click()
def find_countries(driver):
    return driver.find_elements('xpath', '//span[contains(@class,"countries__country-inner")]')
def find_airports(driver):
    return driver.find_elements('xpath', '//fsw-airport-item//span[@data-ref="airport-item__name"]')
def find_airports_clickable(driver):
    return driver.find_elements(By.TAG_NAME, 'fsw-airport-item')
def get_airport_name(airport):
    return re.sub('[\W_]+', '', airport.get_attribute("innerHTML"))
def get_airport_code(airport):
    return airport.get_attribute("data-id")
def script_click(driver, element):
    driver.execute_script("arguments[0].click();", element)
def is_available(element):
    return'not-available' not in element.get_attribute('class')

def origin_country_select(driver, origin_idx):
    if origin_idx != 0: click_origin_box(driver)
    origin_country = find_countries(driver)[origin_idx]
    origin_country_name = origin_country.get_attribute("innerHTML")
    origin_country.click()
    return origin_country_name

def destination_country_select(destination_country):
    destination_country_name = get_airport_name(destination_country)
    destination_country.click()
    return destination_country_name

def airport_select(driver, airport_idx, is_origin=True):
    airport_clickable = find_airports_clickable(driver)[airport_idx]
    airport = find_airports(driver)[airport_idx]

    airport_code = get_airport_code(airport)
    airport_name = get_airport_name(airport)
    if is_origin: script_click(driver, airport_clickable)
    return airport_code, airport_name

def append_to_list(l, origin_country_name, origin_airport_code,origin_airport_name,
                   desination_country_name,destination_airport_code,destination_airport_name):
    dic = {'origin_country_name': origin_country_name, 
        'origin_airport_code': origin_airport_code, 
        'origin_airport_name': origin_airport_name, 
        'dest_country_name': desination_country_name, 
        'dest_airport_code': destination_airport_code, 
        'dest_airport_name': destination_airport_name}
    l.append(dic)


## For loop
# df = pd.DataFrame()
data_list = []
# select origin box
# driver.find_element('xpath', '//*[@id="input-button__departure"]').click()
click_origin_box(driver)
countries_len = len(find_countries(driver))
# for origin_country in origin_countries[:2]:
# for origin_idx in range(countries_len):
for origin_idx in range(2):
    origin_country_name = origin_country_select(driver, origin_idx)
    time.sleep(1)

    origin_airports_clickable = find_airports_clickable(driver)
    # origin_airports = driver.find_elements('xpath', '//fsw-airport-item//span[@data-ref="airport-item__name"]')
    # len(origin_airports)

    # trunc = 2
    # for origin_airport, origin_airport_clickable in zip(origin_airports[:trunc], origin_airports_clickable[:trunc]):
    # for airport_idx in range(len(origin_airports_clickable)):
    for origin_airport_idx in range(2):
        origin_airport_code, origin_airport_name = airport_select(driver, origin_airport_idx)
        time.sleep(1)

        # destination_countries =  find_countries(driver)
        # for destination_country in destination_countries:
        # for destination_idx in range(countries_len):
        for destination_idx in range(2):
            destination_country =  find_countries(driver)[destination_idx]
            if is_available(destination_country):
                desination_country_name = destination_country_select(destination_country)
                destination_airports_clickable = find_airports_clickable(driver)
                # destination_airports = driver.find_elements('xpath', '//fsw-airport-item//span[@data-ref="airport-item__name"]')
                # len(destination_airports_clickable)
                time.sleep(1)

                # for destination_airport, destination_airport_clickable in zip(destination_airports[:trunc], destination_airports_clickable[:trunc]):
                # for dest_airport_idx in range(len(destination_airports_clickable)):    
                for dest_airport_idx in range(2):    
                    destination_airport_code, destination_airport_name = airport_select(driver, dest_airport_idx, is_origin=False)
                    
                    append_to_list(data_list)
                    # print("final:", dic)
                    time.sleep(1)




# ## destinations
# destination = driver.find_element('xpath','//*[@id="input-button__destination"]')
# destination.send_keys('Venecia Treviso')
# airports = driver.find_elements(By.TAG_NAME, 'fsw-airport-item')
# driver.execute_script("arguments[0].click();", airports[1])
# driver.find_element('xpath','//*[@id="ry-tooltip-3"]/div[2]/hp-app-controls-tooltips/fsw-controls-tooltips-container/fsw-controls-tooltips/fsw-destination-container/fsw-airports/div/fsw-airports-list/div[2]/div[1]/fsw-airport-item[2]').click() # first one in the list

## scroll to see better
# ActionChains(driver).scroll_by_amount(0, 100).perform()

## departure date
# departure = driver.find_element('xpath','//*[@id="ry-tooltip-10"]/div[2]/hp-app-controls-tooltips/fsw-controls-tooltips-container/fsw-controls-tooltips/fsw-flexible-datepicker-container/fsw-datepicker/ry-datepicker-desktop/div')
# dates = departure.find_elements(By.CLASS_NAME, 'calendar-body__cell')

# for date in dates: 
#     class_value = date.get_attribute('class')
#     if 'calendar-body__cell--disabled' not in class_value: # available dates
#         date_value = date.get_attribute('data-id')
#         # print(date_value)
#         if date_value == "2024-03-27":
#             print(date_value)
#             chosen_date = date
#             break
# chosen_date.click()


## click search button
# driver.find_element('xpath', '//button[contains(@class,"flight-search-widget__start-search-cta")]').click()


# time.sleep(2)
# fares = driver.find_elements('xpath', '//carousel-item[@class="ng-star-inserted"]')


# scroll to see better
ActionChains(driver).scroll_by_amount(0, 100).perform()
driver.save_screenshot("screenshot1.png")
driver.quit()
















