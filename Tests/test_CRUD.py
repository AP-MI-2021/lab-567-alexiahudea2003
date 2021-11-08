from Domain.inventar import get_id, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import get_by_id, adauga_obiect, sterge_obiect, modifica_obiect


def test_adauga_obiect():
    lista = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s203", lista)

    assert len(lista) == 1
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_nume(get_by_id("1", lista)) == "tabla"
    assert get_descriere(get_by_id("1", lista)) == "alba"
    assert get_pret(get_by_id("1", lista)) == 300
    assert get_locatie(get_by_id("1", lista)) == "s203"

def test_sterge_obiect():
    lista = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s203", lista)
    lista = adauga_obiect("2", "proiector", "suspendat", 700, "s203", lista)

    lista = sterge_obiect("1", lista)

    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None

    lista = sterge_obiect("3", lista)

    assert len(lista) == 1
    assert get_by_id("2", lista) is not None

def test_modifica_obiect():
    lista = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s203", lista)
    lista = adauga_obiect("2", "proiector", "suspendat", 700, "s203", lista)

    lista = modifica_obiect("1", "ceas", "digital", 100, "s203", lista)

    obiect_updatat = get_by_id("1", lista)
    assert get_id(obiect_updatat) == "1"
    assert get_nume(obiect_updatat) == "ceas"
    assert get_descriere(obiect_updatat) == "digital"
    assert get_pret(obiect_updatat) == 100
    assert get_locatie(obiect_updatat) == "s203"

    lista = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s203", lista)
    lista = modifica_obiect("3", "ceas", "digital", 100, "s203", lista)

    obiect_neupdatat = get_by_id("1", lista)
    assert get_id(obiect_neupdatat) == "1"
    assert get_nume(obiect_neupdatat) == "tabla"
    assert get_descriere(obiect_neupdatat) == "alba"
    assert get_pret(obiect_neupdatat) == 300
    assert get_locatie(obiect_neupdatat) == "s203"

