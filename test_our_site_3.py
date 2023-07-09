from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def open_page(driver,url):
    driver.get(url)

def get_element_by_id(driver,locator):
    driver.find_element(By.ID,locator)

def element_click(driver,locator):
    element = get_element_by_id(driver,locator)
    element.click()

def element_send_keys(driver,locator,text):
    element = get_element_by_id(driver,locator)
    element.send_keys(text)


driver = get_driver()
open_page(driver,URL)

element_send_keys(driver,'user-name',LOGIN)
element_send_keys(driver,'password',PASSWORD)

element_click(driver,'login-button')
