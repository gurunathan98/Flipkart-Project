# main.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from yaml_function import Guru_YAML
import time

yaml_file = 'C:\\Python Project\\Flipkart Project\\2. Mobile Phone\\guru.yaml'

g = Guru_YAML(yaml_file)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.implicitly_wait(10)

driver.get(g.yaml_reader()['url'])

time.sleep(5)

driver.find_element(by=By.XPATH, value=g.yaml_reader()['close_button']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['mobile']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['brand']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['internal_storage']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['internal_storage_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['screen_size']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['screen_size_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['network_type']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['network_type_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['iphone_14']).click()
time.sleep(5)
