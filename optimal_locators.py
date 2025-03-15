from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find.element(By.XPATH, "//h1[@class='a-spacing-small']")
driver.find.element(By.ID, "ap_email")
driver.find.element(By.ID, "continue")
driver.find.element(By.XPATH, "//*[text()='Conditions of Use']")
driver.find.element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href,'privacy_notice')]")
driver.find.element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find.element(By.ID, "auth-fpp-link-bottom")
driver.find.element(By.ID, "ap-other-signin-issues-link")
driver.find.element(By.ID, "createAccountSubmit")


driver.find.element(By.CSS_SELECTOR, ".a-icon-logo")
driver.find.element(By.XPATH, "//h1[contains(text(),'Create account')]")
driver.find.element(By.ID, "ap_customer_name")
driver.find.element(By.ID, "ap_email")
driver.find.element(By.ID, "ap_password")
driver.find.element(By.XPATH, "//div[contains(text(),'Passwords must be')]")
driver.find.element(By.ID, "ap_password_check")
driver.find.element(By.ID, "continue")
driver.find.element(By.XPATH, "//*[text()='Conditions of Use']")
driver.find.element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href,'privacy_notice')]")
driver.find.element(By.CSS_SELECTOR, ".a-link-emphasis")


