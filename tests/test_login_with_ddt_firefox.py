import unittest
from ddt import ddt, data, unpack
from utils.webdriver_setup import WebDriverSetup
from pages.login_page import LoginPage

@ddt  # Aktiviert Data-Driven-Tests
class TestLogin(unittest.TestCase):

    def setUp(self):
        """Startet den WebDriver vor jedem Test."""
        print("Starte WebDriver für den Test")
        self.driver = WebDriverSetup.get_driver()
        self.driver.get("https://seleniumkurs.codingsolo.de")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        """Beendet den WebDriver nach jedem Test."""
        print("Beende WebDriver nach dem Test")
        self.driver.quit()

    @data(
        ("selenium42", "R5vxI0j60"),  # Gültige Anmeldedaten
        ("testuser1", "password123"),  # Ungültige Anmeldedaten
        ("admin", "admin123"),  # Weitere gültige Anmeldedaten
    )
    @unpack
    def test_login(self, username, password):
        """Testet Login mit verschiedenen Zugangsdaten."""

        print(f"Teste Login mit Benutzer: {username}")

        # Arrange
        self.login_page.enter_credentials(username, password)

        # Act
        self.login_page.click_login()

        # Assert: Überprüfe Fehlermeldung bei falschen Anmeldedaten
        error_message = self.login_page.get_error_message()
        if error_message:
            print("Fehlermeldung erhalten:", error_message)
            # Überprüfe, ob ein Teil der Fehlermeldung enthalten ist
            self.assertIn("Anmeldung fehlgeschlagen", error_message)
        else:
            # Assert: Erfolgreicher Login bei gültigen Anmeldedaten
            success_message = self.login_page.get_success_message()
            if success_message:
                print("Erfolgreich eingeloggt:", success_message)
                self.assertIn("Willkommen!", success_message)  # Überprüfe Begrüßungsnachricht
            else:
                self.fail("Es wurde keine Erfolgsnachricht angezeigt.")

if __name__ == '__main__':
    unittest.main()
