from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com")
print(driver.title)

driver.get("https://www.iana.org/domains/example")
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

driver.refresh()
print(driver.title)

driver.quit()


