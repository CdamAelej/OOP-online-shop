# copyright by Adam Celej
import book
import film
import client


k0 = book.Ksiazka(20, "Henryk", "Sienkiewicz", "Potop", "Powiesc historyczna", 2017, 984, 1, 30, 30)
k1 = book.Ksiazka(21, "Henryk", "Sienkiewicz", "Ogniem i mieczem", "Powiesc historyczna", 2016, 606, 1, 30, 30)
k2 = book.Ksiazka(22, "Henryk", "Sienkiewicz", "Pan Wolodyjowski", "Powiesc historyczna", 2018, 1080, 1, 30, 30)
f0 = film.Film(23, "Rid_numberley", "Scott", "Gladiator", 2000, "Dramat historyczna", "Russell", "Crowe", "Joaquin",
          "Phoenix",
          "Richard", "Harris", 155, 1, 1, 30, 30)
material_set = [k0, k1, k2, f0]

user0 = client.Client(0, "haslo_ale_nie_maslo", "Adam", "Celej", "mezczyzna", 20, 0, 0)
user1 = client.Client(1, "haslo_ale_maslo", "Adam", "Kokosza", "mezczyzna", 20, 0, 0)
user2 = client.Client(3, "haslo123", "Julia", "Nowak", "kobieta", 22, 0, 0)
user3 = client.Client(3, "RomaInvicra", "Alicja", "Kowalska", "kobieta", 16, 0, 0)
user4 = client.Client(4, "Covid_to_sciema", "Blanka", "Wysocka", "kobieta", 22, 0, 0)
user_set = [user0, user1, user2, user3, user4]