from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAppPage:
    # Selektoren für die verschiedenen Navigationselemente auf der Test-Applikationsseite
    BTN_HAUPTMENU = (By.ID, "portaltab-burger-menu")  # Hauptmenü-Button
    LINK_TESTFORM1 = (By.LINK_TEXT, "Selenium Test Form1")  # Link zum Testformular 1
    LINK_DragAndDrop = (By.LINK_TEXT, "Drag and Drop Beispiel")  # Link zum Drag-and-Drop-Beispiel
    LINK_IFRAMEBEISPIEL = (By.LINK_TEXT, "IFrame Beispiel")  # Link zum IFrame-Beispiel
    LINK_WEBELEMENTE = (By.LINK_TEXT, "Web Elemente")  # Link zur Web-Elemente-Testseite
    LINK_KATZENSUCHE = (By.LINK_TEXT, "Katzensuche Testseite (AJAX)")  # Link zur Katzensuche-Testseite mit AJAX

    def __init__(self, driver):
        """ Konstruktor speichert die WebDriver-Instanz. """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Wartezeit von 10 Sekunden

    def hauptmenu_aufrufen(self):
        """ Öffnet das Hauptmenü durch Klicken auf den entsprechenden Button. """
        # Warten, bis der Button sichtbar ist, bevor geklickt wird
        menu_button = self.wait.until(EC.visibility_of_element_located(self.BTN_HAUPTMENU))
        menu_button.click()

    def test_form1_anklicken(self):
        """ Klickt auf den Link zur Testformular-1-Seite. """
        # Warten, bis der Link sichtbar ist, bevor geklickt wird
        link_testform1 = self.wait.until(EC.element_to_be_clickable(self.LINK_TESTFORM1))
        link_testform1.click()

    def drag_and_drop_anklicken(self):
        """ Klickt auf den Link zur Drag-and-Drop-Testseite. """
        # Warten, bis der Link sichtbar ist, bevor geklickt wird
        link_drag_and_drop = self.wait.until(EC.element_to_be_clickable(self.LINK_DragAndDrop))
        link_drag_and_drop.click()

    def iframe_beispiel_anklicken(self):
        """ Klickt auf den Link zum IFrame-Testbeispiel. """
        # Warten, bis der Link sichtbar ist, bevor geklickt wird
        link_iframe = self.wait.until(EC.element_to_be_clickable(self.LINK_IFRAMEBEISPIEL))
        link_iframe.click()

    def web_elemente_anklicken(self):
        """ Klickt auf den Link zur Testseite für Web-Elemente. """
        # Warten, bis der Link sichtbar ist, bevor geklickt wird
        link_web_elemente = self.wait.until(EC.element_to_be_clickable(self.LINK_WEBELEMENTE))
        link_web_elemente.click()

    def katzensuche_anklicken(self):
        """ Klickt auf den Link zur Katzensuche-Testseite mit AJAX. """
        # Warten, bis der Link sichtbar ist, bevor geklickt wird
        link_katzensuche = self.wait.until(EC.element_to_be_clickable(self.LINK_KATZENSUCHE))
        link_katzensuche.click()
