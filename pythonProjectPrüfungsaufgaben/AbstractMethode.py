from abc import ABC, abstractmethod


# Abstrakte Klasse
class Hund(ABC):
    def __init__(self, alter, fellfarbe):
        self.alter = alter
        self.fellfarbe = fellfarbe

    @abstractmethod
    def sprechen(self):
        pass

    @abstractmethod
    def ausgabe(self):
        pass

    def get_fellfarbe(self):
        return self.fellfarbe


# Konkrete Klasse Schäferhund
class Schäferhund(Hund):
    def sprechen(self):
        return "Wuff Wuff"

    def ausgabe(self):
        print(f"Ich bin ein Schäferhund, {self.alter} Jahre alt und habe {self.fellfarbe}es Fell.")


# Konkrete Klasse Dackel
class Dackel(Hund):
    def sprechen(self):
        return "Wau Wau"

    def ausgabe(self):
        print(f"Ich bin ein Dackel, {self.alter} Jahre alt und habe {self.fellfarbe}es Fell.")


# Beispielverwendung
if __name__ == "__main__":
    schaeferhund = Schäferhund(3, "schwarzes")
    dackel = Dackel(5, "braunes")

    print(schaeferhund.sprechen())
    schaeferhund.ausgabe()
    print(dackel.sprechen())
    dackel.ausgabe()

"""
Erklärung des Codes
Abstrakte Klasse Hund:

Deklariert mit ABC aus dem Modul abc.

Hat zwei abstrakte Methoden: sprechen und ausgabe.

Der Konstruktor und die Methode get_fellfarbe sind nicht abstrakt und können direkt genutzt werden.

Konkrete Klassen Schäferhund und Dackel:

Erben von Hund und implementieren die abstrakten Methoden sprechen und ausgabe.

Diese Klassen müssen die abstrakten Methoden implementieren, sonst würden sie als abstrakte Klassen gelten und könnten nicht instanziiert werden.

Beispielverwendung:

Instanziiert Objekte von Schäferhund und Dackel.

Ruft die Methoden sprechen und ausgabe auf, um die Implementierungen zu demonstrieren.
"""