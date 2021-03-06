from client import Client
# from book import Ksiazka
# from film import Film
from objects_lists import material_set, user_set


class Sklep:
    def __init__(self):
        self.przedmioty = material_set
        self.uzytkownicy = user_set
        self.listaZamowien = []
        self.logged_id = None
        self.wybor = {
            "1": self.rejestracja,
            "2": self.logowanie,
        }
        self.wyborLogged = {
            "1": self.pokaz_uzytkownikow,
            "2": self.pokaz_przedmioty,
            "3": self.pokaz_uzytkownikow_i_przedmioty,
            "4": self.zloz_zamowienie,
            "5": self.anuluj_zamowienie,
            "6": self.pokaz_zamowienie,
            "7": self.doladuj_konto,
        }

    def menu(self):
        print(""
              "1. Rejestracja\n"
              "2. Logowanie\n"
              "")

    def menu_logged(self):
        print("\n"
              "1. Pokaz uzytkownikow\n"
              "2. Pokaz przedmioty\n"
              "3. Pokaz uzytkownikow i przedmioty\n"
              "4. Zloz zamowienie\n"
              "5. Anuluj zamowienie\n"
              "6. Pokaz zamowienie\n"
              "7. Doladuj konto\n"
              "8. Wyjdz ze sklepu\n")

    def wlacz(self):
        if self.logged_id is None:
            while self.logged_id is None:
                self.menu()
                wybor = input("Wybierz operacje: ")
                dzialanie = self.wybor.get(wybor)
                if dzialanie:
                    dzialanie()
                else:
                    print("Nie ma takiej opcji. Wybierz ponownie.")
        elif self.logged_id != None:
            while True:
                self.menu_logged()
                wybor = input("Wybierz operacje: ")
                dzialanie = self.wyborLogged.get(wybor)
                if dzialanie:
                    dzialanie()
                else:
                    print("Nie ma takiej opcji. Wybierz ponownie.")

    def rejestracja(self):  # dodaje kolejny obiekt do bazy (listy) obiektow klasy user
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        plec = input("Podaj plec (m lub k): ")
        wiek = input("Podaj swoj wiek: ")
        haslo = input("Podaj haslo: ")
        numer = len(self.uzytkownicy)
        self.dodaj_uzytkownika(Client(numer, haslo, imie, nazwisko, plec, wiek, 0, 0))
        self.logged_id = numer
        print("\n")
        self.wlacz()

    def dodaj_uzytkownika(self, uzytkownik):
        self.uzytkownicy.append(uzytkownik)

    def logowanie(self):
        numer_klienta = int(input("Podaj swoje ID: "))
        for item in self.uzytkownicy:
            if item.numer == numer_klienta:
                haslo = input("Podaj haslo: ")
                if haslo == item.haslo:
                    print("Jestes zalogowany jako " + item.imie + " " + item.nazwisko + "\n\n")
                    self.logged_id = numer_klienta
                    self.wlacz()
                while haslo != item.haslo:
                    wybor = int(input(
                        "Haslo jest nieprawidlowe.\n Wybierz 1 aby wprowadzic haslo ponownie.\n Wybierz 0 aby przerwac akcje.\n"))
                    if wybor == 1:
                        haslo = input("Podaj haslo ponownie: ")
                    elif wybor == 0:
                        print("\n\n")
                        self.wlacz()

    def pokaz_uzytkownikow(self):
        for item in self.uzytkownicy:
            item.pokaz_clienta()

    def pokaz_przedmioty(self):
        for item in material_set:
            item.pokaz_pozycje()

    def pokaz_uzytkownikow_i_przedmioty(self):
        self.pokaz_uzytkownikow()
        self.pokaz_przedmioty()

    def zloz_zamowienie(self):
        wybrany_material = int(input("Wybierz obiekt ktory chcesz zamowic (podaj jego ID): "))
        for item in self.przedmioty:  # szukam materialu o wybranym id w liscie materialow
            if item.id_number == wybrany_material:
                if self.uzytkownicy[
                    self.logged_id].stan_konta >= item.cena:  # sprawdzam czy stan konta jest wiekszy od ceny materialu
                    if item.jest_dostepne:  # sprawdzam czy material jest dostepny i zmniejszam dostepna liczbe o jeden
                        item.dostepna_liczba -= 1
                        if item.dostepna_liczba == 0:
                            item.jest_dostepne = False
                        self.uzytkownicy[
                            self.logged_id].stan_konta -= item.cena  # zmniejszam stan konta o cene materialu
                        print("Zamowienie zlozone.\n")
                        return
                else:
                    print("Masz za malo srodkow na koncie. Doladuj konto lub wybierz tanszy produkt.\n")
                    print("\n")
                    return
        print("Niestety nie mamy produktu o takim ID. Wybierz inny produkt lub wroc do menu.\n")

    def anuluj_zamowienie(self):
        pass

    def pokaz_zamowienie(self):
        pass

    def doladuj_konto(self):
        pass
        kwota = int(input("Podaj kwote ktora chcesz doladowac konto (jesli wpiszesz 0 operacja zostanie przerwana: "))
        while kwota < 0:
            if kwota == 0:
                return
            kwota = int(input("Kwota nie moze byc ujemna. Podaj kwote jeszcze raz: "))
        user_set[self.logged_id].stan_konta += kwota
