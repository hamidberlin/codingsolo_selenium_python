from selenium import webdriver  # Importiert das Selenium-WebDriver-Modul


class WebDriverSetup:
    """
    Eine Hilfsklasse zur Einrichtung des WebDrivers.
    Stellt eine Methode bereit, um eine neue WebDriver-Instanz zu erstellen.
    """

    @staticmethod
    def get_driver():
        """
        Erstellt und gibt eine neue WebDriver-Instanz für Firefox zurück.
        Das Browserfenster wird maximiert, um eine optimale Darstellung sicherzustellen.

        :return: Eine WebDriver-Instanz für Firefox
        """
        driver = webdriver.Firefox()  # Erstellt eine neue WebDriver-Instanz für Firefox
        driver.maximize_window()  # Maximiert das Browserfenster
        return driver  # Gibt die WebDriver-Instanz zurück
