# copyright by Adam Celej
from abc import ABC, abstractmethod  # ABC to Abstract Base Classes


class MaterialToBuy(ABC):
    def __init__(self, id_number, gatunek, autor_imie, autor_nazwisko, tytul, rok_wydania, cena, jest_dostepne,
                 dostepna_liczba):
        self.__id_number = id_number
        self.__gatunek = gatunek
        self.__autor_imie = autor_imie
        self.__autor_nazwisko = autor_nazwisko
        self.__tytul = tytul
        self.__rok_wydania = rok_wydania
        self.__cena = cena
        self.__jest_dostepne = bool(jest_dostepne)
        self.__dostepna_liczba = dostepna_liczba

    @property
    def id_number(self):
        return self.__id_number

    @property
    def gatunek(self):
        return self.__gatunek

    @property
    def autor_imie(self):
        return self.__autor_imie

    @property
    def autor_nazwisko(self):
        return self.__autor_nazwisko

    @property
    def tytul(self):
        return self.__tytul

    @property
    def rok_wydania(self):
        return self.__rok_wydania

    @property
    def cena(self):
        return self.__cena

    @property
    def jest_dostepne(self):
        return self.__jest_dostepne

    @property
    def dostepna_liczba(self):
        return self.__dostepna_liczba

    @abstractmethod
    def zmniejsz_dostepna_liczbe(self):
        self.__dostepna_liczba -= 1

    @abstractmethod
    def zwieksz_dostepna_liczbe(self):
        self.__dostepna_liczba += 1

    @abstractmethod
    def dostepne(self):
        self.__jest_dostepne = True

    @abstractmethod
    def niedostepne(self):
        self.__jest_dostepne = False

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
