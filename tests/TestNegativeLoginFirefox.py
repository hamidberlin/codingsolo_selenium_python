import unittest  # Importiert das unittest-Modul für strukturiertes Testen
from utils.webdriver_setup import WebDriverSetup  # Importiert die WebDriver-Setup-Klasse
from pages.login_page import LoginPage  # Importiert die LoginPage-Klasse für den Test

class TestNegativeLogin(unittest.TestCase):
    """
    Testklasse für einen fehlgeschlagenen Login-Versuch.
    Verwendet unittest für die Teststruktur.
    """

    def setUp(self):
        """
        Vorbereitungsfunktion, die vor jedem Test ausgeführt wird.
        Startet den WebDriver und navigiert zur Login-Seite.
        """
        print("Starte WebDriver für den Test")
        self.driver = WebDriverSetup.get_driver()  # WebDriver-Instanz aus der Setup-Klasse abrufen
        self.driver.get("https://seleniumkurs.codingsolo.de")  # Zur Login-Seite navigieren
        self.login_page = LoginPage(self.driver)  # Instanziert die LoginPage-Klasse zur Interaktion mit der Seite

    def tearDown(self):
        """
        Aufräumfunktion, die nach jedem Test ausgeführt wird.
        Beendet den WebDriver.
        """
        print("Beende WebDriver nach dem Test")
        self.driver.quit()  # Schließt den WebDriver und den Browser

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
