from Domain.inventar import to_string, gestionare_obiect, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect, get_by_id
from Logic.functionalitate import mutare_obiect, pret_max, ordonare_obiecte, suma_preturi
from Tests.test_functionalitate import concatenare_string


def print_menu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutare obiect")
    print("5. Concatenare")
    print("6. Pretul maxim al obiectelor dintr-o locatie")
    print("7. Ordonarea obiectelor crescator dupa pret")
    print("8. Afisarea sumelor preturilor pentru fiecare locatie")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare obiecte")
    print("x. Iesire")

def ui_adaugare_obiect(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul:")
        nume = input("Dati nume:")
        descriere = input("Dati descrierea:")
        pret = float(input("Dati pretul:"))
        locatie = input("Dati locatia:")
        rezultat = adauga_obiect(id, nume, descriere, pret, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_stergere_obiect(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul obiectului de sters:")
        rezultat = sterge_obiect(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_modificare_obiect(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul obiectului de modificat:")
        nume = input("Dati noul nume:")
        descriere = input("Dati noua descriere:")
        pret = float(input("Dati noul pret:"))
        locatie = input("Dati noua locatie:")
        rezultat = modifica_obiect(id, nume, descriere, pret, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def show_all(lista):
    for obiect in lista:
        print(to_string(obiect))

def ui_mutare_obiect(lista, undo_list, redo_list):
    locatie_noua = input("Dati noua locatie:")
    rezultat = mutare_obiect(locatie_noua, lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def ui_concatenare(lista, undo_list, redo_list):
    try:
        valoarea = float(input("Dati valoarea:"))
        string = str(input("Dati string-ul:"))
        rezultat = concatenare_string(valoarea, string, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_pret_max(lista):
    rezultat = pret_max(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie, rezultat[locatie]))

def ui_ordonare_obiecte(lista):
    show_all(ordonare_obiecte(lista))

def ui_suma_preturi(lista):
    rezultat = suma_preturi(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))

def run_menu(lista):
    undo_list = []
    redo_list = []
    while True:
        print_menu()
        optiune = input("Dati optiunea:")
        if optiune == "1":
            lista = ui_adaugare_obiect(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_stergere_obiect(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modificare_obiect(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = ui_mutare_obiect(lista, undo_list, redo_list)
        elif optiune == "5":
            ui_concatenare(lista, undo_list, redo_list)
        elif optiune == "6":
            ui_pret_max(lista)
        elif optiune == "7":
            ui_ordonare_obiecte(lista)
        elif optiune == "8":
            ui_suma_preturi(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati:")



