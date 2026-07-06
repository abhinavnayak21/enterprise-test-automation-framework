from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from config.settings import Settings


class DriverFactory:
    """Factory class to create WebDriver instances."""

    @staticmethod
    def get_driver():
        browser = Settings.get("browser").lower()
        headless = Settings.get("headless")

        if browser != "chrome":
            raise ValueError(f"Unsupported browser: {browser}")

        options = ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            options=options, service=webdriver.ChromeService(ChromeDriverManager().install())
        )

        driver.implicitly_wait(Settings.get("implicit_wait"))

        return driver
