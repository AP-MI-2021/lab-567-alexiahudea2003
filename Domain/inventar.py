def gestionare_obiect(id, nume, descriere, pret, locatie):
    '''
    creeaza un dictionar ce reprezinta inventarul unei institutii
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: un dictionar reprezentand inventarul unei institutii
    '''
    return[id, nume, descriere, pret, locatie]

def get_id(obiect):
    '''
    da id-ul unui obiect din inventar
    :param obiect: dictionar ce contine un obiect
    :return: id-ul obiectului
    '''
    return obiect[0]

def get_nume(obiect):
    '''
    da numele unui obiect din inventar
    :param obiect: dictionar ce contine un obiect
    :return: numele obiectului
    '''
    return obiect[1]

def get_descriere(obiect):
    '''
    da descrierea unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: descrierea obiectului
    '''
    return obiect[2]

def get_pret(obiect):
    '''
    da pretul unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: pretul obiectului
    '''
    return obiect[3]

def get_locatie(obiect):
    '''
    da locatia unui obiect
    :param obiect: dictionar ce contine un obiect
    :return: locatia obiectului
    '''
    return obiect[4]

def to_string(obiect):
    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie: {}".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret(obiect),
        get_locatie(obiect)
    )
