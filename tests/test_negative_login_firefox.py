import logging
import os
import unittest  # Importiert das unittest-Modul für strukturiertes Testen
from datetime import datetime

from utils.webdriver_setup import WebDriverSetup  # Importiert die WebDriver-Setup-Klasse
from pages.login_page import LoginPage  # Importiert die LoginPage-Klasse für den Test


# Logger wird aus conftest.py automatisch initialisiert
logger = logging.getLogger(__name__)


class TestNegativeLogin(unittest.TestCase):
    """
    Testklasse für einen fehlgeschlagenen Login-Versuch.
    Verwendet unittest für die Teststruktur.
    """

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self._outcome = None

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

    def test_login_failed(self):
        """
        Testet einen fehlgeschlagenen Login-Versuch mit falschen Zugangsdaten.
        Überprüft, ob eine Fehlermeldung angezeigt wird.
        """
        print("Starte Test: Fehlgeschlagener Login")

        ## Arrange
        #self.login_page.enter_username("test")
        #self.login_page.enter_password("1234")
        self.login_page.enter_credentials("test", "1234")

        ## Act
        self.login_page.click_login()

        ## Asssert
        error_message = self.login_page.get_error_message()  # Fehlermeldung abrufen
        self.assertIn("Anmeldung fehlgeschlagen", error_message)  # Überprüfen, ob die Fehlermeldung korrekt ist

if __name__ == '__main__':
    unittest.main()  # Führt die Tests aus, wenn das Skript direkt gestartet wird
