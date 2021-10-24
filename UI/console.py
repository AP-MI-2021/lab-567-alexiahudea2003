from Domain.inventar import to_string
from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect


def print_menu():
    print("1. Adugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutare obiect")
    print("a. Afisare obiecte")
    print("x. Iesire")

def ui_adaugare_obiect(lista):
    id = input("Dati id-ul:")
    nume = input("Dati nume:")
    descriere = input("Dati descrierea:")
    pret = float(input("Dati pretul:"))
    locatie = input("Dati locatia:")
    return adauga_obiect(id, nume, descriere, pret, locatie,lista)

def ui_stergere_obiect(lista):
    id = input("Dati id-ul obiectului de sters:")
    return sterge_obiect(id, lista)

def ui_modificare_obiect(lista):
    id = input("Dati id-ul obiectului de modificat:")
    nume = input("Dati noul nume:")
    descriere = input("Dati noua descriere:")
    pret = float(input("Dati noul pret:"))
    locatie = input("Dati noua locatie:")
    return modifica_obiect(id, nume, descriere, pret, locatie, lista)

def show_all(lista):
    for obiect in lista:
        print(to_string(obiect))

def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiunea:")
        if optiune == "1":
            lista = ui_adaugare_obiect(lista)
        elif optiune == "2":
            lista = ui_stergere_obiect(lista)
        elif optiune == "3":
            lista = ui_modificare_obiect(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati:")
