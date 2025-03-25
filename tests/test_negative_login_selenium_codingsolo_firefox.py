import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Import für Expected Conditions

class TestNegativeLoginCodingSoloFirefox(unittest.TestCase):

    def setUp(self):
        """ Setup: Startet den WebDriver und öffnet die Login-Seite. """
        print("Initialisiere WebDriver für den Test")
        self.driver = webdriver.Firefox()
        self.driver.get("https://seleniumkurs.codingsolo.de")

    def tearDown(self):
        """ Cleanup: Beendet den WebDriver nach dem Test. """
        print("Nach dem Test. Ich räume auf")
        self.driver.quit()

    def test_negative_login(self):
        """ Test: Negativer Login-Versuch mit falschen Anmeldedaten. """
        print("Starte test_login_fehlschlag")

        ## Arrange - Eingabe von falschen Login-Daten
        wait = WebDriverWait(self.driver, 10)  # Warte maximal 10 Sekunden auf Elemente
        wait.until(EC.presence_of_element_located((By.ID, "__ac_name"))).send_keys("test")
        wait.until(EC.presence_of_element_located((By.ID, "__ac_password"))).send_keys("1234")

        ## Act - Login-Button klicken
        self.driver.find_element(By.XPATH, "//input[@name='buttons.login']").click()

        ## Assert - Fehlernachricht prüfen (warten, bis sie sichtbar ist)
        fehlerMeldung = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='portalMessage error']"))).text
        self.assertTrue('Anmeldung fehlgeschlagen' in fehlerMeldung, "Fehlermeldung nicht gefunden!")

if __name__ == '__main__':
    unittest.main()
