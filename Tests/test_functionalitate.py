from Domain.inventar import get_locatie, get_descriere, get_id
from Logic.CRUD import adauga_obiect, get_by_id, adauga_obiect_undo_redo
from Logic.functionalitate import mutare_obiect, concatenare_string, pret_max, ordonare_obiecte, suma_preturi, Undo, Redo


def test_mutare_obiect():
    lista = []
    undo = []
    redo = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s201", lista)
    lista = adauga_obiect("2", "birou", "lemn", 200, "s202", lista)
    lista = adauga_obiect("3", "scaune", "tapiatate", 100, "s203", lista)

    lista = mutare_obiect("s204", lista, undo, redo)

    assert get_locatie(get_by_id("1", lista)) == "s204"
    assert get_locatie(get_by_id("2", lista)) == "s204"
    assert get_locatie(get_by_id("3", lista)) == "s204"


def test_concatenare():
    lista = []
    undo = []
    redo = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s201", lista)
    lista = adauga_obiect("2", "birou", "lemn", 200, "s202", lista)
    lista = adauga_obiect("3", "scaune", "tapitate", 100, "s203", lista)

    lista = concatenare_string(150, "mobilier", lista, undo, redo)

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
    undo = []
    redo = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s203", lista)
    lista = adauga_obiect("2", "scaun", "lemn", 200, "s203", lista)
    lista = adauga_obiect("3", "ceas", "digital", 100, "s203", lista)

    rezultat = ordonare_obiecte(lista, undo, redo)

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

def test_undo_redo():
    lista = []
    undo = []
    redo = []
    lista = adauga_obiect_undo_redo("1", "tabla", "alba", 300, "s203", lista, undo, redo)
    lista = adauga_obiect_undo_redo("2", "scaun", "lemn", 200, "s203", lista, undo, redo)
    lista = adauga_obiect_undo_redo("3", "ceas", "digital", 100, "s203", lista, undo, redo)
    assert lista == [{"id": "1", "nume": "tabla", "descriere": "alba", "pret":300, "locatie": "s203"}, {"id": "2", "nume": "scaun", "descriere": "lemn", "pret":200, "locatie": "s203"}, {"id": "3", "nume": "ceas", "descriere": "digital", "pret":100, "locatie": "s203"}]
    lista = Undo(lista, undo, redo)
    assert lista == [{"id": "1", "nume": "tabla", "descriere": "alba", "pret":300, "locatie": "s203"}, {"id": "2", "nume": "scaun", "descriere": "lemn", "pret":200, "locatie": "s203"}]
    lista = Undo(lista, undo, redo)
    assert lista == [{"id": "1", "nume": "tabla", "descriere": "alba", "pret":300, "locatie": "s203"}]
    lista = Undo(lista, undo, redo)
    assert lista == []
    lista = Undo(lista, undo, redo)
    assert lista is None
    undo = []
    redo = []
    lista = []
    lista = adauga_obiect_undo_redo("4", "telefon", "apple", 6000, "s203", lista, undo, redo)
    lista = adauga_obiect_undo_redo("5", "telefon", "apple", 7000, "s203", lista, undo, redo)
    lista = adauga_obiect_undo_redo("6", "telefon", "apple", 8000, "s203", lista, undo, redo)
    lista = Redo(lista, undo, redo)
    assert lista == [{"id": "4", "nume": "telefon", "descriere": "apple", "pret": 6000, "locatie": "s203"},
                     {"id": "5", "nume": "telefon", "descriere": "apple", "pret": 7000, "locatie": "s203"},
                     {"id": "6", "nume": "telefon", "descriere": "apple", "pret": 8000, "locatie": "s203"}]
    lista = Undo(lista, undo, redo)
    lista = Undo(lista, undo, redo)
    assert lista == [{"id": "4", "nume": "telefon", "descriere": "apple", "pret": 6000, "locatie": "s203"}]
    lista = Redo(lista, undo, redo)
    assert lista == [{"id": "4", "nume": "telefon", "descriere": "apple", "pret": 6000, "locatie": "s203"},
                     {"id": "5", "nume": "telefon", "descriere": "apple", "pret": 7000, "locatie": "s203"}]
    lista = Redo(lista, undo, redo)
    assert lista == [{"id": "4", "nume": "telefon", "descriere": "apple", "pret": 6000, "locatie": "s203"},
                     {"id": "5", "nume": "telefon", "descriere": "apple", "pret": 7000, "locatie": "s203"},
                     {"id": "6", "nume": "telefon", "descriere": "apple", "pret": 8000, "locatie": "s203"}]
    lista = Undo(lista, undo, redo)
    lista = Undo(lista, undo, redo)
    lista = adauga_obiect_undo_redo("7", "telefon", "apple", 9000, "s203", lista, undo, redo)
    assert lista == [{"id": "4", "nume": "telefon", "descriere": "apple", "pret": 6000, "locatie": "s203"},
                     {"id": "7", "nume": "telefon", "descriere": "apple", "pret": 9000, "locatie": "s203"}]
    lista = Redo(lista, undo, redo)
    assert lista == [{"id": "4", "nume": "telefon", "descriere": "apple", "pret": 6000, "locatie": "s203"},
                     {"id": "7", "nume": "telefon", "descriere": "apple", "pret": 9000, "locatie": "s203"}]
    lista = Undo(lista, undo, redo)
    assert lista == [{"id": "4", "nume": "telefon", "descriere": "apple", "pret": 6000, "locatie": "s203"}]
    lista = Undo(lista, undo, redo)
    assert lista == []
    lista = Redo(lista, undo, redo)
    lista = Redo(lista, undo, redo)
    assert lista == [{"id": "4", "nume": "telefon", "descriere": "apple", "pret": 6000, "locatie": "s203"},
                     {"id": "7", "nume": "telefon", "descriere": "apple", "pret": 9000, "locatie": "s203"}]
    lista = Redo (lista, undo, redo)
    assert lista == [{"id": "4", "nume": "telefon", "descriere": "apple", "pret": 6000, "locatie": "s203"},
                     {"id": "7", "nume": "telefon", "descriere": "apple", "pret": 9000, "locatie": "s203"}]






