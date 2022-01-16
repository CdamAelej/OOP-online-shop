import objects_lists
import os
import client

logged_id = -1 # zmienna potrzebna do operacji takich jak zloz zamowienie po zalogowaniu

def cls(): #niby czysci ekran ale jakos w to nie wierze XD
    os.system('cls' if os.name == 'nt' else 'clear')


def rejestracja(): #dodaje kolejny obiekt do bazy (listy) obiektow klasy user
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    plec = input("Podaj plec (m lub k): ")
    wiek = input("Podaj swoj wiek: ")
    haslo = input("Podaj haslo: ")
    numer = len(objects_lists.user_set)
    objects_lists.user_set.append(client.Client(numer, haslo, imie, nazwisko, plec, wiek, 0, 0))
    print("\n")


def logowanie():
    numer_klienta = int(input("Podaj swoje ID: "))
    for item in objects_lists.user_set:
        if item.numer == numer_klienta:
            haslo = input("Podaj haslo: ")
            if haslo == item.haslo:
                cls()
                print("Jestes zalogowany jako " + item.imie + " " + item.nazwisko + "\n\n")
                logged_id = numer_klienta
                menu(1)
            while haslo != item.haslo:
                wybor = int(input(
                    "Haslo jest nieprawidlowe.\n Wybierz 1 aby wprowadzic haslo ponownie.\n Wybierz 0 aby przerwac akcje.\n"))
                if wybor == 1:
                    haslo = input("Podaj haslo ponownie: ")
                elif wybor == 0:
                    print("\n\n")
                    menu(0)


def pokaz_klientow():
    for item in objects_lists.user_set:
        item.pokaz_clienta()


def pokaz_materialy():
    for item in objects_lists.material_set:
        item.pokaz_pozycje()


def zloz_zamowienie():
    wybrany_material = int(input("Wybierz obiekt ktory chcesz zamowic (podaj jego ID): "))
    for item in objects_lists.material_set: #szukam materialu o wybranym id w liscie materialow
        if item.id_number == wybrany_material:
            if objects_lists.user_set[logged_id].stan_konta >= objects_lists.material_set[wybrany_material].cena: #sprawdzam czy stan konta jest wiekszy od ceny materialu
                if item.jest_dostepne: #sprawdzam czy material jest dostepny i zmniejszam dostepna liczbe o jeden
                    item.dostepna_liczba -= 1
                    if item.dostepna_liczba == 0:
                        item.jest_dostepne = False
                    objects_lists.user_set[logged_id].stan_konta -= objects_lists.material_set[wybrany_material].cena #zmniejszam stan konta o cene materialu
                    print("Zamowienie zlozone.\n")
                    break
            else:
                print("Masz za malo srodkow na koncie. Doladuj konto lub wybierz tanszy produkt.\n")
                print("\n")
                break
    print("Niestety nie mamy produktu o takim ID. Wybierz inny produkt lub wroc do menu.\n")


def doladuj_konto():
    kwota = int(input("Podaj kwote ktora chcesz doladowac konto (jesli wpiszesz 0 operacja zostanie przerwana: "))
    while kwota < 0:
        if kwota == 0:
            break
        kwota = int(input("Kwota nie moze byc ujemna. Podaj kwote jeszcze raz: "))


def menu(state): #  -> object # state to stan zalogowania. Jego wartosc to 0 lub 1 (ewentualnie True lub False)
    print("Wybierz operacje do wykonania: ")
    if state==False:
        print("1. Rejestracja")
        print("2. Logowanie")
        wybranaOperacja = int(input())
        if wybranaOperacja == 1:
            rejestracja()
        elif wybranaOperacja == 2:
            logowanie()
    print("1. Pokaz klientow: ")
    print("2. Pokaz materialy: ")
    print("3. Pokaz klientow i materialy: ")
    print("4. Zloz zamowienie: ")
    print("5. Anuluj zamowienie: ")
    print("6. Pokaz zamowienia: ")
    print("7. Doladuj konto: \n")
    print("8. Wyjdz z aplikacji: \n")
    wybranaOperacja = int(input())
    if wybranaOperacja == 1:
        pokaz_klientow()
        menu(1)
    elif wybranaOperacja == 2:
        pokaz_materialy()
        menu(1)
    elif wybranaOperacja == 3:
        pokaz_klientow()
        pokaz_materialy()
        menu(1)
    elif wybranaOperacja == 4:
        zloz_zamowienie()
        menu(1)
    elif wybranaOperacja == 7:
        doladuj_konto()
        menu(1)
    elif wybranaOperacja == 8:
        pass
    print("\n\n")
