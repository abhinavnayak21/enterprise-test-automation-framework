from datetime import datetime
from pathlib import Path


class ScreenshotManager:
    """Utility class for capturing screenshots."""

    SCREENSHOT_DIR = Path("screenshots")

    @classmethod
    def save(cls, driver, test_name: str) -> str:
        """Save a screenshot and return its path."""

        cls.SCREENSHOT_DIR.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"{test_name}_{timestamp}.png"

        filepath = cls.SCREENSHOT_DIR / filename

        driver.save_screenshot(str(filepath))

        return str(filepath)
