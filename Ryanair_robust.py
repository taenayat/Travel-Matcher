from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
from datetime import datetime
import pandas as pd
import re

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

origin = "MAD"
destination = "TSF"
start_date = date.today()
end_date = "2024-03-15"

def url_finder(origin, destination, start_date):
    start_date = start_date.strftime('%Y-%m-%d')
    url = 'https://www.ryanair.com/es/es/trip/flights/select?adults=1&teens=0&children=0&infants=0&'\
        'dateOut={2}&dateIn=&isConnectedFlight=false&discount=0&isReturn=false&promoCode=&'\
        'originIata={0}&destinationIata={1}&tpAdults=1&tpTeens=0&tpChildren=0&tpInfants=0&'\
        'tpStartDate={2}&tpEndDate=&tpDiscount=0&tpPromoCode=&tpOriginIata={0}&tpDestinationIata={1}'
    return url.format(origin, destination, start_date)

url = url_finder(origin,destination,start_date)


## output dataframe of a given page
def fares_dataframe(driver):

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"date-item")]'))
    )
    fares = driver.find_elements(By.XPATH, '//button[contains(@class,"date-item")]')
    # print('len =', len(fares))
    temp_list = []
    for fare in fares:
        date_value = fare.get_attribute("data-ref")
        day_of_week = fare.find_element(By.CLASS_NAME, value='date-item__day-of-week').get_attribute('innerHTML').strip()
        price_arr = [element.get_attribute('innerHTML') for element in fare.find_elements(By.XPATH, value='.//span[contains(@class,"price")]')]
        price = ''.join(map(lambda x: x.strip(), price_arr))
        dic = {'date': date_value, 'day_of_week': day_of_week, 'price': price}
        # print(dic)
        temp_list.append(dic)
    return pd.DataFrame(temp_list).replace('', None), datetime.strptime(date_value, '%Y-%m-%d').date()



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@class="cookie-popup-with-overlay__button"]')))
    element.click()
except:
    print("Cookies button not found within 10 seconds")

# wait for site to load
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"date-item")]'))
)
df,_ = fares_dataframe(driver)
# driver.save_screenshot("screenshot1.png")
# print(df.head())
# print('iteration = 0')
## next dates

current_date = start_date
end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
i = 1
while current_date <= end_date:
    # print('iteration =', i)
    i += 1
    print('iter =', i, "current:", current_date, "end:", end_date)
    # print("condition:", current_date <= end_date)
    # current_date = datetime.strptime(re.findall(r'tpStartDate=.{10}', driver.current_url)[0][-10:], '%Y-%m-%d').date()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"carousel-next")]'))).click()
    df_temp, current_date = fares_dataframe(driver)
    df = pd.concat([df, df_temp])
    # print(df.tail(5))

df.to_csv('MAD_TSF_20240218_20240315.csv', index=False)

# driver.save_screenshot("screenshot1.png")
driver.quit()





