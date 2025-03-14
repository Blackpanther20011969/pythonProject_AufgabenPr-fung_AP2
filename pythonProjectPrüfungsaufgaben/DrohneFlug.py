class GeoPos:
    def __init__(self, latitude, longitude, altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude


class GeoCalculator:
    @staticmethod
    def getDistance(pos1, pos2):
        # Berechnet die Distanz zwischen zwei GeoPos-Objekten (vereinfachte Formel)
        return ((pos1.latitude - pos2.latitude) ** 2 +
                (pos1.longitude - pos2.longitude) ** 2 +
                (pos1.altitude - pos2.altitude) ** 2) ** 0.5


def calculateFlight (geoPositions):
    flightPositions = []
    # Start bei der ersten Position (Index 0)
    currentPos = geoPositions[0]
    flightPositions.append( currentPos)
    geoPositions.remove( currentPos)

    # Solange noch Positionen übrig sind
    while geoPositions:
        nearestPos = None
        nearestDistance = float('inf')

        # Finde die Position mit der kürzesten Entfernung zur aktuellen Position
        for pos in geoPositions:
            distance = GeoCalculator.getDistance(currentPos, pos)
            if distance < nearestDistance:
                nearestDistance = distance
                nearestPos = pos

        # Füge die nächste Position hinzu und setze sie als aktuelle Position
        flightPositions.append(nearestPos )
        geoPositions.remove(nearestPos)
        currentPos = nearestPos

    return flightPositions


# Beispielnutzung
geoPositions = [
    GeoPos(10.0, 20.0, 30.0),
    GeoPos(11.0, 21.0, 31.0),
    GeoPos(12.0, 22.0, 32.0),
    GeoPos(9.0, 19.0, 29.0)
]

flightPositions = calculateFlight ( geoPositions )

for i, pos in enumerate(flightPositions):
    print(f"Flight {i}: Latitude = {pos.latitude}, Longitude = {pos.longitude}, Altitude = {pos.altitude}")

"""
Aufgabe 2 Zusammenfassung:

Die Aufgabe dreht sich um eine Drohne, die mehrere Positionen (GeoPositions)
 in einer bestimmten Reihenfolge anfliegen soll. Die Drohne wählt immer die nächste Position, 
 die der aktuellen Position am nächsten liegt. Hierbei werden Entfernungen zwischen zwei 
 Positionen mithilfe der Methode getDistance der Klasse GeoCalculator berechnet.

Anforderung:

    Du hast ein Array geoPositions, das die Positionen speichert, die die Drohne anfliegen soll.
    Zu Beginn befindet sich die Drohne an der ersten Position (Index 0).
    Die Drohne fliegt immer zur nächstgelegenen Position und diese wird ins Array flightPositions geschrieben.
    Die Position, die die Drohne bereits angeflogen hat, wird aus dem Array geoPositions gelöscht.

Hinweise:

    Verwende Double.MAX_VALUE (in Python entspricht das float('inf')) um die größte mögliche Entfernung darzustellen.
  Wie du Pseudocode verstehen kannst:

Pseudocode ist eine einfache Darstellung eines Algorithmus, um ihn leicht zu verstehen,
 bevor man ihn in eine Programmiersprache übersetzt. Hier einige Tipps:

    Verwende klare Struktur:
        Pseudocode soll wie eine Mischung aus natürlicher Sprache und Programmierlogik sein. Z.B. kann man sagen: 
        
    Solange geoPositions nicht leer ist:
    Berechne die Distanz zwischen der aktuellen Position und jeder verbleibenden Position.
    Wähle die Position mit der kürzesten Distanz als nächste Position.
    Entferne diese Position aus geoPositions.
    
    
    BEGIN calculateFlight(geoPositions)
    INITIALIZE flightPositions as an empty list
    SET currentPos to geoPositions[0]  // Start bei der ersten Position
    ADD currentPos to flightPositions  // Speichere die Startposition
    REMOVE currentPos from geoPositions  // Entferne die Startposition

    WHILE geoPositions is not empty DO  // Solange noch Positionen vorhanden sind
        SET nearestPos to NULL
        SET nearestDistance to INFINITY  // Größte mögliche Entfernung

        FOR EACH pos IN geoPositions DO  // Für jede verbleibende Position
            CALCULATE distance between currentPos and pos using GeoCalculator.getDistance()
            IF distance < nearestDistance THEN  // Wenn die Entfernung kürzer ist
                SET nearestDistance to distance
                SET nearestPos to pos  // Speichere die nächste Position

        ADD nearestPos to flightPositions  // Speichere die nächste Position
        REMOVE nearestPos from geoPositions  // Entferne die angeflogene Position
        SET currentPos to nearestPos  // Setze die aktuelle Position auf die neu gewählte Position
    END WHILE

    RETURN flightPositions  // Gebe die komplette Route zurück
END

Erklärung des Pseudocodes:

    Initialisierung:
        flightPositions ist eine leere Liste, in der die angeflogenen Positionen gespeichert werden.
        currentPos wird auf die erste Position (geoPositions[0]) gesetzt.

    Schleife (WHILE):
        Solange es noch Positionen im geoPositions-Array gibt, wird die nächste Position gesucht.

    Suche nach der nächsten Position:
        nearestPos wird die nächste Position sein, die wir anfliegen.
        nearestDistance speichert die kürzeste bisher gefundene Entfernung.

    Vergleich:
        Für jede Position in geoPositions wird die Entfernung zur aktuellen Position berechnet.
         Wenn diese Entfernung kürzer ist als die bisher gefundene, wird diese Position als die nächste gespeichert.

    Speichern der nächsten Position:
        Die nächste Position wird in flightPositions gespeichert und aus geoPositions entfernt.
        Danach wird die Drohne auf diese Position gesetzt (currentPos wird aktualisiert).

    Rückgabe:
        Sobald alle Positionen abgeflogen sind, wird die vollständige Route (flightPositions) zurückgegeben.

Tipps zum Verstehen von Pseudocode:

    Anweisungen sind klar und direkt: Nutze einfache Aussagen wie "SET", "ADD", "REMOVE", "IF", "WHILE" etc., 
    um Aktionen
     zu beschreiben.
    Struktur: Achte auf Einrückungen und klar strukturierte Schleifen und Bedingungen.
    Lesbarkeit: Pseudocode soll möglichst allgemein und verständlich sein, ohne sich auf Syntaxregeln 
    einer Programmiersprache festzulegen.
    
     Kompakter Pseudocode
     BEGIN calculateFlight(geoPositions)
    INITIALIZE flightPositions as empty list
    SET currentPos to geoPositions[0]
    ADD currentPos to flightPositions
    REMOVE currentPos from geoPositions

    WHILE geoPositions is not empty DO
        SET nearestPos to position in geoPositions with minimum distance to currentPos
        ADD nearestPos to flightPositions
        REMOVE nearestPos from geoPositions
        SET currentPos to nearestPos
    END WHILE

    RETURN flightPositions
END

Vorschlag für eine leicht erweiterte Version (für zusätzliche Sicherheit)

Falls du sicher gehen willst, kannst du eine leicht erweiterte Version schreiben, die trotzdem kurz bleibt:

  BEGIN calculateFlight(geoPositions)
    INITIALIZE flightPositions as empty list
    SET currentPos to geoPositions[0]
    ADD currentPos to flightPositions
    REMOVE currentPos from geoPositions

    WHILE geoPositions is not empty DO
        SET nearestPos to NULL
        SET nearestDistance to INFINITY

        FOR EACH pos IN geoPositions DO
            CALCULATE distance between currentPos and pos
            IF distance < nearestDistance THEN
                SET nearestDistance to distance
                SET nearestPos to pos

        ADD nearestPos to flightPositions
        REMOVE nearestPos from geoPositions
        SET currentPos to nearestPos
    END WHILE

    RETURN flightPositions
END

    
"""