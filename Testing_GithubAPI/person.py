
class Person:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}. Mam {self.wiek} lat.")
        print("Zgadza sie :)")
    def urodziny(self):
        wiek_przed = self.wiek
        self.wiek += 1
        return wiek_przed
