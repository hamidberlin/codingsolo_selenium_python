import unittest

from selenium import webdriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.webdriver_setup import WebDriverSetup


class TestHomePageFireFox(unittest.TestCase):

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

    def test_homePage(self):
        print("Starte test_homepage ")

        ##Arrange

        loginPage = LoginPage(self.driver)
        loginPage.enter_username("selenium42")
        loginPage.enter_password("R5vxI0j60")
        ##Act

        loginPage.click_login()

        ##Assert

        homePage = HomePage(self.driver)

        success_message = homePage.statusmeldung_auslesen()
        self.assertTrue('Willkommen' in success_message)

if __name__ == '__main__':
        unittest.main()