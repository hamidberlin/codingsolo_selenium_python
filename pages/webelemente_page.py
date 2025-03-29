from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebElementePage:
    """
    Diese Klasse verwaltet die Web-Elemente für Checkboxen und Radiobuttons auf einer Webseite.
    Sie ermöglicht das Anklicken und Überprüfen des Status der jeweiligen Elemente.
    """

    # Selektoren für die Checkboxen anhand ihrer ID
    CHECK_BOX1 = (By.ID, "checkBoxOption1")  # Erste Checkbox
    CHECK_BOX2 = (By.ID, "checkBoxOption2")  # Zweite Checkbox
    CHECK_BOX3 = (By.ID, "checkBoxOption3")  # Dritte Checkbox

    # Selektoren für die Radiobuttons anhand des CSS-Selektors und des Werts
    RADIO_BTN1 = (By.CSS_SELECTOR, "input[value='radio1']")  # Erster Radiobutton
    RADIO_BTN2 = (By.CSS_SELECTOR, "input[value='radio2']")  # Zweiter Radiobutton
    RADIO_BTN3 = (By.CSS_SELECTOR, "input[value='radio3']")  # Dritter Radiobutton

    def __init__(self, driver):
        """ Konstruktor speichert die WebDriver-Instanz. """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Setze eine Wartezeit von bis zu 10 Sekunden

    # Methoden zum Anklicken der Checkboxen
    def checkbox1_anklicken(self):
        """ Klickt auf die erste Checkbox. """
        element = self.wait.until(EC.element_to_be_clickable(self.CHECK_BOX1))  # Warte, bis das Element klickbar ist
        element.click()

    def checkbox2_anklicken(self):
        """ Klickt auf die zweite Checkbox. """
        element = self.wait.until(EC.element_to_be_clickable(self.CHECK_BOX2))  # Warte, bis das Element klickbar ist
        element.click()

    def checkbox3_anklicken(self):
        """ Klickt auf die dritte Checkbox. """
        element = self.wait.until(EC.element_to_be_clickable(self.CHECK_BOX3))  # Warte, bis das Element klickbar ist
        element.click()

    # Methoden zum Überprüfen, ob die Checkboxen ausgewählt sind
    def checkbox1_status_auslesen(self):
        """ Gibt den aktuellen Status der ersten Checkbox zurück (True, wenn ausgewählt). """
        element = self.wait.until(EC.presence_of_element_located(self.CHECK_BOX1))  # Warte, bis das Element vorhanden ist
        return element.is_selected()

    def checkbox2_status_auslesen(self):
        """ Gibt den aktuellen Status der zweiten Checkbox zurück (True, wenn ausgewählt). """
        element = self.wait.until(EC.presence_of_element_located(self.CHECK_BOX2))  # Warte, bis das Element vorhanden ist
        return element.is_selected()

    def checkbox3_status_auslesen(self):
        """ Gibt den aktuellen Status der dritten Checkbox zurück (True, wenn ausgewählt). """
        element = self.wait.until(EC.presence_of_element_located(self.CHECK_BOX3))  # Warte, bis das Element vorhanden ist
        return element.is_selected()

    # Methoden zum Aktivieren der Radiobuttons
    def radio_btn1_aktivieren(self):
        """ Aktiviert den ersten Radiobutton. """
        element = self.wait.until(EC.element_to_be_clickable(self.RADIO_BTN1))  # Warte, bis das Element klickbar ist
        element.click()

    def radio_btn2_aktivieren(self):
        """ Aktiviert den zweiten Radiobutton. """
        element = self.wait.until(EC.element_to_be_clickable(self.RADIO_BTN2))  # Warte, bis das Element klickbar ist
        element.click()

    def radio_btn3_aktivieren(self):
        """ Aktiviert den dritten Radiobutton. """
        element = self.wait.until(EC.element_to_be_clickable(self.RADIO_BTN3))  # Warte, bis das Element klickbar ist
        element.click()

    # Methoden zum Überprüfen, ob ein Radiobutton ausgewählt ist
    def radio_btn1_status_auslesen(self):
        """ Gibt zurück, ob der erste Radiobutton aktiv ist. """
        element = self.wait.until(EC.presence_of_element_located(self.RADIO_BTN1))  # Warte, bis das Element vorhanden ist
        return element.is_selected()

    def radio_btn2_status_auslesen(self):
        """ Gibt zurück, ob der zweite Radiobutton aktiv ist. """
        element = self.wait.until(EC.presence_of_element_located(self.RADIO_BTN2))  # Warte, bis das Element vorhanden ist
        return element.is_selected()

    def radio_btn3_status_auslesen(self):
        """ Gibt zurück, ob der dritte Radiobutton aktiv ist. """
        element = self.wait.until(EC.presence_of_element_located(self.RADIO_BTN3))  # Warte, bis das Element vorhanden ist
        return element.is_selected()
