from Domain.inventar import gestionare_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie

def mutare_obiect(locatie_noua, lista):
    '''
    mutarea obiectelor intr-o locatie data
    :param locatie: string
    :param lista: lista de obiecte
    :return: mutarea obiectelor intr-o locatie
    '''
    lista_noua = []
    for obiect in lista:
        lista_noua.append(gestionare_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect), get_pret(obiect), locatie_noua))
    return lista_noua

def concatenare_string(valoarea, string, lista):
    '''
    concatenarea unui string in functie de valoarea data
    :param valoarea: float
    :param string: string
    :param lista: lista obiecte
    :return: concatenare string
    '''
    lista_noua = []
    for obiect in lista:
        if get_pret(obiect) > float(valoarea):
            lista_noua.append(gestionare_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect)+string, get_pret(obiect), get_locatie(obiect)))
        else:
            lista_noua.append(obiect)
    return lista_noua
