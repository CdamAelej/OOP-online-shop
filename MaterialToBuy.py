# copyright by Adam Celej
from abc import ABC, abstractmethod  # ABC to Abstract Base Classes


class MaterialToBuy(ABC):
    def __init__(self, id_number, gatunek, autor_imie, autor_nazwisko, tytul, rok_wydania, cena, jest_dostepne,
                 dostepna_liczba):
        self.id_number = id_number
        self.gatunek = gatunek
        self.autor_imie = autor_imie
        self.autor_nazwisko = autor_nazwisko
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.cena = cena
        self.jest_dostepne = bool(jest_dostepne)
        self.dostepna_liczba = dostepna_liczba

    @abstractmethod
    def pokaz_pozycje(self):
        print("ID produktu: " + str(self.id_number))
        print("Autor: " + self.autor_imie + " " + self.autor_nazwisko)
        print("Tytul: " + self.tytul)
        print("Gatunek: " + self.gatunek)
        print("Rok wydania: " + str(self.rok_wydania))
        print("Cena: " + str(self.cena))
        if self.jest_dostepne:
            print("Dostepne: " + str(self.dostepna_liczba) + " sztuk")
        else:
            print("Dostepne: Nie")
