from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------------------------
# VARIABLES (defined first)
# ---------------------------
url = "https://tutorialsninja.com/demo/"
first_name_33 = "A" * 33
last_name_33 = "B" * 33
valid_email = "testuser123@gmail.com"
telephone = "9876543210"
address1 = "Main Street 123"
city = "Hyderabad"
postcode = "500001"

# ---------------------------
# LAUNCH FIREFOX
# ---------------------------
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

driver.get(url)
driver.maximize_window()

# ---------------------------
# PART 1: Launch Application
# ---------------------------

# Verify Title
assert "Your Store" in driver.title
print("Title verified")

# Click My Account dropdown
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//span[normalize-space()='My Account']"))
).click()

# Click Register
wait.until(EC.element_to_be_clickable(
    (By.LINK_TEXT, "Register"))
).click()

# Verify Register page using URL and First Name field
assert "route=account/register" in driver.current_url
wait.until(EC.presence_of_element_located(
    (By.ID, "input-firstname")
))
print("Register Account page loaded")

# Click Continue without agreeing Privacy Policy
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

# Verify warning message
warning = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, ".alert-danger"))).text
assert "Warning: You must agree to the Privacy Policy!" in warning
print("Privacy Policy warning verified")

# ---------------------------
# PART 2: Your Personal Details
# ---------------------------

# First Name – 33 characters
driver.find_element(By.ID, "input-firstname").send_keys(first_name_33)
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

error_fn = driver.find_element(
    By.XPATH, "//input[@id='input-firstname']/following-sibling::div"
).text
assert "First Name must be between 1 and 32 characters!" in error_fn
print("First Name validation verified")

# Last Name – 33 characters
driver.find_element(By.ID, "input-lastname").send_keys(last_name_33)
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

error_ln = driver.find_element(
    By.XPATH, "//input[@id='input-lastname']/following-sibling::div"
).text
assert "Last Name must be between 1 and 32 characters!" in error_ln
print("Last Name validation verified")

# Valid Email
driver.find_element(By.ID, "input-email").send_keys(valid_email)

# Telephone (3–32 characters)
driver.find_element(By.ID, "input-telephone").send_keys(telephone)
print("Personal details entered")

# ---------------------------
# PART 3: Your Address
# ---------------------------

# Scroll to bottom so address fields are visible
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# Address 1 (3–128)
wait.until(EC.visibility_of_element_located(
    (By.ID, "input-address-1"))
).send_keys(address1)

# City (2–128)
driver.find_element(By.ID, "input-city").send_keys(city)

# Post Code (2–10)
driver.find_element(By.ID, "input-postcode").send_keys(postcode)

print("Address details entered")

# ---------------------------
# END TEST
# ---------------------------
time.sleep(3)
driver.quit()
