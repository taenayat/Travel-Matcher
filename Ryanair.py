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


## For loop
# select origin box
driver.find_element('xpath', '//*[@id="input-button__departure"]').click()
origin_countries = driver.find_elements('xpath', '//span[contains(@class,"countries__country-inner")]')
# for origin_country in origin_countries[:2]:
# for origin_idx in range(len(origin_countries)):
for origin_idx in range(1):
    origin_countries = driver.find_elements('xpath', '//span[contains(@class,"countries__country-inner")]')
    origin_country = origin_countries[origin_idx]
    country_name = origin_country.get_attribute("innerHTML")
    print(country_name)
    origin_country.click()
    time.sleep(1)

    origin_airports_clickable = driver.find_elements(By.TAG_NAME, 'fsw-airport-item')
    origin_airports = driver.find_elements('xpath', '//fsw-airport-item//span[@data-ref="airport-item__name"]')
    # len(origin_airports)

    trunc = 1
    for origin_airport, origin_airport_clickable in zip(origin_airports[:trunc], origin_airports_clickable[:trunc]):
        origin_airport_code = origin_airport.get_attribute("data-id")
        print(origin_airport_code)
        origin_airport_name = re.sub('[\W_]+', '', origin_airports[0].get_attribute("innerHTML"))
        # origin_airports_clickable[0].click()
        driver.execute_script("arguments[0].click();", origin_airport_clickable)
        time.sleep(2)

        destination_countries =  driver.find_elements('xpath', '//span[contains(@class,"countries__country-inner")]')
        # for destination_country in destination_countries:
        for origin_idx in range(len(origin_countries)):
            if 'not-available' not in destination_country.get_attribute('class'): # dest country is available
                destination_country.click()
                destination_airports_clickable = driver.find_elements(By.TAG_NAME, 'fsw-airport-item')
                destination_airports = driver.find_elements('xpath', '//fsw-airport-item//span[@data-ref="airport-item__name"]')
                # len(destination_airports_clickable)

                for destination_airport, destination_airport_clickable in zip(destination_airports, destination_airports_clickable):
                    destination_airport_code = destination_airport.get_attribute("data-id")
                    print(destination_airport_code)
                    destination_airport_name = re.sub('[\W_]+', '', destination_airports[0].get_attribute("innerHTML"))
                    print(destination_airport_name)
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

















