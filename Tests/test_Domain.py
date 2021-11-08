from Domain.inventar import gestionare_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie


def test_obiect():
    obiect = gestionare_obiect("1", "tabla", "alba", 300, "s203")

    assert get_id(obiect) == "1"
    assert get_nume(obiect) == "tabla"
    assert get_descriere(obiect) == "alba"
    assert get_pret(obiect) == 300
    assert get_locatie(obiect) == "s203"