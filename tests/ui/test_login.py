from config.settings import Settings
from ui.locators.login_page import LoginPageLocators
from ui.pages.login_page import LoginPage


def test_valid_login(driver):
    """Verify that a user can log in with valid credentials."""

    driver.get(Settings.get("base_url"))

    login_page = LoginPage(driver)

    login_page.login(
        "Admin",
        "admin123",
    )

    assert login_page.is_visible(LoginPageLocators.DASHBOARD_HEADER)
