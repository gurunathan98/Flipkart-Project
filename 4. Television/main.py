# main.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from yaml_function import Guru_YAML
import time

yaml_file = 'C:\\Python Project\\Flipkart Project\\4. Television\\guru.yaml'

g = Guru_YAML(yaml_file)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.implicitly_wait(10)

driver.get(g.yaml_reader()['url'])

time.sleep(5)

driver.find_element(by=By.XPATH, value=g.yaml_reader()['close_button']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['mobiles']).click()
move_button = driver.find_element(by=By.XPATH, value=g.yaml_reader()['tv_and_appliances'])
action=ActionChains(driver)
action.move_to_element(move_button).perform()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['television']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['sony_tv']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['screen_size']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['screen_size_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['screen_type']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['screen_type_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['customer_rating']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['price_range']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['sony_bravia']).click()
time.sleep(5)
driver.close()