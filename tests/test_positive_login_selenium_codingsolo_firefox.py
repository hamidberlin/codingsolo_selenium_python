import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Import für Expected Conditions


class TestPositiveLoginCodingSoloFirefox(unittest.TestCase):

    def setUp(self):
        """ Setup-Methode: Startet den WebDriver und öffnet die Login-Seite. """
        print("Initialisiere WebDriver für den Test")
        self.driver = webdriver.Firefox()  # Öffnet den Firefox-Browser
        self.driver.get("https://seleniumkurs.codingsolo.de")  # Navigiert zur Test-Webseite

    def tearDown(self):
        """ Cleanup-Methode: Schließt den WebDriver nach dem Test. """
        print("Nach dem Test. Ich räume auf")
        self.driver.quit()  # Beendet den gesamten WebDriver-Prozess und schließt den Browser

    def test_login(self):
        """ Testfall: Erfolgreicher Login mit gültigen Zugangsdaten. """
        print("Starte test_login")

        ## Arrange - Vorbereitung: Eingabe der Login-Daten
        wait = WebDriverWait(self.driver, 10)  # Warte maximal 10 Sekunden auf Elemente

        # Warte auf das Eingabefeld für den Benutzernamen und gebe "selenium42" ein
        wait.until(EC.presence_of_element_located((By.ID, "__ac_name"))).send_keys("selenium42")

        # Warte auf das Eingabefeld für das Passwort und gebe "R5vxI0j60" ein
        wait.until(EC.presence_of_element_located((By.ID, "__ac_password"))).send_keys("R5vxI0j60")

        ## Act - Handlung: Login-Button anklicken
        self.driver.find_element(By.XPATH, "//input[@name='buttons.login']").click()

        ## Assert - Überprüfung: Willkommensmeldung erscheint nach erfolgreichem Login
        # Warte darauf, dass die Statusmeldung sichtbar ist, dann speichere den Text
        statusMeldung = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='portalMessage info']"))).text

        # Prüfe, ob die Willkommensmeldung im Text enthalten ist
        self.assertTrue('Willkommen!' in statusMeldung, "Login fehlgeschlagen - 'Willkommen!' nicht gefunden!")


if __name__ == '__main__':
    unittest.main()
