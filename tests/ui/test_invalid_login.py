import pytest

from config.settings import Settings
from test_data.login_data import LoginData
from ui.pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password",
    LoginData.INVALID_USERS,
)
def test_invalid_login(driver, username, password):
    """Verify login fails with invalid credentials."""

    driver.get(Settings.get("base_url"))

    login_page = LoginPage(driver)

    login_page.login(username, password)

    assert not login_page.is_login_successful()
