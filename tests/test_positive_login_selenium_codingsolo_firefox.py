import unittest
from utils.webdriver_setup import WebDriverSetup
from pages.login_page import LoginPage

class TestPositiveLogin(unittest.TestCase):

    def setUp(self):
        print("Starte WebDriver für den Test")
        self.driver = WebDriverSetup.get_driver()
        self.driver.get("https://seleniumkurs.codingsolo.de")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        print("Beende WebDriver nach dem Test")
        self.driver.quit()

    def test_login_successful(self):
        print("Starte Test: Erfolgreicher Login")
        self.login_page.enter_username("selenium42")
        self.login_page.enter_password("R5vxI0j60")
        self.login_page.click_login()
        success_message = self.login_page.get_success_message()
        self.assertIn("Willkommen!", success_message)

if __name__ == '__main__':
    unittest.main()
