from Domain.inventar import get_locatie, get_descriere
from Logic.CRUD import adauga_obiect, get_by_id
from Logic.functionalitate import mutare_obiect,concatenare_string

def test_mutare_obiect():
    lista = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s201", lista)
    lista = adauga_obiect("2", "birou", "lemn", 200, "s202", lista)
    lista = adauga_obiect("3", "scaune", "tapitate", 100, "s203", lista)

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