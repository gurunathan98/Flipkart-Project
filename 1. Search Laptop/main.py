# main.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from yaml_function import Guru_YAML
import time

yaml_file = 'C:\\Python Project\\Flipkart Project\\1. Search Laptop\\guru.yaml'

g = Guru_YAML(yaml_file)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.implicitly_wait(10)

driver.get(g.yaml_reader()['url'])

time.sleep(5)

driver.find_element(by=By.XPATH, value=g.yaml_reader()['close_button']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['search_box']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['search_box']).send_keys(g.yaml_reader()['search_box_input'])
driver.find_element(by=By.XPATH, value=g.yaml_reader()['search_box']).send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['screen_size']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['screen_size_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['weight']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['weight_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['ssd_capacity']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['ssd_capacity_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['price_range']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['apple_macbook_pro']).click()
time.sleep(10)
