from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------------
# Launch Browser
# -------------------------------
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

# -------------------------------
# 1. Open iframe page
# -------------------------------
driver.get("https://letcode.in/frame")

# -------------------------------
# 2. Switch to iframe and enter text
# -------------------------------
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

driver.find_element(By.NAME, "fname").send_keys("Saritha")
driver.find_element(By.NAME, "lname").send_keys("R")

print("Entered text inside iframe")

# -------------------------------
# 3. Switch back to main content
# -------------------------------
driver.switch_to.default_content()

insight = driver.find_element(By.XPATH, "//p[text()=' Insight ']").is_displayed()
print("Insight is displayed:", insight)

# -------------------------------
# 4. Open a new window / tab
# -------------------------------
driver.execute_script("window.open('https://letcode.in/windows');")

parent_window = driver.current_window_handle
all_windows = driver.window_handles

# -------------------------------
# 5. Switch between windows and print titles
# -------------------------------
for window in all_windows:
    driver.switch_to.window(window)
    print("Window Title:", driver.title)

# -------------------------------
# 6. Close child window and return to parent
# -------------------------------
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        driver.close()

driver.switch_to.window(parent_window)
print("Returned to parent window")

time.sleep(3)
driver.quit()
