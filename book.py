# copyright by Adam Celej
from MaterialToBuy import MaterialToBuy


class Ksiazka(MaterialToBuy):
    def __init__(self, id_number, liczba_stron, gatunek,  autor_imie, autor_nazwisko, tytul, rok_wydania, cena, jest_dostepne, dostepna_liczba):
        super().__init__(id_number, gatunek, autor_imie, autor_nazwisko, tytul, rok_wydania, cena, jest_dostepne, dostepna_liczba)
        self.liczba_stron = liczba_stron

    def pokaz_pozycje(self):
        super(Ksiazka, self).pokaz_pozycje()
        print("Liczba stron: " + str(self.liczba_stron))
        print("\n")
