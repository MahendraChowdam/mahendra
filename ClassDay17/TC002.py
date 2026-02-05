from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://letcode.in/alert")

time.sleep(2)   # wait for page to load

driver.find_element(By.ID, "accept").click()

time.sleep(3)   # wait so alert is visible

alert = driver.switch_to.alert
print(alert.text)

time.sleep(2)   # wait before accepting alert
alert.accept()

time.sleep(2)   # wait before closing browser
driver.quit()
