feld = [2,5,9,8,1,5,2,4]

#Ausgabe des unsortierten Felds
for a in feld:
    print(a, end=' ')
print('\n')

#sortieren mit Bubble-Sort
anzahl = len(feld)
for j in range(0,anzahl):
    for i in range(0,anzahl - j - 1):
        if feld[i] > feld[i+1]:
            help = feld[i]
            feld[i] = feld[i+1]
            feld[i+1] = help

for a in feld:
    print(a, end=' ')

feld = [4, 2, 7, 1, 3]

# Ausgabe des unsortierten Feldes
print("Unsortiertes Feld:", feld)

# Bubble Sort
anzahl = len(feld)
for j in range(anzahl):
    for i in range(anzahl - j - 1):
        if feld[i] > feld[i + 1]:
            feld[i], feld[i + 1] = feld[i + 1], feld[i]

# Ausgabe des sortierten Feldes
print("Sortiertes Feld:", feld)


feld = ["Apfel", "Orange", "Banane", "Kirsche"]

# Bubble Sort
anzahl = len(feld)
for j in range(anzahl):
    for i in range(anzahl - j - 1):
        if feld[i] > feld[i+1]:
            feld[i], feld[i+1] = feld[i+1], feld[i]

# Ausgabe des sortierten Feldes
print("Sortiertes Feld:", feld)


feld = [4, 2, 7, 1, 3]

# Bubble Sort in absteigender Reihenfolge
anzahl = len(feld)
for j in range(anzahl):
    for i in range(anzahl - j - 1):
        if feld[i] < feld[i+1]:
            feld[i], feld[i+1] = feld[i+1], feld[i]

# Ausgabe des sortierten Feldes
print("Sortiertes Feld (absteigend):", feld)


feld = [2, 5, 2, 8, 2, 4, 5]

# Bubble Sort
anzahl = len(feld)
for j in range(anzahl):
    for i in range(anzahl - j - 1):
        if feld[i] > feld[i+1]:
            feld[i], feld[i+1] = feld[i+1], feld[i]

# Ausgabe des sortierten Feldes
print("Sortiertes Feld:", feld)


feld = [4, 2, 7, 1, 3]

# Bubble Sort mit Debug-Ausgaben
anzahl = len(feld)
for j in range(anzahl):
    for i in range(anzahl - j - 1):
        if feld[i] > feld[i+1]:
            feld[i], feld[i+1] = feld[i+1], feld[i]
    print(f"Zwischenstand nach Durchgang {j+1}: {feld}")

# Ausgabe des sortierten Feldes
print("Sortiertes Feld:", feld)


# 1. Eingabe der Daten
schuelerListe = [
    {"name": "Anna", "note": 3},
    {"name": "Ben", "note": 1},
    {"name": "Clara", "note": 2}
]

# 2. Sortieren der Daten mit Bubble Sort
anzahl = len(schuelerListe)
for j in range(anzahl):
    for i in range(anzahl - j - 1):
        if schuelerListe[i]["note"] > schuelerListe[i+1]["note"]:
            schuelerListe[i], schuelerListe[i+1] = schuelerListe[i+1], schuelerListe[i]

# 3. Berichterstellung
bericht = []
for schueler in schuelerListe:
    bericht.append(f'{schueler["name"]}: {schueler["note"]}')

# 4. Ausgabe des Berichts
print("Sortierte Schülerliste:")
for eintrag in bericht:
    print(eintrag)



