# copyright by Adam Celej
import MaterialToBuy


class Film(MaterialToBuy.MaterialToBuy):
    def __init__(self, id_number, gatunek, autor_imie, autor_nazwisko, tytul, rok_wydania, czas_trwania, jest_dostepne,
                 ma_napisy,
                 dostepna_liczba, cena):
        super().__init__(id_number, gatunek, autor_imie, autor_nazwisko, tytul, rok_wydania, cena, jest_dostepne,
                         dostepna_liczba)

        self.__czas_trwania = czas_trwania
        self.__ma_napisy = bool(ma_napisy)

    # uzywam dekoratorow dzieki czemu metody grzecznie zwracaja mi argumenty :)
    @property
    def czas_trwania(self):
        return self.__czas_trwania

    @property
    def ma_napisy(self):
        return self.__ma_napisy

    def pokaz_pozycje(self):
        super(Film, self).pokaz_pozycje()
        print("czas trwania: " + str(self.czas_trwania))
        if self.ma_napisy:
            print("Dostepne napisy: Tak")
        else:
            print("Dostepne napisy: Nie")
        print("\n")

    def zmniejsz_dostepna_liczbe(self):
        super(Film, self).zmniejsz_dostepna_liczbe()

    def zwieksz_dostepna_liczbe(self):
        super(Film, self).zwieksz_dostepna_liczbe()

    def dostepne(self):
        super(Film, self).dostepne()

    def niedostepne(self):
        super(Film, self).niedostepne()
