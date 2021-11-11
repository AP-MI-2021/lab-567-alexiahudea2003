from Domain.inventar import get_id
from Logic.CRUD import adauga_obiect, get_by_id
from Logic.functionalitate import concatenare_string, mutare_obiect


def test_undo_redo():
    redo_list = []
    lista = []
    undo_list = []

    rezultat = adauga_obiect("1", "tabla", "alba", 300, "s203", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = rezultat
    assert len(lista) == 1
    assert lista == [["1", "tabla", "alba", 300, "s203"]]
    assert get_id(get_by_id("1", lista)) == "1"

    rezultat = adauga_obiect("2", "proiector", "suspendat", 750, "s203", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = rezultat
    assert len(lista) == 2
    assert lista == [["1", "tabla", "alba", 300, "s203"],
                     ["2", "proiector", "suspendat", 750, "s203"]]

    rezultat = adauga_obiect("3", "ceas", "digital", 70, "s203", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = rezultat
    assert len(lista) == 3
    assert lista == [["1", "tabla", "alba", 300, "s203"],
                     ["2", "proiector", "suspendat", 750, "s203"],
                     ["3", "ceas", "digital", 70, "s203"]]

    redo_list.clear()
    lista = undo_list.pop()
    assert undo_list == [[],
                         [["1", "tabla", "alba", 300, "s203"]]]


    redo_list.append(lista)
    lista = undo_list.pop()
    assert undo_list == [[]]

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert undo_list == []

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert undo_list == []

    assert lista == []
    rezultat = adauga_obiect("4", "telefon", "fix", 150, "s203", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()
    assert redo_list == []
    assert lista == [["4", "telefon", "fix", 150, "s203"]]

    rezultat = adauga_obiect("5", "macbook", "air", 5500, "s203", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = rezultat

    rezultat = adauga_obiect("6", "macbook", "pro", 7000, "s203", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = rezultat

    assert len(lista) == 3

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert redo_list == []
    assert len(redo_list) == 0

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert undo_list == [[],
                         [["4", "telefon", "fix", 150, "s203"]]]

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert undo_list == [[]]

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(redo_list) == 1

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(redo_list) == 0

    if len(undo_list) > 0:
        redo_list.append(lista)
    lista = undo_list.pop()
    assert undo_list == [[],
                         [["4", "telefon", "fix", 150, "s203"]]]


    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert undo_list == [[]]

    rezultat = adauga_obiect("7", "casti", "beats", 750, "s203", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()
    assert len(lista) == 2
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert undo_list == [[], [["4", "telefon", "fix", 150, "s203"]]]

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert undo_list == [[]]

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert undo_list == []

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 1
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(redo_list) == 0

    rezultat = concatenare_string(33, "nou", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = rezultat
    assert lista == [["4", "telefon", "fixnou", 150, "s203"],
                     ["7", "casti", "beatsnou", 750, "s203"]]

    rezultat = concatenare_string(22, "out", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = rezultat
    assert lista == [["4", "telefon", "fixnouout", 150, "s203"],
                     ["7", "casti", "beatsnouout", 750, "s203"]]

    rezultat = adauga_obiect("1", "apple", "telefon", 6000, "s203",lista)
    undo_list.append(lista)
    redo_list.append(lista)
    lista = rezultat

    rezultat = adauga_obiect("2", "apple", "macbook", 7000, "s203",lista)
    undo_list.append(lista)
    redo_list.append(lista)
    lista = rezultat

    rezultat = mutare_obiect("s204", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = rezultat

    rezultat = mutare_obiect("s205", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = rezultat

    rezultat = mutare_obiect("s206", lista)
    undo_list.append(lista)
    redo_list.clear()
    lista = rezultat
