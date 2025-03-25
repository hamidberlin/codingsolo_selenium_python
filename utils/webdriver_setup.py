from selenium import webdriver

class WebDriverSetup:
    @staticmethod
    def get_driver():
        driver = webdriver.Firefox()
        driver.maximize_window()
        return driver
