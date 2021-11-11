from Domain.inventar import gestionare_obiect, get_id

def adauga_obiect(id, nume, descriere, pret, locatie, lista):
    '''
    adauga un obiect intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: o lista continand atat elemente vechi, cat si noul obiect
    '''
    if get_by_id(id, lista) is not None:
<<<<<<< HEAD
        raise ValueError("id-ul exista deja")
    if pret < 0:
        raise ValueError("nu exista pret negativ")
    if len(locatie) != 4:
        raise ValueError("locatia are mai mult sau mai putin de 4 caractere")
=======
        raise ValueError("id existent")
    if pret < 0 :
        raise ValueError("pret negativ")
>>>>>>> c321a4a071b1fd1627882ebcfc18cd9933803ff2
    obiect = gestionare_obiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]

def get_by_id(id, lista):
    '''
    gaseste un obiect cu id-ul dat intr-o lista
    :param id: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat din lista sau None, daca nu exista
    '''
    for obiect in lista:
        if get_id(obiect) == id:
            return obiect
    return None

def sterge_obiect(id, lista):
    '''
    sterge un obiect cu id-ul dat din lista
    :param id: id-ul obiectului care se sterge
    :param lista: lista de obiecte
    :return: o lista de obiecte fara elementul cu id dat
    '''
    if get_by_id(id,lista) is None:
        raise ValueError("nu exista")
    return [obiect for obiect in lista if get_id(obiect) != id]

def modifica_obiect(id, nume, descriere, pret, locatie, lista):
    '''
    modifica un obiect cu id-ul dat
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret: pretul obiectului
    :param locatie: locatia obiectului
    :param lista: lista de obiecte
    :return: lista modificata
    '''
<<<<<<< HEAD
    if pret < 0:
        raise ValueError("pretul nu poate fi negativ")
    if len(locatie) !=4:
        raise ValueError("locatia are mai mai mult sau mai putin de 4 caractere")
=======
    if get_by_id(id,lista) is None:
        raise ValueError("nu exista")
>>>>>>> c321a4a071b1fd1627882ebcfc18cd9933803ff2
    lista_noua = []
    for obiect in lista:
        if get_id(obiect) == id:
            obiect_nou = gestionare_obiect(id, nume, descriere, pret, locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua

