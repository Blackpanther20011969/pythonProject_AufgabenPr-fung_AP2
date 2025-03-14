class Fahrzeug:
    def __init__(self, kennzeichen):
        self.kennzeichen = kennzeichen

    def fahren(self):
        print("Brumm")

class PKW(Fahrzeug):
    def __init__(self, kennzeichen):
        super().__init__(kennzeichen)
        self.motor = Motor()

    def fahren(self):
        print("Brumm Brumm")

class Motor:
    pass

# Hauptprogramm
if __name__ == "__main__":
    f = Fahrzeug("ABC-123")
    f.fahren()

    p = PKW("XYZ-234")
    p.fahren()

    f2 = PKW("XYZ-456")
    f2.fahren()
