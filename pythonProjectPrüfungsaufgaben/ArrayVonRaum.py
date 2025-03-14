class Raum :
    def __init__ (self, belegung) :
        self.belegung = belegung

    def getBelegung (self) :
        return self.belegung


def sortiereRaeume (raeume) :
    n = len ( raeume )
    # Bubble Sort Algorithmus
    for i in range ( n ) :
        for j in range ( 0, n - i - 1 ) :
            # Vergleiche die Belegungszahlen benachbarter Räume
            if raeume[j].getBelegung () > raeume[j + 1].getBelegung () :
                # Tausche die Räume, falls Belegungszahl größer ist
                raeume[j], raeume[j + 1] = raeume[j + 1], raeume[j]

    return raeume


# Beispielnutzung:
raum1 = Raum ( 5 )
raum2 = Raum ( 3 )
raum3 = Raum ( 10 )
raeume = [raum1, raum2, raum3]

sortierte_raeume = sortiereRaeume ( raeume )

# Ausgabe der Belegungszahlen sortierter Räume
for raum in sortierte_raeume :
    print ( raum.getBelegung () )


"""
Erklärungen:

    Raum-Klasse: Enthält die Methode getBelegung(), um die Belegungszahl des Raumes abzurufen.
    sortiereRaeume(): Nutzt den Bubble Sort-Algorithmus, um die Räume basierend auf ihren Belegungszahlen aufsteigend zu sortieren.
    Nach der Sortierung wird das Array der sortierten Räume zurückgegeben.
    
    Pseudocode
    
    Algorithmus: sortiereRaeume(raeume)

    Eingabe: raeume - Array von Raum-Objekten
    n = Länge von raeume

    Für i = 0 bis n-1
        Für j = 0 bis n-i-2
            Wenn getBelegung(raeume[j]) > getBelegung(raeume[j+1]) dann
                Tausche raeume[j] und raeume[j+1]
            Ende Wenn
        Ende Für
    Ende Für

    Rückgabe: sortiertes Array von Raum-Objekten
Ende Algorithmus

   Beschreibung:

    sortiereRaeume(raeume): Der Algorithmus nimmt ein Array von Raum-Objekten als Eingabe und sortiert es nach aufsteigender Belegungszahl.
    Es wird eine doppelte Schleife verwendet (ähnlich wie bei Bubble Sort).
    In jedem Durchlauf wird überprüft, ob das aktuelle Element eine größere Belegungszahl als das nächste hat. Falls ja, werden die beiden Elemente getauscht.

Erklärung der Schritte:

    Bestimme die Länge des Arrays raeume.
    Verwende eine doppelte Schleife, um die benachbarten Elemente zu vergleichen.
    Tausche zwei benachbarte Räume, wenn der erste eine größere Belegungszahl hat als der zweite.
    Wiederhole den Prozess, bis das Array sortiert ist.
    Am Ende wird das sortierte Array zurückgegeben. 
    
"""