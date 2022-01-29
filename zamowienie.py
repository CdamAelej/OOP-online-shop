class Zamowienie:
    def __init__(self, id_zamowienia, id_zamawiajacego, id_przedmiotu):
        self.id_zamowienia = id_zamowienia
        self.id_zamawiajacego = id_zamawiajacego
        self.id_przedmiotu = id_przedmiotu
        self.lista_zamowien = []

    def __del__(self):
        print("Zamowienie zostalo anulowane")
    # def zamow(self):
