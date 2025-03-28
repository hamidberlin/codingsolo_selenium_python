import os
import unittest
import logging
from utils.webdriver_setup import WebDriverSetup
from pages.login_page import LoginPage
from datetime import datetime

# Logger wird aus conftest.py automatisch initialisiert
logger = logging.getLogger(__name__)


class TestPositiveLogin(unittest.TestCase):
    """
    Testklasse für einen erfolgreichen Login.
    Jeder Test speichert einen Screenshot (passed & failed).
    """

    def setUp(self):
        """Startet den WebDriver und navigiert zur Login-Seite."""
        logger.info("Starte WebDriver für den Test")
        self.driver = WebDriverSetup.get_driver()
        self.driver.get("https://seleniumkurs.codingsolo.de")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        """Speichert einen Screenshot und beendet den WebDriver."""
        test_failed = any(error for (_, error) in self._outcome.errors if error)

        # Screenshot speichern (egal ob der Test erfolgreich oder fehlgeschlagen ist)
        self.save_screenshot(success=not test_failed)

        if test_failed:
            logger.warning("Test fehlgeschlagen, Screenshot gespeichert unter 'screenshots/failed/'.")
        else:
            logger.info("Test erfolgreich, Screenshot gespeichert unter 'screenshots/passed/'.")

        logger.info("Beende WebDriver nach dem Test")
        self.driver.quit()

    def save_screenshot(self, success=True):
        """Speichert einen Screenshot unter 'screenshots/passed/' oder 'screenshots/failed/'."""
        folder = "screenshots/passed" if success else "screenshots/failed"
        os.makedirs(folder, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = self.id().split(".")[-1]  # Holt den Namen des Tests
        screenshot_filename = os.path.join(folder, f"{test_name}_{timestamp}.png")

        self.driver.save_screenshot(screenshot_filename)
        logger.info(f"Screenshot gespeichert: {screenshot_filename}")

    def test_login_successful(self):
        """Testet einen erfolgreichen Login-Vorgang mit gültigen Zugangsdaten."""
        logger.info("Starte Test: Erfolgreicher Login")

        ## Arrange
        self.login_page.enter_credentials("selenium42", "R5vxI0j60")

        ## Act
        self.login_page.click_login()

        ## Assert
        success_message = self.login_page.get_success_message()

        if success_message:
            logger.info("Erfolgreich eingeloggt: %s", success_message)
        else:
            logger.error("Login fehlgeschlagen! Keine Erfolgsmeldung erhalten.")

        self.assertIn("Willkommen!", success_message, "Erfolgsmeldung nicht gefunden.")

if __name__ == '__main__':
    unittest.main()
