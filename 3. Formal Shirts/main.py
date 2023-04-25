# main.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from yaml_function import Guru_YAML
import time

yaml_file = 'C:\\Python Project\\Flipkart Project\\3. Formal Shirts\\guru.yaml'

g = Guru_YAML(yaml_file)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.implicitly_wait(10)

driver.get(g.yaml_reader()['url'])

time.sleep(5)

driver.find_element(by=By.XPATH, value=g.yaml_reader()['close_button']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['mobiles']).click()
time.sleep(3)
move_button = driver.find_element(by=By.XPATH, value=g.yaml_reader()['men'])
action=ActionChains(driver)
action.move_to_element(move_button).perform()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['formal_shirts']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['gender']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['gender_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['size']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['size_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['brand']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['brand_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['sleeves']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['sleeves_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['theme']).click()
driver.find_element(by=By.XPATH, value=g.yaml_reader()['theme_selection']).click()
time.sleep(3)
driver.find_element(by=By.XPATH, value=g.yaml_reader()['men_formal_shirt']).click()
time.sleep(10)
