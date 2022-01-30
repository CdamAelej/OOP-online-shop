# copyright by Adam Celej
from MaterialToBuy import MaterialToBuy


class Ksiazka(MaterialToBuy):
    def __init__(self, id_number, liczba_stron, gatunek,  autor_imie, autor_nazwisko, tytul, rok_wydania, cena, jest_dostepne, dostepna_liczba):
        super().__init__(id_number, gatunek, autor_imie, autor_nazwisko, tytul, rok_wydania, cena, jest_dostepne, dostepna_liczba)
        self.__liczba_stron = liczba_stron

    @property
    def liczba_stron(self):
        return self.__liczba_stron

    def pokaz_pozycje(self):
        super(Ksiazka, self).pokaz_pozycje()
        print("Liczba stron: " + str(self.liczba_stron))
        print("\n")

    def zmniejsz_dostepna_liczbe(self):
        super(Ksiazka, self).zmniejsz_dostepna_liczbe()

    def zwieksz_dostepna_liczbe(self):
        super(Ksiazka, self).zwieksz_dostepna_liczbe()

    def dostepne(self):
        super(Ksiazka, self).dostepne()

    def niedostepne(self):
        super(Ksiazka, self).niedostepne()