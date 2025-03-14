"""
### Vorgehensweise:
1. Wir durchlaufen das `messung`-Array, das Messdaten enthält.
2. Für jeden Tag wird überprüft, ob der `istWert` eines Messdatums zu stark vom `sollWert` abweicht.
3. Falls ja, wird die Abweichung als Fehler gezählt.
4. Das Tagesprotokoll wird erstellt und ausgedruckt.

### Formel zur Berechnung der prozentualen Abweichung:
"""


def set_Arry(len):
    array = [0 for _ in range(len)]
    return array


def drucke_report(messung, anzahl, maxToleranz):
    tagesProtokoll = set_Arry(anzahl)
    vorherigesDatum = 0
    for Messung in messung:
        if vorherigesDatum == Messung.datum:
            zaehle_abweichung(Messung, tagesProtokoll, maxToleranz)
        else:
            drucke_tag(vorherigesDatum, tagesProtokoll)
            vorherigesDatum = Messung.datum
            tagesProtokoll = set_Arry(anzahl)
            zaehle_abweichung(Messung, tagesProtokoll, maxToleranz)
    drucke_report(vorherigesDatum, tagesProtokoll)


def zaehle_abweichung(Messung, tagesProtokoll, maxToleranz):
    abweichung = absolut((Messung.istWert / Messung.sollwert - 1) * 100)
    if abweichung > maxToleranz:
        tagesProtokoll[Messung.messArt] += 1


def drucke_tag(date, array):
    date.print_date()
    for messArt in array:
        print(messArt + " " + array[messArt])


def laenge(array):
    return len(array)


def absolut(wert):
    if wert >= 0:
        return wert
    else:
        return -1 * wert


class Date():
    jahr = "2024"
    monat = "Oktober"
    tag = "19"

    def print_date(self):
        print(self.jahr + " " + self.monat + " " + self.tag)


# Testaufrufe:
print(absolut(-5))

"""
Pseudocode für die Funktion druckeReport:

FUNKTION druckeReport(messung: Array von Messung, messArtAnzahl: integer, maxToleranz: double)
    tagesProtokoll = setArray(messArtAnzahl)  // Erzeuge ein Fehlerzählungsarray für den Tag
    aktuellesDatum = messung[0].datum         // Speichere das erste Datum
    i = 0                                     // Schleifenvariable
    
    SOLANGE i < laenge(messung)
        // Neues Tagesprotokoll, wenn wir ein neues Datum erreichen
        WENN messung[i].datum != aktuellesDatum DANN
            druckeTag(aktuellesDatum, tagesProtokoll)  // Drucke das Protokoll des aktuellen Tages
            tagesProtokoll = setArray(messArtAnzahl)  // Erzeuge ein neues Fehlerzählungsarray
            aktuellesDatum = messung[i].datum         // Setze das neue aktuelle Datum
        
        // Berechne die Abweichung des Istwerts vom Sollwert
        abweichung = absolut((messung[i].istWert - messung[i].sollWert) / messung[i].sollWert) * 100
        
        // Wenn die Abweichung größer ist als die maximale Toleranz, wird ein Fehler gezählt
        WENN abweichung > maxToleranz DANN
            tagesProtokoll[messung[i].messArt] = tagesProtokoll[messung[i].messArt] + 1
        
        i = i + 1  // Zum nächsten Messwert gehen
    
    // Drucke das Protokoll für den letzten Tag
    druckeTag(aktuellesDatum, tagesProtokoll)
ENDE FUNKTION
Erklärung der Schritte:

    Initialisierung:
        Wir beginnen mit dem ersten Datum und erzeugen ein tagesProtokoll-Array, 
        um die Fehler für jeden Tag und jede Messart zu zählen.
    Schleife über die Messungen:
        Für jede Messung wird geprüft, ob das Datum wechselt.
         Falls ja, wird das Tagesprotokoll für den vorherigen Tag ausgedruckt,
          und ein neues Tagesprotokoll wird erstellt.
    Fehlerprüfung:
        Die prozentuale Abweichung zwischen istWert und sollWert wird berechnet.
         Falls die Abweichung die maximale Toleranz überschreitet, 
         wird ein Fehler in der entsprechenden Position im tagesProtokoll gezählt.
    Druck des Tagesprotokolls:
        Am Ende wird das letzte Protokoll ausgedruckt.

Mit diesem Pseudocode kannst du die Aufgabe schrittweise in Python umsetzen.
 Durch das Durchlaufen der Messungen und die Berechnung der Abweichungen pro Messung wird der
  Fehlerreport effizient erstellt.
  
"""
