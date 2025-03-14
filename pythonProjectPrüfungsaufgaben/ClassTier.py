class Tier:
    def __init__(self, alter):
        self.alter = alter

    def ausgabe(self):
        print(f"Ich bin ein Tier, und ich bin {self.alter} Jahre alt.")


class Hund(Tier):
    def __init__(self, alter, fellfarbe):
        super().__init__(alter)
        self.fellfarbe = fellfarbe
        print("Aufruf des Konstruktors in Hund.")

    def get_fellfarbe(self):
        return self.fellfarbe

    def ausgabe(self):
        super().ausgabe()
        print("Ich bin ein Hund. Wau Wau")


# Beispielnutzung
if __name__ == "__main__":
    hund = Hund(5, "braun")
    hund.ausgabe()
