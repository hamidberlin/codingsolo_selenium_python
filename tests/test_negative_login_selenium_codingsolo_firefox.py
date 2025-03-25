import unittest
from utils.webdriver_setup import WebDriverSetup
from pages.login_page import LoginPage

class TestNegativeLogin(unittest.TestCase):

    def setUp(self):
        print("Starte WebDriver für den Test")
        self.driver = WebDriverSetup.get_driver()
        self.driver.get("https://seleniumkurs.codingsolo.de")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        print("Beende WebDriver nach dem Test")
        self.driver.quit()

    def test_login_failed(self):
        print("Starte Test: Fehlgeschlagener Login")
        self.login_page.enter_username("test")
        self.login_page.enter_password("1234")
        self.login_page.click_login()
        error_message = self.login_page.get_error_message()
        self.assertIn("Anmeldung fehlgeschlagen", error_message)

if __name__ == '__main__':
    unittest.main()
