from selenium.webdriver.common.by import By  # Import für das Finden von Elementen mit By-Selektoren
from selenium.webdriver.support.ui import WebDriverWait  # Import für das Warten auf Elemente
from selenium.webdriver.support import expected_conditions as EC  # Import für erwartete Bedingungen
from selenium.webdriver.common.action_chains import ActionChains  # Für Drag-and-Drop Aktionen

class HomePage:
    # Definiert die Selektoren für verschiedene Elemente auf der Seite
    STATUS_MELDUNG = (By.CSS_SELECTOR, "div.portalMessage:nth-child(1)")  # Selektor für eine Statusmeldung
    BTN_HAUPTMENU = (By.ID, "portaltab-burger-menu")  # Selektor für das Hauptmenü (Burger-Menü)
    LINK_SELENIUMTESTAPP = (By.LINK_TEXT, "Selenium Testapplikationen")  # Selektor für den Link zur Selenium-Test-App

    def __init__(self, driver):
        """ Initialisiert die Klasse mit dem Selenium WebDriver. """
        self.driver = driver  # Speichert den WebDriver in der Instanzvariable

    def statusmeldung_auslesen(self):
        """ Liest den Text der Statusmeldung aus und gibt ihn zurück. """
        # Wartet, bis die Statusmeldung sichtbar ist, bevor sie den Text ausliest
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.STATUS_MELDUNG)
        )
        return self.driver.find_element(*self.STATUS_MELDUNG).text  # Findet das Element und gibt seinen Text zurück

    def hauptmenu_aufrufen(self):
        """ Klickt auf das Hauptmenü (Burger-Menü). """
        # Wartet, bis der Button für das Hauptmenü klickbar ist, bevor darauf geklickt wird
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BTN_HAUPTMENU)
        )
        self.driver.find_element(*self.BTN_HAUPTMENU).click()  # Findet das Element und klickt darauf

    def selenium_test_app_anklicken(self):
        """ Klickt auf den Link zur Selenium-Testapplikation. """
        # Wartet, bis der Link zur Testapplikation klickbar ist
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LINK_SELENIUMTESTAPP)
        )
        self.driver.find_element(*self.LINK_SELENIUMTESTAPP).click()  # Findet den Link und klickt darauf
