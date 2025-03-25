import unittest  # Importiert das unittest-Modul für das strukturierte Testen
from utils.webdriver_setup import WebDriverSetup  # Importiert die WebDriver-Setup-Klasse
from pages.login_page import LoginPage  # Importiert die LoginPage-Klasse für den Test

class TestPositiveLogin(unittest.TestCase):
    """
    Testklasse für einen erfolgreichen Login.
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

    def test_login_successful(self):
        """
        Testet einen erfolgreichen Login-Vorgang mit gültigen Zugangsdaten.
        Überprüft, ob eine Erfolgsmeldung angezeigt wird.
        """
        print("Starte Test: Erfolgreicher Login")
        self.login_page.enter_username("selenium42")  # Gültigen Benutzernamen eingeben
        self.login_page.enter_password("R5vxI0j60")  # Gültiges Passwort eingeben
        self.login_page.click_login()  # Login-Button klicken

        success_message = self.login_page.get_success_message()  # Erfolgsmeldung abrufen
        self.assertIn("Willkommen!", success_message)  # Überprüfen, ob die Erfolgsmeldung korrekt ist

if __name__ == '__main__':
    unittest.main()  # Führt die Tests aus, wenn das Skript direkt gestartet wird
