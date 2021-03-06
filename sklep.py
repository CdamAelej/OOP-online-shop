from client import Client
from objects_lists import material_set, user_set
from sys import exit
from zamowienie import Zamowienie


class Sklep:
    def __init__(self):
        self.przedmioty = material_set
        self.uzytkownicy = user_set
        self.listaZamowien = []
        self.logged_id = None
        self.wybor = {
            "1": self.rejestracja,
            "2": self.logowanie,
            "3": self.wyjdz
        }
        self.wyborLogged = {
            "0": self.zmiana_hasla,
            "1": self.pokaz_uzytkownikow,
            "2": self.pokaz_przedmioty,
            "3": self.pokaz_uzytkownikow_i_przedmioty,
            "4": self.zloz_zamowienie,
            "5": self.anuluj_zamowienie,
            "6": self.pokaz_zamowienia,
            "7": self.doladuj_konto,
            "8": self.wyloguj,
            "9": self.wyjdz
        }

    def menu(self):
        print(""
              "1. Rejestracja\n"
              "2. Logowanie\n"
              "3. Wyjdz ze sklepu\n"
              "")

    def menu_logged(self):
        print("\n"
              "0. Zmiana hasla\n"
              "1. Pokaz uzytkownikow\n"
              "2. Pokaz przedmioty\n"
              "3. Pokaz uzytkownikow i przedmioty\n"
              "4. Zloz zamowienie\n"
              "5. Anuluj zamowienie\n"
              "6. Pokaz zamowienie\n"
              "7. Doladuj konto\n"
              "8. Wyloguj\n"
              "9. Wyjdz ze sklepu\n")

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
        elif self.logged_id is not None:
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
        # szukam podanego id w liscie uzytkownikow
        for item in self.uzytkownicy:
            # jesli znaleziono id to prosze o podanie hasla
            if item.numer == numer_klienta:
                haslo = input("Podaj haslo: ")
                # jesli haslo jest prawidlowe to loguje uzytkownika i wyswietlam menu dla zalogowanych
                if haslo == item.haslo:
                    print("Jestes zalogowany jako " + item.imie + " " + item.nazwisko + "\n\n")
                    # ustawiam klienta jako zalogowanego
                    self.logged_id = numer_klienta
                    self.wlacz()
                # dopoki haslo nie jest prawidlowe to pytam uzytkownika czy chce ponowic probe
                while haslo != item.haslo:
                    wybor = int(input(
                        "Haslo jest nieprawidlowe.\n Wybierz 1 aby wprowadzic haslo ponownie.\n Wybierz 0 aby przerwac akcje.\n"))
                    # ponawiamy probe zalogowania
                    if wybor == 1:
                        haslo = input("Podaj haslo ponownie: ")
                        if haslo == item.haslo:
                            self.logged_id = numer_klienta
                            self.wlacz()
                    # wyswietlam menu dla niezalogowanych
                    elif wybor == 0:
                        print("\n\n")
                        self.wlacz()

    def zmiana_hasla(self):
        for item in self.uzytkownicy:
            if item.numer == self.logged_id:
                item.zmien_haslo()

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
        # szukam materialu o wybranym id w liscie materialow
        for item in self.przedmioty:
            if item.id_number == wybrany_material:
                # sprawdzam czy stan konta jest wiekszy od ceny materialu
                if self.uzytkownicy[self.logged_id].stan_konta >= item.cena:
                    # sprawdzam czy material jest dostepny i zmniejszam dostepna liczbe o jeden
                    if item.jest_dostepne:
                        item.zmniejsz_dostepna_liczbe()
                        # jesli dostepna liczba jest rowna zero to przedmiot zmienia status na niedostepny
                        if item.dostepna_liczba == 0:
                            item.niedostepne()
                        # zmniejszam stan konta o cene materialu, zwiekszam liczbe zamowien klienta
                        self.uzytkownicy[self.logged_id].stan_konta -= item.cena
                        self.uzytkownicy[self.logged_id].zwieksz_liczbe_zamowien()
                        # do listy zamowien dodaje nowy obiekt klasy zamowienie skladajacy sie z id zamowienia,
                        # id zamawiajacego oraz id zamawianego przedmiotu
                        self.listaZamowien.append(Zamowienie(len(self.listaZamowien), self.logged_id, wybrany_material))
                        print("Zamowienie zlozone.\n")
                        return
                else:
                    print("Masz za malo srodkow na koncie. Doladuj konto lub wybierz tanszy produkt.\n")
                    print("\n")
                    return
        print("Niestety nie mamy produktu o takim ID. Wybierz inny produkt lub wroc do menu.\n")

    def anuluj_zamowienie(self):
        nr_zamowienia = int(input("Podaj id zamowienia ktore chcesz anulowac: "))
        for item in self.listaZamowien:
            # sprawdzam czy obiekt jest klasy zamowienie
            assert isinstance(item, Zamowienie)
            # jesli znaleziono obiekt to zmiejszam liczbe zamowien klienta oraz usuwam zamowienie
            if nr_zamowienia == item.id_zamowienia:
                self.uzytkownicy[self.logged_id].zmniejsz_liczbe_zamowien()
                self.listaZamowien.pop(item.id_zamowienia)

    def pokaz_zamowienia(self):
        for item in self.listaZamowien:
            # sprawdzamy i zapewniamy ??e item jest obiektem klasy Zamowienie
            assert isinstance(item, Zamowienie)
            print("Zamowienie nr " + str(item.id_zamowienia) + " zlozone przez uzytkownika o id " + str(
                item.id_zamawiajacego) + " na przedmiot o id " + str(item.id_przedmiotu) + "\n")

    def doladuj_konto(self):
        kwota = int(input("Podaj kwote ktora chcesz doladowac konto (jesli wpiszesz 0 operacja zostanie przerwana): "))
        while kwota < 0:
            if kwota == 0:
                return
            kwota = int(input("Kwota nie moze byc ujemna. Podaj kwote jeszcze raz: "))
        user_set[self.logged_id].stan_konta += kwota
        print("Doladowano konto. Stan konta wynosi " + str(user_set[self.logged_id].stan_konta))

    def wyloguj(self):
        self.logged_id = None
        self.wlacz()

    def wyjdz(self):
        print("Dziekuje za skorzystanie z mojego sklepu :) ")
        exit(0)
