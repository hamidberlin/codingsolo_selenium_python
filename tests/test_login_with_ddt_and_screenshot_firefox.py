import os
import unittest
import logging
from ddt import ddt, data, unpack
from utils.webdriver_setup import WebDriverSetup
from pages.login_page import LoginPage
from datetime import datetime

# Logger wird aus conftest.py automatisch initialisiert
logger = logging.getLogger(__name__)

@ddt
class TestLogin(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.driver = None
        self.login_page = None

    def setUp(self):
        """Startet den WebDriver vor jedem Test."""
        logger.debug("Starte WebDriver für den Test")
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

    @data(
        ("selenium42", "R5vxI0j60"),  # Gültige Anmeldedaten
        ("testuser1", "password123"),  # Ungültige Anmeldedaten
        ("admin", "admin123"),  # Weitere gültige Anmeldedaten
    )
    @unpack
    def test_login(self, username, password):
        """Testet Login mit verschiedenen Zugangsdaten."""

        logger.info(f"Teste Login mit Benutzer: {username}")

        # Arrange
        self.login_page.enter_credentials(username, password)

        # Act
        self.login_page.click_login()

        # Assert: Überprüfe Fehlermeldung bei falschen Anmeldedaten
        error_message = self.login_page.get_error_message()
        if error_message:
            logger.warning("Fehlermeldung erhalten: %s", error_message)
            self.assertIn("Anmeldung fehlgeschlagen", error_message)
        else:
            success_message = self.login_page.get_success_message()
            if success_message:
                logger.info("Erfolgreich eingeloggt: %s", success_message)
                self.assertIn("Willkommen!", success_message)
            else:
                self.fail("Es wurde keine Erfolgsnachricht angezeigt.")


if __name__ == '__main__':
    unittest.main()
