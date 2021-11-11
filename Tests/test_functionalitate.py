from Domain.inventar import get_locatie, get_descriere, get_id
from Logic.CRUD import adauga_obiect, get_by_id
from Logic.functionalitate import mutare_obiect, concatenare_string, pret_max, ordonare_obiecte, suma_preturi


def test_mutare_obiect():
    lista = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s201", lista)
    lista = adauga_obiect("2", "birou", "lemn", 200, "s202", lista)
    lista = adauga_obiect("3", "scaune", "tapiatate", 100, "s203", lista)

    lista = mutare_obiect("s204", lista)

    assert get_locatie(get_by_id("1", lista)) == "s204"
    assert get_locatie(get_by_id("2", lista)) == "s204"
    assert get_locatie(get_by_id("3", lista)) == "s204"


def test_concatenare():
    lista = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s201", lista)
    lista = adauga_obiect("2", "birou", "lemn", 200, "s202", lista)
    lista = adauga_obiect("3", "scaune", "tapitate", 100, "s203", lista)

    lista = concatenare_string(150, "mobilier", lista)

    assert get_descriere(get_by_id("1", lista)) == "albamobilier"
    assert get_descriere(get_by_id("2", lista)) == "lemnmobilier"
    assert get_descriere(get_by_id("3", lista)) == "tapitate"

def test_pret_max():
    lista = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s203", lista)
    lista = adauga_obiect("2", "scaun", "lemn", 200, "s203", lista)
    lista = adauga_obiect("3", "ceas", "digital", 100, "s203", lista)

    rezultat = pret_max(lista)

    assert len(rezultat) == 1
    assert rezultat["s203"] == 300

def test_ordonare_obiecte():
    lista = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s203", lista)
    lista = adauga_obiect("2", "scaun", "lemn", 200, "s203", lista)
    lista = adauga_obiect("3", "ceas", "digital", 100, "s203", lista)

    rezultat = ordonare_obiecte(lista)

    assert get_id(rezultat[0]) == "3"
    assert get_id(rezultat[1]) == "2"
    assert get_id(rezultat[2]) == "1"

def test_suma_preturi():
    lista = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s203", lista)
    lista = adauga_obiect("2", "scaun", "lemn", 200, "s203", lista)
    lista = adauga_obiect("3", "ceas", "digital", 100, "s203", lista)

    rezultat = suma_preturi(lista)

    assert len(rezultat) == 1
    assert rezultat["s203"] == 600

<<<<<<< HEAD

=======
>>>>>>> 0abe628d5eac2681fc158c926964e5df6b72a16d
