import pytest

from utils.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def driver():
    """
    Initialize and quit WebDriver for each test.
    """
    driver = DriverFactory.get_driver()

    yield driver

    driver.quit()
