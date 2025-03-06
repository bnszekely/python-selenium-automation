from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# populate sign in field
search = driver.find_element(By.ID, 'account-sign-in').click()

# wait for 4 sec
sleep(4)

# click sign in button
driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()

# wait for 5 sec
sleep(5)

# verify search results
driver.find_element(By.XPATH, "//*[contains(., 'Sign in')]")



sleep(10)
