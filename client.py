# copyright by Adam Celej
class Client:
    def __init__(self, numer, haslo, imie, nazwisko, plec, wiek, ilosc_zamowien, stan_konta):
        self.__numer = numer
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__plec = plec
        self.__wiek = wiek
        self.__ilosc_zamowien = ilosc_zamowien
        self.__haslo = haslo
        self.stan_konta = stan_konta

    # uzywam dekoratorow dzieki czemu metody grzecznie zwracaja mi argumenty :)
    @property
    def numer(self):
        return self.__numer

    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @property
    def plec(self):
        return self.__plec

    @property
    def wiek(self):
        return self.__wiek

    @property
    def ilosc_zamowien(self):
        return self.__ilosc_zamowien

    @property
    def haslo(self):
        return self.__haslo

    def pokaz_clienta(self):
        print("id_number: " + str(self.numer))
        print("Haslo: " + '*' * len(self.haslo))
        print("Imie: " + self.imie)
        print("Nazwisko: " + self.nazwisko)
        print("Plec: " + self.plec)
        print("Wiek: " + str(self.wiek))
        print("Ilosc zamowien: " + str(self.ilosc_zamowien))
        print("Stan konta: " + str(self.stan_konta))
        print("\n")

    def zmien_haslo(self):
        old_haslo = input("Podaj stare haslo: ")
        while old_haslo != self.__haslo:
            old_haslo = input("Nieprawidlowe haslo. Podaj stare haslo jeszcze raz: ")
            if old_haslo == self.__haslo:
                new_haslo = input("Podaj nowe haslo: ")
                self.__haslo = new_haslo
                break

    def zwieksz_liczbe_zamowien(self):
        self.__ilosc_zamowien += 1

    def zmniejsz_liczbe_zamowien(self):
        self.__ilosc_zamowien -= 1
