from Tests.test_all import run_all_tests
from UI.console import run_menu
from Logic.CRUD import adauga_obiect

def main():
    run_all_tests()
    lista = []
    lista = adauga_obiect("1", "tabla", "alba", 300, "s203", lista)
    lista = adauga_obiect("2", "proiector", "suspendat", 750, "s203", lista)
    run_menu(lista)
main()
