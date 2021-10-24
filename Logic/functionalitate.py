from Domain.inventar import get_id,get_nume,get_descriere,get_pret,get_locatie,gestionare_obiect
def mutare_obiect(locatie_noua, lista):
    get_locati = locatie_noua
    for obiect in lista:
        obiect_mutat = gestionare_obiect(
            get_id(obiect),
            get_nume(obiect),
            get_descriere(obiect),
            get_pret(obiect),
            get_locatie(obiect),
        )
        lista.append(obiect_mutat)
    return lista
