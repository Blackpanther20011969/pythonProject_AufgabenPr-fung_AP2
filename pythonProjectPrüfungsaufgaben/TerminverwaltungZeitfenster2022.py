class Zeitfenster:
    def __init__(self, max_buchungen, buchbar=True):
        self.max_buchungen = max_buchungen  # Maximal mögliche Buchungen für das Zeitfenster
        self.verfuegbare_buchungen = max_buchungen if buchbar else 0
        self.zustand = "grün" if buchbar else "gesperrt"
        self.aktualisiere_zustand()

    def aktualisiere_zustand(self):
        """ Aktualisiert den Zustand des Zeitfensters basierend auf den verfügbaren Buchungen """
        if self.verfuegbare_buchungen >= 10:
            self.zustand = "grün"
        elif 1 <= self.verfuegbare_buchungen < 10:
            self.zustand = "rot"
        else:
            self.zustand = "gesperrt"

    def buchen(self):
        """ Führt eine Buchung durch, sofern das Zeitfenster nicht gesperrt ist """
        if self.zustand != "gesperrt" and self.verfuegbare_buchungen > 0:
            self.verfuegbare_buchungen -= 1
            self.aktualisiere_zustand()
            print(f"Buchung erfolgreich. Verfügbare Buchungen: {self.verfuegbare_buchungen}")
        else:
            print("Buchung nicht möglich. Zeitfenster gesperrt oder keine Buchungen verfügbar.")

    def stornieren(self):
        """ Führt eine Stornierung durch, sofern das Maximum noch nicht erreicht ist """
        if self.verfuegbare_buchungen < self.max_buchungen:
            self.verfuegbare_buchungen += 1
            self.aktualisiere_zustand()
            print(f"Stornierung erfolgreich. Verfügbare Buchungen: {self.verfuegbare_buchungen}")
        else:
            print("Stornierung nicht möglich. Alle Buchungen bereits verfügbar.")

# Beispiel zur Verwendung
zeitfenster = Zeitfenster(max_buchungen=20)
zeitfenster.buchen()  # Buchung durchführen
zeitfenster.stornieren()  # Stornierung durchführen

"""
Überblick:

    Ein Zeitfenster kann die Zustände grün, rot oder gesperrt annehmen.
        grün: Buchbar, mindestens 10 Buchungen verfügbar.
        rot: Nur 1 bis 9 Buchungen verfügbar.
        gesperrt: Keine Buchungen verfügbar oder initial für unbuchbare Zeiten.
        Wir beginnen mit einer Klasse Zeitfenster, die die Anzahl der Buchungen und den Zustand 
        des Zeitfensters verwaltet. 
        Für die Statusänderungen erstellen wir Methoden zur Buchung und Stornierung.
     In diesem Code:

    Konstruktor (__init__): Hier wird das Zeitfenster initialisiert. buchbar legt fest, ob das Fenster von Anfang an buchbar ist.
    aktualisiere_zustand: Diese Methode überprüft und setzt den Zustand des Zeitfensters basierend auf den verbleibenden Buchungen.
    buchen: Verringert die verfügbaren Buchungen um 1 und aktualisiert den Zustand.
    stornieren: Erhöht die verfügbaren Buchungen um 1 und aktualisiert ebenfalls den Zustand.   
    
    KLASSE Zeitfenster
    INITIALISIERE max_buchungen, buchbar
    SETZE verfügbare_buchungen = max_buchungen WENN buchbar SONST 0
    SETZE zustand WENN buchbar "grün" SONST "gesperrt"
    Rufe aktualisiere_zustand() AUF

    FUNKTION aktualisiere_zustand()
        WENN verfügbare_buchungen >= 10 DANN
            zustand = "grün"
        SONST WENN 1 <= verfügbare_buchungen < 10 DANN
            zustand = "rot"
        SONST
            zustand = "gesperrt"
        ENDE WENN

    FUNKTION buchen()
        WENN zustand NICHT "gesperrt" UND verfügbare_buchungen > 0 DANN
            verfügbare_buchungen = verfügbare_buchungen - 1
            Rufe aktualisiere_zustand() AUF
            AUSGABE "Buchung erfolgreich"
        SONST
            AUSGABE "Buchung nicht möglich"
        ENDE WENN

    FUNKTION stornieren()
        WENN verfügbare_buchungen < max_buchungen DANN
            verfügbare_buchungen = verfügbare_buchungen + 1
            Rufe aktualisiere_zustand() AUF
            AUSGABE "Stornierung erfolgreich"
        SONST
            AUSGABE "Stornierung nicht möglich"
        ENDE WENN
ENDE KLASSE
Dieser Pseudocode gibt dir ein Grundgerüst für die Programmierung:

    aktualisiere_zustand prüft die Bedingungen für die Zustandsübergänge.
    buchen und stornieren prüfen die Verfügbarkeit und passen die Buchungen an.
        
"""