from config.settings import Settings


def test_open_application(driver):
    driver.get(Settings.get("base_url"))

    assert "OrangeHRM" in driver.title
