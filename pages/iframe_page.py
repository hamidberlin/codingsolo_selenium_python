from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IFramePage:
    # Selektoren für die benötigten Elemente innerhalb des iFrames
    INPUT_NAME = (By.ID, "name")  # Eingabefeld für den Namen
    BTN_ALERT = (By.ID, "alertbtn")  # Button zum Auslösen eines Alerts

    def __init__(self, driver):
        """ Konstruktor der Klasse, um die WebDriver-Instanz zu speichern. """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Wartezeit von 10 Sekunden

    def aktiviere_iframe(self):
        """ Wechselt in den iFrame mit dem Namen 'iframe'. """
        iframe = self.wait.until(EC.frame_to_be_available_and_switch_to_it("iframe"))
        return iframe

    def namen_eingeben(self, namen):
        """ Gibt den übergebenen Namen in das Eingabefeld innerhalb des iFrames ein. """
        # Warten, bis das Eingabefeld sichtbar ist, bevor es verwendet wird
        input_name = self.wait.until(EC.visibility_of_element_located(self.INPUT_NAME))
        input_name.send_keys(namen)

    def alert_anklicken(self):
        """ Klickt auf den Button, um das Alert-Fenster auszulösen. """
        # Warten, bis der Button klickbar ist
        alert_button = self.wait.until(EC.element_to_be_clickable(self.BTN_ALERT))
        alert_button.click()

    def alert_box_auslesen(self):
        """ Liest den Text der Alert-Box aus und gibt ihn zurück. """
        # Warten, bis das Alert-Fenster sichtbar ist
        alert = self.wait.until(EC.alert_is_present())
        return alert.text

    def alert_box_wegklicken(self):
        """ Akzeptiert und schließt die Alert-Box. """
        # Warten, bis das Alert-Fenster sichtbar ist und akzeptieren
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
