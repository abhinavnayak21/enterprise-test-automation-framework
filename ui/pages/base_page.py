from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.settings import Settings
from utils.logger import get_logger


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WebDriverWait(
            driver,
            Settings.get("explicit_wait"),
        )

    def click(self, locator: tuple) -> None:
        """Click on an element."""
        self.logger.info(f"Clicking element: {locator}")

        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator: tuple, text: str) -> None:
        """Enter text into an input field."""
        self.logger.info(f"Entering text into: {locator}")

        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_title(self) -> str:
        """Return page title."""
        return self.driver.title

    def get_current_url(self) -> str:
        """Return current page URL."""
        return self.driver.current_url

    def is_visible(self, locator: tuple) -> bool:
        """Check whether an element is visible."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
