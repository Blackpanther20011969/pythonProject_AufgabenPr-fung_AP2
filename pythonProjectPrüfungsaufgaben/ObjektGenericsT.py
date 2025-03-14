class Mitarbeiter:
    def __init__(self, name: str, gehalt: float):
        self._name = name
        self._gehalt = gehalt

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def gehalt(self):
        return self._gehalt

    @gehalt.setter
    def gehalt(self, value: float):
        self._gehalt = value


class Liste:
    def __init__(self):
        self._items = []

    def get(self, index: int):
        return self._items[index]

    def set(self, index: int, element):
        self._items[index] = element

    def size(self) -> int:
        return len(self._items)

    def add(self, element):
        self._items.append(element)


def sort(liste: Liste, f):
    n = liste.size()
    for i in range(n):
        for j in range(n - i - 1):
            if f(liste.get(j), liste.get(j + 1)) > 0:
                # Elemente tauschen
                temp = liste.get(j)
                liste.set(j, liste.get(j + 1))
                liste.set(j + 1, temp)


# Vergleichsfunktion
def vergleiche_mitarbeiter(m1: Mitarbeiter, m2: Mitarbeiter):
    return m1.gehalt - m2.gehalt


# Beispiel
mitarbeiter_liste = Liste()
mitarbeiter_liste.add(Mitarbeiter("Anna", 50000))
mitarbeiter_liste.add(Mitarbeiter("Ben", 60000))
mitarbeiter_liste.add(Mitarbeiter("Clara", 55000))

sort(mitarbeiter_liste, vergleiche_mitarbeiter)

for i in range(mitarbeiter_liste.size()):
    mitarbeiter = mitarbeiter_liste.get(i)
    print(f"{mitarbeiter.name}: {mitarbeiter.gehalt}")

"""
Erklärung des Codes:
Klasse Mitarbeiter: Enthält Getter- und Setter-Methoden für name und gehalt.

Klasse Liste: Implementiert get, set, size und add Methoden zur Verwaltung einer Liste von Objekten.

Sortierfunktion: Verwendet die Getter- und Setter-Methoden der Liste, um die Objekte zu sortieren.

Vergleichsfunktion: Definiert, wie zwei Mitarbeiterobjekte basierend auf ihrem Gehalt verglichen werden.

Beispielverwendung: Erstellt eine Liste von Mitarbeitern, sortiert sie und gibt die sortierten Ergebnisse aus.

START

# Klasse Mitarbeiter
KLASSE Mitarbeiter:
    EIGENSCHAFTEN: name, gehalt
    METHODEN:
        GETTER und SETTER für name und gehalt

# Klasse Liste
KLASSE Liste:
    EIGENSCHAFTEN: items
    METHODEN:
        GET(index: int): Element an index zurückgeben
        SET(index: int, element): Setze Element an index
        SIZE(): Anzahl der Elemente zurückgeben
        ADD(element): Füge Element zur Liste hinzu

# Sortierfunktion
FUNKTION sort(liste: Liste, f):
    n = liste.SIZE()
    FÜR i von 0 bis n - 1:
        FÜR j von 0 bis n - i - 1:
            WENN f(liste.GET(j), liste.GET(j + 1)) > 0:
                TAUSCHE liste.GET(j) und liste.GET(j + 1) MIT liste.SET

# Vergleichsfunktion
FUNKTION vergleiche_mitarbeiter(m1: Mitarbeiter, m2: Mitarbeiter):
    RÜCKGABE m1.gehalt - m2.gehalt

# Beispiel
ERSTELLE mitarbeiter_liste ALS Liste
ADD Mitarbeiter("Anna", 50000) ZU mitarbeiter_liste
ADD Mitarbeiter("Ben", 60000) ZU mitarbeiter_liste
ADD Mitarbeiter("Clara", 55000) ZU mitarbeiter_liste

SORT(mitarbeiter_liste, vergleiche_mitarbeiter)

FÜR i von 0 bis mitarbeiter_liste.SIZE() - 1:
    DRUCKE mitarbeiter_liste.GET(i).name und mitarbeiter_liste.GET(i).gehalt

ENDE

Erklärung des Pseudocodes:
Mitarbeiter-Klasse:

Definiert die Eigenschaften name und gehalt.

Enthält Getter- und Setter-Methoden für diese Eigenschaften.

Liste-Klasse:

Hat eine Eigenschaft items zur Speicherung von Elementen.

Methoden zum Abrufen (GET), Setzen (SET), Hinzufügen (ADD) und Größenbestimmen (SIZE) der Elemente.

Sortierfunktion:

Verwendet die GET und SET Methoden der Liste, um die Elemente zu sortieren.

Nutzt eine Vergleichsfunktion vergleiche_mitarbeiter zur Bestimmung der Sortierreihenfolge.

Beispiel:

Erstellt eine Instanz der Liste-Klasse und fügt Mitarbeiter hinzu.

Sortiert die Liste mit der sort-Funktion.

Gibt die sortierte Liste der Mitarbeiter aus.  

"""