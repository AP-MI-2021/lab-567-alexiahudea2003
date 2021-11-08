from Domain.inventar import gestionare_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie


def mutare_obiect(locatie_noua, lista, undo_list, redo_list):
    '''
    mutarea obiectelor intr-o locatie data
    :param locatie_noua: string
    :param lista: lista de obiecte
    :return: mutarea obiectelor intr-o locatie
    '''
    lista_noua = []
    for obiect in lista:
        lista_noua.append(gestionare_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect), get_pret(obiect), locatie_noua))
    undo_list.append(lista)
    redo_list.clear()
    return lista_noua

def concatenare_string(valoarea, string, lista, undo_list, redo_list):
    '''
    concatenarea unui string in functie de valoarea data
    :param valoarea: float
    :param string: stri
    :param lista: lista obiecte
    :return: concatenare string
    '''
    lista_noua = []
    for obiect in lista:
        if get_pret(obiect) > float(valoarea):
            lista_noua.append(gestionare_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect) + string, get_pret(obiect), get_locatie(obiect)))
        else:
            lista_noua.append(obiect)
    undo_list.append(lista)
    redo_list.clear
    return lista_noua

def pret_max(lista):
    '''
    determina cel mai mare pret din fiecare locatie
    :param lista: lista obiecte
    :return: cel mai mare pret din fiecare locatie
    '''
    rezultat = {}
    for obiect in lista:
        pret = get_pret(obiect)
        locatie = get_locatie(obiect)
        if locatie in rezultat:
            if pret > rezultat[locatie]:
                rezultat[locatie] = pret
        else:
            rezultat[locatie] = pret
    return rezultat

def ordonare_obiecte(lista, undo_list, redo_list):
    '''
    ordoneaza obiectele crescator dupa pret
    :param lista: lista obiecte
    :return: ordonarea obiectelor dupa pret
    '''
    undo_list.append(lista)
    redo_list.clear()
    return sorted(lista, key = lambda obiect: get_pret(obiect))

def suma_preturi(lista):
    '''
    calculeaza suma preturilor obiectelor pentru fiecare locatie
    :param lista: lista obiecte
    :return: suma preturilor obiectelor pentru aceeasi locatie
    '''
    rezultat = {}
    for obiect in lista:
        locatie = get_locatie(obiect)
        pret = get_pret(obiect)
        if locatie in rezultat:
            rezultat[locatie] = rezultat[locatie] + pret
        else:
            rezultat[locatie] = pret
    return rezultat

def Undo(lista, undo_list, redo_list):
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    else:
        return None
    return lista

def Redo(lista, undo_list, redo_list):
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop
    return lista
