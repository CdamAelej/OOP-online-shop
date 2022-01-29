# copyright by Adam Celej
from book import Ksiazka
from film import Film
from client import Client


k0 = Ksiazka(20, 300, "Powiesc historyczna", "Henryk", "Sienkiewicz", "Potop", 2019, 30, True, 10)
k1 = Ksiazka(21, 600, "Powiesc historyczna", "Henryk", "Sienkiewicz", "Ogniem i mieczem", 2016, 30, True, 20)
k2 = Ksiazka(22, 900, "Powiesc historyczna", "Henryk", "Sienkiewicz", "Pan Wolodyjowski", 2018, 30, True, 15)
f0 = Film(23, "Dramat historyczna", "Ridley", "Scott", "Gladiator", 2000, 155, True, True, 30, 30)
material_set = [k0, k1, k2, f0]

user0 = Client(0, "haslo_ale_nie_maslo", "Adam", "Celej", "mezczyzna", 20, 0, 0)
user1 = Client(1, "haslo_ale_maslo", "Adam", "Kokosza", "mezczyzna", 20, 0, 0)
user2 = Client(3, "haslo123", "Julia", "Nowak", "kobieta", 22, 0, 0)
user3 = Client(3, "RomaInvicra", "Alicja", "Kowalska", "kobieta", 16, 0, 0)
user4 = Client(4, "Covid_to_sciema", "Blanka", "Wysocka", "kobieta", 22, 0, 0)
user_set = [user0, user1, user2, user3, user4]
