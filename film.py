# copyright by Adam Celej
import MaterialToBuy


class Film(MaterialToBuy.MaterialToBuy):
    def __init__(self, id_number, rezyser_imie, rezyser_nazwisko, tytul, rok_wydania, gatunek, aktor1_imie,
                 aktor1_nazwisko,
                 aktor2_imie, aktor2_nazwisko, aktor3_imie, aktor3_nazwisko, czas_trwania, jest_dostepne, ma_napisy,
                 dostepna_liczba, cena):
        self.id_number = id_number
        self.rezyser_imie = rezyser_imie
        self.rezyser_nazwisko = rezyser_nazwisko
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.aktor1_imie = aktor1_imie
        self.aktor1_nazwisko = aktor1_nazwisko
        self.aktor2_imie = aktor2_imie
        self.aktor2_nazwisko = aktor2_nazwisko
        self.aktor3_imie = aktor3_imie
        self.aktor3_nazwisko = aktor3_nazwisko
        self.czas_trwania = czas_trwania
        self.jest_dostepne = bool(jest_dostepne)
        self.ma_napisy = bool(ma_napisy)
        self.dostepna_liczba = dostepna_liczba
        self.cena = cena

    def pokaz_pozycje(self):
        print("id_number: " + str(self.id_number))
        print("Rezyser: " + self.rezyser_imie + " " + self.rezyser_nazwisko)
        print("Tytul: " + self.tytul)
        print("Rok wydania: " + str(self.rok_wydania))
        print("Gatunek: " + self.gatunek)
        print("Aktor 1: " + self.aktor1_imie + " " + self.aktor1_nazwisko)
        print("Aktor 2: " + self.aktor2_imie + " " + self.aktor2_nazwisko)
        print("Aktor 3: " + self.aktor3_imie + " " + self.aktor3_nazwisko)
        print("czas trwania: " + str(self.czas_trwania))
        if self.ma_napisy:
            print("Dostepne: Tak")
        else:
            print("Dostepne: Nie")
        if self.jest_dostepne:
            print("Dostepne: " + str(self.dostepna_liczba) + " sztuk")
        else:
            print("Dostepne: 0 sztuk")
        print("\n")
