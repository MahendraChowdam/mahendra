import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------- CONFIGURATION ----------------
class Config:
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME = "Admin"
    PASSWORD = "admin123"
    IMPLICIT_WAIT = 10


# ---------------- BASE PAGE (Reusable Methods) ----------------
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text


# ---------------- PAGE OBJECT (Login Page) ----------------
class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_TEXT = (By.XPATH, "//h6[text()='Dashboard']")

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_dashboard_text(self):
        return self.get_text(self.DASHBOARD_TEXT)


# ---------------- PYTEST FIXTURE ----------------
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()


# ---------------- TEST SCRIPT ----------------
def test_login_valid(setup):
    login_page = LoginPage(setup)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    result = login_page.get_dashboard_text()
    print("Login Result:", result)

    assert result == "Dashboard"
