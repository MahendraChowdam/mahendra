import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Day20.driverfactory import get_driver

@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_google_search(browser):
    driver = get_driver(browser)
    driver.get("https://www.google.com")

    search_box = driver.find_element("name", "q")
    search_box.send_keys("selenium grid")
    search_box.submit()

    # ✅ Wait until title contains search text
    WebDriverWait(driver, 20).until(
        EC.title_contains("selenium grid")
    )

    assert "selenium grid" in driver.title.lower()
    time.sleep(5)
    driver.quit()
