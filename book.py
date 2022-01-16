import MaterialToBuy


class Ksiazka(MaterialToBuy.MaterialToBuy):
    def __init__(self, id_number, autor_imie, autor_nazwisko, tytul, gatunek, rok_wydania, liczba_stron, jest_dostepne,
                 dostepna_liczba, cena):
        self.id_number = id_number
        self.autor_imie = autor_imie
        self.autor_nazwisko = autor_nazwisko
        self.tytul = tytul
        self.gatunek = gatunek
        self.rok_wydania = rok_wydania
        self.liczba_stron = liczba_stron
        self.jest_dostepne = bool(jest_dostepne)
        self.dostepna_liczba = dostepna_liczba
        self.cena = cena

    def pokaz_pozycje(self):
        print("id_number: " + str(self.id_number))
        print("Autor: " + self.autor_imie + " " + self.autor_nazwisko)
        print("Tytul: " + self.tytul)
        print("Gatunek: " + self.gatunek)
        print("Rok wydania: " + str(self.rok_wydania))
        print("Liczba stron: " + str(self.liczba_stron))
        if self.jest_dostepne:
            print("Dostepne: " + str(self.dostepna_liczba) + " sztuk")
        else:
            print("Dostepne: 0 sztuk")
        print("\n")
