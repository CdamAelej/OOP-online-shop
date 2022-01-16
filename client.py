# copyright by Adam Celej
class Client:
    def __init__(self, numer, haslo, imie, nazwisko, plec, wiek, ilosc_zamowien, stan_konta):
        self.numer = numer
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.wiek = wiek
        self.ilosc_zamowien = ilosc_zamowien
        self.haslo = haslo
        self.stan_konta = stan_konta

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
