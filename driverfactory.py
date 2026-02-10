from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

GRID_URL = "http://192.168.1.166:4444/wd/hub"

def get_driver(browser):
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )

    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    return driver
