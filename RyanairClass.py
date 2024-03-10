## Authur: Taha Enayat
## March 2024

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


class RyanairDataFetcher:
    
    def __init__(self, origin, destination, start_date, end_date):

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self.origin = origin
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.url = self.url_finder(self.origin, self.destination, self.start_date)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(self.url)

    def url_finder(self, origin, destination, start_date):
        start_date = start_date.strftime('%Y-%m-%d')
        url = 'https://www.ryanair.com/es/es/trip/flights/select?adults=1&teens=0&children=0&infants=0&'\
            'dateOut={2}&dateIn=&isConnectedFlight=false&discount=0&isReturn=false&promoCode=&'\
            'originIata={0}&destinationIata={1}&tpAdults=1&tpTeens=0&tpChildren=0&tpInfants=0&'\
            'tpStartDate={2}&tpEndDate=&tpDiscount=0&tpPromoCode=&tpOriginIata={0}&tpDestinationIata={1}'
        return url.format(origin, destination, start_date)

    def fares_dataframe(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"date-item")]'))
        )
        fares = self.driver.find_elements(By.XPATH, '//button[contains(@class,"date-item")]')
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
    
    def click_cookie_button(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"cookie-popup-with-overlay__button") and @data-ref="cookie.accept-all"]')))
            element.click()
        except:
            print("Cookies button not found within 10 seconds")

    def fetch_data(self):
        current_date = self.start_date
        end = datetime.strptime(self.end_date, '%Y-%m-%d').date()

        i = 0
        all_null_counter = 0
        while current_date <= end and all_null_counter < 3:
            i += 1
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"carousel-next")]'))).click()
            df_temp, current_date = self.fares_dataframe(self.driver)
            time.sleep(1)
            print(df_temp)
            all_null_counter += int(df_temp['price'].isnull().all())
            self.df = pd.concat([self.df, df_temp])

    def write_date(self, path='RyanairData/'):
        self.df['origin'] = self.origin
        self.df['destination'] = self.destination
        self.df['fetch_date'] = self.start_date
        self.df.to_csv(path + '{0}_{1}_{2}_{3}.csv'.format(self.origin, self.destination, self.start_date.strftime('%Y%m%d'),self.end_date.replace('-','')), index=False)

    def quit(self):
        self.driver.quit()
