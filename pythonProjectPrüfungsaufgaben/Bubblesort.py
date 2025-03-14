# Bubblesort Vorgehensweise 1
def bubble_sort(array):
    n = len(array)
    # Äußere Schleife für jede Iteration
    for i in range(n):
        swapped = False
        print(f"\n--- Iteration {i + 1} ---")  # Ausgabe der aktuellen Iteration

        # Innere Schleife für das Vergleichen und Tauschen
        for j in range(0, n - i - 1):
            print(f"Vergleiche {array[j]} und {array[j + 1]}")  # Vergleichsausgabe
            if array[j] > array[j + 1]:  # Wenn das linke Element größer ist, dann tauschen
                # Tauschen
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                print(f"Tauschen: {array}")  # Ausgabe des Arrays nach dem Tausch

        # Ausgabe des Arrays nach einer kompletten Durchlauf (Iteration)
        print(f"Array nach Iteration {i + 1}: {array}")

        # Wenn keine Vertauschung stattgefunden hat, ist das Array bereits sortiert
        if not swapped:
            break

    return array


# Hauptprogrammteil: Hier rufen wir die Funktion auf
array = [5, 3, 8, 4, 2]  # Das unsortierte Array
print("Ursprüngliches Array:", array)
sorted_array = bubble_sort(array)
print("\nSortiertes Array:", sorted_array)

print()

# Bubblesort Vorgehensweise 2

def bubbleSort(array):
    for j in range(0, len(array)-1):
        for i in range(0, len(array)-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

array_numbers = [54,26,93,17,77,31,44,55,20]
bubbleSort(array_numbers)

print(array_numbers)

print()

# Bubblesort Vorgehensweise 3

def bubble_sort(array):
    length = len(array)

    # Äußere Schleife: Durchlaufe alle Elemente
    for i in range(length):
        # Innere Schleife: Vergleiche je zwei benachbarte Elemente
        for j in range(1, length - i):
            # Prüfe, ob Elemente falsch sortiert sind (Ziel: Aufsteigend)
            if array[j - 1] > array[j]:
                # Tauschen der Elemente
                temp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = temp


def print_array(array):
    for i in range(len(array)):
        print(f"{i}:{array[i]} ", end="")
    print()  # Zum Abschluss der Zeile


# Hauptprogramm
if __name__ == "__main__":
    array = [77, 42, 35, 12, 101, 5]

    print("Array vor der Sortierung:")
    print_array(array)

    bubble_sort(array)  # Sortiere mit Bubble Sort

    print("Array nach der Sortierung:")
    print_array(array)

print()


"""
Ursprüngliches Array: [5, 3, 8, 4, 2]

--- Iteration 1 ---
Vergleiche 5 und 3
Tauschen: [3, 5, 8, 4, 2]
Vergleiche 5 und 8
Vergleiche 8 und 4
Tauschen: [3, 5, 4, 8, 2]
Vergleiche 8 und 2
Tauschen: [3, 5, 4, 2, 8]
Array nach Iteration 1: [3, 5, 4, 2, 8]

--- Iteration 2 ---
Vergleiche 3 und 5
Vergleiche 5 und 4
Tauschen: [3, 4, 5, 2, 8]
Vergleiche 5 und 2
Tauschen: [3, 4, 2, 5, 8]
Array nach Iteration 2: [3, 4, 2, 5, 8]

--- Iteration 3 ---
Vergleiche 3 und 4
Vergleiche 4 und 2
Tauschen: [3, 2, 4, 5, 8]
Array nach Iteration 3: [3, 2, 4, 5, 8]

--- Iteration 4 ---
Vergleiche 3 und 2
Tauschen: [2, 3, 4, 5, 8]
Array nach Iteration 4: [2, 3, 4, 5, 8]

Sortiertes Array: [2, 3, 4, 5, 8]

Übungsaufgabe für Bubble Sort

Aufgabe: Sortiere das folgende Array mit dem Bubble-Sort-Algorithmus:

Unsortiertes Array: [5, 3, 8, 4, 2]
Zwischenschritte von unsortiert zu sortiert

Wir gehen nun Schritt für Schritt durch die Sortierung.

Initiales Array: [5, 3, 8, 4, 2]

    Erste Iteration:
        Vergleiche 5 und 3: Tauschen -> [3, 5, 8, 4, 2]
        Vergleiche 5 und 8: Kein Tausch -> [3, 5, 8, 4, 2]
        Vergleiche 8 und 4: Tauschen -> [3, 5, 4, 8, 2]
        Vergleiche 8 und 2: Tauschen -> [3, 5, 4, 2, 8]

    Array nach der 1. Iteration: [3, 5, 4, 2, 8] (8 ist nun am endgültigen Platz)

    Zweite Iteration:
        Vergleiche 3 und 5: Kein Tausch -> [3, 5, 4, 2, 8]
        Vergleiche 5 und 4: Tauschen -> [3, 4, 5, 2, 8]
        Vergleiche 5 und 2: Tauschen -> [3, 4, 2, 5, 8]

    Array nach der 2. Iteration: [3, 4, 2, 5, 8] (5 und 8 sind nun am endgültigen Platz)

    Dritte Iteration:
        Vergleiche 3 und 4: Kein Tausch -> [3, 4, 2, 5, 8]
        Vergleiche 4 und 2: Tauschen -> [3, 2, 4, 5, 8]

    Array nach der 3. Iteration: [3, 2, 4, 5, 8] (4, 5 und 8 sind am endgültigen Platz)

    Vierte Iteration:
        Vergleiche 3 und 2: Tauschen -> [2, 3, 4, 5, 8]

    Array nach der 4. Iteration: [2, 3, 4, 5, 8]

Da keine weiteren Vertauschungen notwendig sind, ist das Array nun sortiert.

Übung für dich:

Versuche, den Bubble-Sort-Algorithmus auf das folgende Array anzuwenden und die Zwischenschritte wie oben durchzugehen:

Übungs-Array: [9, 7, 3, 1, 5]

BEGIN BubbleSort(array)
    SET n to the length of array

    FOR i FROM 0 TO n - 1 DO
        SET swapped to False
        FOR j FROM 0 TO n - i - 2 DO
            IF array[j] > array[j + 1] THEN
                SWAP array[j] and array[j + 1]
                SET swapped to True
        END FOR

        IF swapped is False THEN
            BREAK
    END FOR
END

Bubble Sort Algorithmus Erklärung

Bubble Sort ist ein einfacher Sortieralgorithmus, der Elemente eines Arrays wiederholt paarweise 
vergleicht und vertauscht, wenn sie in der falschen Reihenfolge stehen. Dies führt dazu,
 dass das größte Element "nach oben wandert", also ans Ende der Liste „bubblet“.
  Der Prozess wird wiederholt, bis die Liste vollständig sortiert ist.

Grundlegender Ablauf von Bubble Sort:

    Vergleiche benachbarte Elemente in der Liste.
    Wenn das linke Element größer ist als das rechte, vertausche die beiden.
    Wiederhole den Vorgang für alle Elemente in der Liste.
    Nach jedem Durchgang (einer sogenannten "Iteration") wird das größte Element an seinen endgültigen Platz verschoben.
    Reduziere die zu durchlaufende Liste nach jeder Iteration um eins, da das letzte Element schon am richtigen Platz ist.
    Wiederhole die Schritte, bis keine Vertauschungen mehr nötig sind.
"""



