from ui.locators.login_page import LoginPageLocators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page."""

    def enter_username(self, username: str) -> None:
        self.enter_text(
            LoginPageLocators.USERNAME_INPUT,
            username,
        )

    def enter_password(self, password: str) -> None:
        self.enter_text(
            LoginPageLocators.PASSWORD_INPUT,
            password,
        )

    def click_login(self) -> None:
        self.click(
            LoginPageLocators.LOGIN_BUTTON,
        )

    def login(self, username: str, password: str) -> None:
        """Perform login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self) -> bool:
        """Return True if login was successful."""
        return self.is_visible(LoginPageLocators.DASHBOARD_HEADER)
