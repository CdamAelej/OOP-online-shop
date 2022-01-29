from client import Client
from book import Ksiazka
from film import Film

class zamowienie(object):
    def __init__(self):
        self.zamawiajacy = Client
        self.zamawiane = Ksiazka or Film

    def pokaz_zamowienie(self):
        print("Klient o id " + str(Client().numer) + " zamowil produkt o id " + str())