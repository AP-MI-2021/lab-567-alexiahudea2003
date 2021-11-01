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
    lista_noua = []
    for obiect in lista:
        if get_id(obiect) == id:
            obiect_nou = gestionare_obiect(id, nume, descriere, pret, locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua
