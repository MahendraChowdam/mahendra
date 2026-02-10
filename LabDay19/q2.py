from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

GRID_URL = "http://localhost:4444"   # Selenium Grid 4

def get_driver(browser_name):

    if browser_name == "chrome":
        options = ChromeOptions()

    elif browser_name == "firefox":
        options = FirefoxOptions()

    elif browser_name == "edge":
        options = EdgeOptions()

    else:
        raise ValueError("Unsupported browser")

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    return driver


browsers = ["chrome", "firefox", "edge"]

for browser in browsers:
    driver = get_driver(browser)

    driver.get("https://example.com")

    # Verify title
    assert "Example Domain" in driver.title

    # Get browser & platform details from capabilities
    caps = driver.capabilities
    browser_name = caps.get("browserName")
    platform_name = caps.get("platformName")

    print(f"Browser: {browser_name}")
    print(f"Platform: {platform_name}")
    print("Title Verified Successfully\n")

    driver.quit()
