from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class TestForm1Page:
    # Selektoren für verschiedene Elemente auf der Testformular-Seite
    TEXT_UBERSCHRIFT = (By.TAG_NAME, "h1")  # Überschrift der Seite
    INPUT_Betreff = (By.ID, "form-widgets-betreff")  # Eingabefeld für den Betreff
    INPUT_NAME = (By.ID, "form-widgets-name")  # Eingabefeld für den Namen
    SELECT_KURS = (By.NAME, "form.widgets.auswahl1:list")  # Dropdown zur Auswahl eines Kurses
    SELECT_FIRMABOX1 = (By.ID, "form-widgets-auswahl2-from")  # Erste Auswahlbox für Firmen
    BTN_FIRMAAUSWAHL = (By.NAME, "from2toButton")  # Button zum Übernehmen der Firmenauswahl
    SELECT_FIRMABOX2 = (By.ID, "form-widgets-auswahl2-to")  # Zweite Auswahlbox für Firmen
    BTN_FIRMANACHOBENSCHIEBEN = (By.NAME, "upButton")  # Button zum Verschieben von Firmen nach oben
    BTN_FORMULARSPEICHERN = (By.NAME, "form.buttons.speichern")  # Button zum Speichern des Formulars
    TEXT_STATUSMELDUNG = (By.ID, "message")  # Statusmeldung nach Absenden des Formulars
    TEXT_ERSTESELEMENTLISTE = (By.XPATH, "//ul[@id='companies']/li[1]")  # Erstes Element einer Liste

    def __init__(self, driver):
        """ Konstruktor speichert die WebDriver-Instanz. """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 Sekunden Timeout für das Warten auf Elemente

    def ueberschrift_auslesen(self):
        """ Liest die Hauptüberschrift der Seite aus und gibt sie zurück. """
        return self.wait.until(EC.visibility_of_element_located(self.TEXT_UBERSCHRIFT)).text

    def betreff_eingeben(self, betreff):
        """ Gibt einen Betreff in das entsprechende Eingabefeld ein. """
        self.wait.until(EC.visibility_of_element_located(self.INPUT_Betreff)).send_keys(betreff)

    def name_eingeben(self, name):
        """ Gibt einen Namen in das entsprechende Eingabefeld ein. """
        self.wait.until(EC.visibility_of_element_located(self.INPUT_NAME)).send_keys(name)

    def kurs_auswaehlen(self, kursname):
        """ Wählt einen Kurs aus dem Dropdown-Menü anhand des sichtbaren Textes aus. """
        kursAuswahl = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT_KURS)))
        kursAuswahl.select_by_visible_text(kursname)

    def firma_in_box1_auswaehlen(self, auswahl):
        """ Wählt eine oder mehrere Firmen in der ersten Firmen-Box aus. """
        firmaAuswahl = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT_FIRMABOX1)))
        for i in auswahl:
            firmaAuswahl.select_by_index(i)  # Auswahl nach Index

    def firmen_uebernehmen(self):
        """ Übernimmt die ausgewählten Firmen aus der ersten Box in die zweite Box. """
        self.wait.until(EC.element_to_be_clickable(self.BTN_FIRMAAUSWAHL)).click()

    def firma_in_box2_auswaehlen(self, auswahl):
        """ Wählt eine oder mehrere Firmen in der zweiten Firmen-Box aus. """
        firmaAuswahl = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT_FIRMABOX2)))
        for i in auswahl:
            firmaAuswahl.select_by_index(i)  # Auswahl nach Index

    def ausgewaehlte_firmen_nach_oben_verschieben(self):
        """ Verschiebt die ausgewählten Firmen in der zweiten Box nach oben. """
        self.wait.until(EC.element_to_be_clickable(self.BTN_FIRMANACHOBENSCHIEBEN)).click()

    def formular_speichern(self):
        """ Speichert das Formular durch Klicken auf den Speichern-Button. """
        self.wait.until(EC.element_to_be_clickable(self.BTN_FORMULARSPEICHERN)).click()

    def statusmeldung_auslesen(self):
        """ Liest die Statusmeldung nach dem Speichern des Formulars aus und gibt sie zurück. """
        return self.wait.until(EC.visibility_of_element_located(self.TEXT_STATUSMELDUNG)).text

    def erstes_lsitenelement_auslesen(self):
        """ Liest das erste Element einer Liste auf der Seite aus und gibt es zurück. """
        return self.wait.until(EC.visibility_of_element_located(self.TEXT_ERSTESELEMENTLISTE)).text
