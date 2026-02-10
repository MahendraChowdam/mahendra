from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# 1️⃣ IMPLICIT WAIT (applies to all elements)
driver.implicitly_wait(10)  # seconds

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

print("Implicit wait applied: 10 seconds")

# 2️⃣ EXPLICIT WAIT (wait until element is clickable)
try:
    enable_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Enable']"))
    )
    print("Explicit Wait: Enable button is clickable")
    enable_button.click()
except TimeoutException:
    print("Explicit Wait: Element not clickable within time")

# 3️⃣ FLUENT WAIT (custom polling interval)
try:
    fluent_wait = WebDriverWait(
        driver,
        timeout=20,
        poll_frequency=2,  # polling every 2 seconds
        ignored_exceptions=[NoSuchElementException]
    )

    text_box = fluent_wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
    )

    print("Fluent Wait: Text box is available for interaction")
    text_box.send_keys("Selenium Waits Demo")

except TimeoutException:
    print("Fluent Wait: Element not found within time")

time.sleep(3)
driver.quit()
