import pytest

from utils.driver_factory import DriverFactory
from utils.screenshot import ScreenshotManager


@pytest.fixture(scope="function")
def driver():
    """
    Initialize and quit WebDriver for each test.
    """
    driver = DriverFactory.get_driver()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture a screenshot on test failure.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            ScreenshotManager.save(driver, item.name)
