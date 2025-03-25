from selenium.webdriver.common.by import By  # Ermöglicht das Auffinden von Elementen über verschiedene Selektoren
from selenium.webdriver.support.ui import WebDriverWait  # Ermöglicht explizite Wartezeiten für Elemente
from selenium.webdriver.support import expected_conditions as EC  # Enthält Bedingungen, um Elemente zu überprüfen


class LoginPage:
    """
    Repräsentiert die Login-Seite der Webanwendung und bietet Methoden zur Interaktion mit den Login-Elementen.
    """

    def __init__(self, driver):
        """
        Initialisiert die LoginPage-Klasse mit einem WebDriver-Objekt und definiert die benötigten Web-Elemente.

        :param driver: WebDriver-Instanz zur Steuerung des Browsers.
        """
        self.driver = driver
        self.username_field = (By.ID, "__ac_name")  # ID-Selektor für das Benutzername-Eingabefeld
        self.password_field = (By.ID, "__ac_password")  # ID-Selektor für das Passwort-Eingabefeld
        self.login_button = (By.XPATH, "//input[@name='buttons.login']")  # XPATH für den Login-Button
        self.error_message = (By.XPATH, "//div[@class='portalMessage error']")  # XPATH für Fehlermeldungen
        self.success_message = (By.XPATH, "//div[@class='portalMessage info']")  # XPATH für Erfolgsnachrichten

    def enter_username(self, username):
        """
        Gibt den Benutzernamen in das entsprechende Feld ein.

        :param username: Der einzugebende Benutzername.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)

    def enter_password(self, password):
        """
        Gibt das Passwort in das entsprechende Feld ein.

        :param password: Das einzugebende Passwort.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field)
        ).send_keys(password)

    def click_login(self):
        """
        Klickt auf den Login-Button.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def get_error_message(self):
        """
        Ruft die Fehlermeldung nach einem fehlgeschlagenen Login-Versuch ab.

        :return: Der Text der Fehlermeldung.
        """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        ).text

    def get_success_message(self):
        """
        Ruft die Erfolgsnachricht nach einem erfolgreichen Login-Vorgang ab.

        :return: Der Text der Erfolgsnachricht.
        """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_message)
        ).text
