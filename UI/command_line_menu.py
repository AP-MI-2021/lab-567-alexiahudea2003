from Domain.inventar import to_string
from Logic.CRUD import adauga_obiect, modifica_obiect

def adaugare_obiect(id,nume,descriere,pret,locatie,lista):
    try:
        return adauga_obiect(id,nume,descriere,pret,locatie,lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista

def modificare_obiect(id,nume,descriere,pret,locatie,lista):
    try:
        return modifica_obiect(id,nume,descriere,pret,locatie,lista)
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista

def afiseaza(lista):
    for obiect in lista:
        print(to_string(obiect))

def ajutor():
    print("Instructiuni:")
    print("add - adaugare")
    print("update - modificare")
    print("show_all - afiseaza")
    print("stop - oprire")

def meniu():
    lista = []
    go = True
    while go is True:
        text = input("Introduceti comanda:")
        comanda_lista = text.split("-")
        for optiune in comanda_lista:
            comanda = optiune.split(";")
        if comanda[0] == "add":
            lista = adaugare_obiect(comanda[1], comanda[2], comanda[3], comanda[4], comanda[5], lista)
        elif comanda[0] == "update":
            lista = modificare_obiect(comanda[1], comanda[2], comanda[3], comanda[4], comanda[5], lista)
        elif comanda[0] == "show_all":
            afiseaza(lista)
        elif comanda[0] == "ajutor":
            ajutor()
        elif comanda[0] == "stop":
            go = False
        else:
            print("Optiune gresita")
meniu()

