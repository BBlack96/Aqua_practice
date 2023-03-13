import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для запуска тестов с использованием селеноида
@pytest.fixture(scope="function")
def selenoid_fixture():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "110.0",
        "selenoid:options": {
            "enableVideo": False,
            "enableVNC": True
        }
    }
    options = webdriver.ChromeOptions()
    options.add_extension("/home/demo/drivers/adblock.crx")
    driver = webdriver.Remote(
        command_executor="http://127.0.1.1:4444/wd/hub",
        desired_capabilities=capabilities,
        options=options
    )
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    yield driver
    driver.quit()
