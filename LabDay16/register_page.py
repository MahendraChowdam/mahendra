from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

# 1. Find elements using different locators and enter text

# By ID
driver.find_element(By.ID, "input-firstname").send_keys("Mahendra")

# By NAME
driver.find_element(By.NAME, "lastname").send_keys("Chowdam")

# By CSS Selector
driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys("mahi890@gmail.com")

# By XPATH
driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("9876543210")

# By CLASS NAME (demo purpose)
driver.find_element(By.CLASS_NAME, "form-control").send_keys("Dummy")

# By XPATH (password)
driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("Test@123")

# By CSS Selector (confirm password)
driver.find_element(By.CSS_SELECTOR, "#input-confirm").send_keys("Test@123")

# 2. Click checkbox and submit
driver.find_element(By.XPATH, "//input[@name='agree']").click()
driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()

time.sleep(3)

# 3. Validate message
msg = driver.find_element(By.CSS_SELECTOR, "#content h1").text
print("Message is:", msg)

if msg == "Your Account Has Been Created!":
    print("Test Passed")
else:
    print("Test Failed")

driver.quit()


