from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Locators for the OrangeHRM Login Page."""

    USERNAME_INPUT = (
        By.NAME,
        "username",
    )

    PASSWORD_INPUT = (
        By.NAME,
        "password",
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "button[type='submit']",
    )

    DASHBOARD_HEADER = (
        By.XPATH,
        "//h6[text()='Dashboard']",
    )
