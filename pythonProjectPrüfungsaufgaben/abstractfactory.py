"""Implementation of the abstract factory pattern"""
import random

class PetShop:
    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory. We can set it at will."""
        self.pet_factory = animal_factory  # Setzt die Fabrik, die für die Erstellung von Tieren verwendet wird

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""
        pet = self.pet_factory.get_pet()  # Erstellt ein Tier mit der Fabrik
        print("This is a lovely", pet)  # Zeigt das erstellte Tier
        print("It says", pet.speak())  # Zeigt, was das Tier sagt
        print("It eats", self.pet_factory.get_food())  # Zeigt das Futter des Tieres

# Klassen, die von unserer Fabrik erzeugt werden

class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"

class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"

# Fabrikklassen

class DogFactory:
    def get_pet(self):
        return Dog()  # Erstellt und gibt einen Hund zurück

    def get_food(self):
        return "dog food"  # Gibt das Futter für Hunde zurück

class CatFactory:
    def get_pet(self):
        return Cat()  # Erstellt und gibt eine Katze zurück

    def get_food(self):
        return "cat food"  # Gibt das Futter für Katzen zurück

# Erzeugt die richtige Fabrik dynamisch

def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()  # Wählt zufällig eine Fabrik (Hund oder Katze)

# Zeigt Tiere mit verschiedenen Fabriken

shop = PetShop()  # Erstellt ein PetShop-Objekt
for i in range(3):
    shop.pet_factory = get_factory()  # Setzt die zufällig ausgewählte Fabrik
    shop.show_pet()  # Zeigt das erstellte Tier und sein Verhalten
    print("=" * 10)  # Trennt die Ausgaben der verschiedenen Durchläufe

"""

https://github.com/gennad/Design-Patterns-in-Python/blob/master/adapter.py

https://refactoring.guru/design-patterns/abstract-factory/python/example#lang-features


PetShop-Klasse:

__init__: Der Konstruktor nimmt eine animal_factory als Argument, die für die Erstellung von Tieren verwendet wird.
 Dies ermöglicht es, verschiedene Fabriken zu verwenden, um verschiedene Arten von Tieren zu erstellen.

show_pet: Diese Methode erstellt ein Tier mit der Fabrik, zeigt das Tier und gibt aus, was es sagt und was es isst.

Dog-Klasse:

Hat eine Methode speak, die "woof" zurückgibt, und eine __str__-Methode, die "Dog" zurückgibt. Diese Klasse repräsentiert einen Hund.

Cat-Klasse:

Hat eine Methode speak, die "meow" zurückgibt, und eine __str__-Methode, die "Cat" zurückgibt. Diese Klasse repräsentiert eine Katze.

DogFactory-Klasse:

get_pet: Erstellt und gibt ein Dog-Objekt zurück.

get_food: Gibt das Futter für Hunde zurück ("dog food").

CatFactory-Klasse:

get_pet: Erstellt und gibt ein Cat-Objekt zurück.

get_food: Gibt das Futter für Katzen zurück ("cat food").

get_factory-Funktion:

Diese Funktion wählt zufällig entweder DogFactory oder CatFactory und gibt eine Instanz dieser Fabrik zurück.

Hauptprogramm:

Erstellt ein PetShop-Objekt und setzt in drei Iterationen eine zufällig ausgewählte Fabrik (DogFactory oder CatFactory).
 Zeigt das Tier und dessen Verhalten an und trennt die Ausgaben mit einer Reihe von "=".
"""