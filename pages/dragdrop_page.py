from selenium.webdriver import ActionChains  # Importiert ActionChains für Drag-and-Drop-Aktionen
from selenium.webdriver.common.by import By  # Importiert By für das Finden von Elementen mit Selektoren
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DragDropPage:
    # Definiert die Selektoren für verschiedene Logos
    LOGO_WHITE = (By.ID, "white-logo")
    LOGO_BLUE = (By.ID, "blue-logo")
    LOGO_RED = (By.ID, "red-logo")
    LOGO_GREEN = (By.ID, "green-logo")
    LOGO_CODING = (By.ID, "coding-logo")

    # Definiert die Selektoren für das Drop-Ziel und den Status-Text
    DROP_BOX = (By.ID, "droppable")
    TEXT_STATUS = (By.CSS_SELECTOR, "#droppable > p")

    def __init__(self, driver):
        """ Initialisiert die Klasse mit dem Selenium WebDriver. """
        self.driver = driver  # Speichert den WebDriver als Instanzvariable
        self.wait = WebDriverWait(self.driver, 10)  # Wartezeit von 10 Sekunden

    def status_abfragen(self):
        """ Gibt den aktuellen Textstatus des Drop-Bereichs zurück. """
        # Warten, bis der Status-Text sichtbar ist
        status_text = self.wait.until(EC.visibility_of_element_located(self.TEXT_STATUS))
        return status_text.text

    # Standard Drag-and-Drop für alle Logos
    def bewege_alle_logos_in_die_box(self):
        """ Bewegt alle Logos in die Drop-Box. """
        # Warten, bis die Logos und das Drop-Ziel sichtbar sind
        drglogo1 = self.wait.until(EC.visibility_of_element_located(self.LOGO_WHITE))
        drglogo2 = self.wait.until(EC.visibility_of_element_located(self.LOGO_BLUE))
        drglogo3 = self.wait.until(EC.visibility_of_element_located(self.LOGO_RED))
        drglogo4 = self.wait.until(EC.visibility_of_element_located(self.LOGO_GREEN))
        drglogo5 = self.wait.until(EC.visibility_of_element_located(self.LOGO_CODING))
        drpbox = self.wait.until(EC.visibility_of_element_located(self.DROP_BOX))

        # Erstellt eine ActionChains-Instanz und führt Drag-and-Drop für jedes Logo aus
        action = ActionChains(self.driver)
        action.drag_and_drop(drglogo1, drpbox).perform()
        action.drag_and_drop(drglogo2, drpbox).perform()
        action.drag_and_drop(drglogo3, drpbox).perform()
        action.drag_and_drop(drglogo4, drpbox).perform()
        action.drag_and_drop(drglogo5, drpbox).perform()

    # Individuelle Drag-and-Drop-Methoden für jedes Logo
    def bewege_logowhite_in_box(self):
        """ Bewegt das weiße Logo in die Drop-Box. """
        # Warten, bis das Logo und das Drop-Ziel sichtbar sind
        logo_white = self.wait.until(EC.visibility_of_element_located(self.LOGO_WHITE))
        drop_box = self.wait.until(EC.visibility_of_element_located(self.DROP_BOX))
        action = ActionChains(self.driver)
        action.drag_and_drop(logo_white, drop_box).perform()

    def bewege_logoblue_in_box(self):
        """ Bewegt das blaue Logo in die Drop-Box. """
        # Warten, bis das Logo und das Drop-Ziel sichtbar sind
        logo_blue = self.wait.until(EC.visibility_of_element_located(self.LOGO_BLUE))
        drop_box = self.wait.until(EC.visibility_of_element_located(self.DROP_BOX))
        action = ActionChains(self.driver)
        action.drag_and_drop(logo_blue, drop_box).perform()

    def bewege_logored_in_box(self):
        """ Bewegt das rote Logo in die Drop-Box. """
        # Warten, bis das Logo und das Drop-Ziel sichtbar sind
        logo_red = self.wait.until(EC.visibility_of_element_located(self.LOGO_RED))
        drop_box = self.wait.until(EC.visibility_of_element_located(self.DROP_BOX))
        action = ActionChains(self.driver)
        action.drag_and_drop(logo_red, drop_box).perform()

    def bewege_logogreen_in_box(self):
        """ Bewegt das grüne Logo in die Drop-Box. """
        # Warten, bis das Logo und das Drop-Ziel sichtbar sind
        logo_green = self.wait.until(EC.visibility_of_element_located(self.LOGO_GREEN))
        drop_box = self.wait.until(EC.visibility_of_element_located(self.DROP_BOX))
        action = ActionChains(self.driver)
        action.drag_and_drop(logo_green, drop_box).perform()

    def bewege_logocs_in_box(self):
        """ Bewegt das Coding-Logo in die Drop-Box. """
        # Warten, bis das Logo und das Drop-Ziel sichtbar sind
        logo_coding = self.wait.until(EC.visibility_of_element_located(self.LOGO_CODING))
        drop_box = self.wait.until(EC.visibility_of_element_located(self.DROP_BOX))
        action = ActionChains(self.driver)
        action.drag_and_drop(logo_coding, drop_box).perform()

    # Drag-and-Drop mit Offset (bewegt die Logos zu einer bestimmten Position)
    def bewege_logowhite_zum_punkt(self, x, y):
        """ Bewegt das weiße Logo um einen bestimmten Offset (x, y). """
        # Warten, bis das Logo sichtbar ist
        logo_white = self.wait.until(EC.visibility_of_element_located(self.LOGO_WHITE))
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(logo_white, x, y).perform()

    def bewege_logoblue_zum_punkt(self, x, y):
        """ Bewegt das blaue Logo um einen bestimmten Offset (x, y). """
        # Warten, bis das Logo sichtbar ist
        logo_blue = self.wait.until(EC.visibility_of_element_located(self.LOGO_BLUE))
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(logo_blue, x, y).perform()

    def bewege_logored_zum_punkt(self, x, y):
        """ Bewegt das rote Logo um einen bestimmten Offset (x, y). """
        # Warten, bis das Logo sichtbar ist
        logo_red = self.wait.until(EC.visibility_of_element_located(self.LOGO_RED))
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(logo_red, x, y).perform()

    def bewege_logogreen_zum_punkt(self, x, y):
        """ Bewegt das grüne Logo um einen bestimmten Offset (x, y). """
        # Warten, bis das Logo sichtbar ist
        logo_green = self.wait.until(EC.visibility_of_element_located(self.LOGO_GREEN))
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(logo_green, x, y).perform()

    def bewege_logocs_zum_punkt(self, x, y):
        """ Bewegt das Coding-Logo um einen bestimmten Offset (x, y). """
        # Warten, bis das Logo sichtbar ist
        logo_coding = self.wait.until(EC.visibility_of_element_located(self.LOGO_CODING))
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(logo_coding, x, y).perform()
