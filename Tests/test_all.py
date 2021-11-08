from Tests.test_CRUD import test_adauga_obiect, test_sterge_obiect, test_modifica_obiect
from Tests.test_Domain import test_obiect
from Tests.test_functionalitate import test_concatenare, test_pret_max, test_ordonare_obiecte, test_suma_preturi, \
    test_undo_redo


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_sterge_obiect()
    test_modifica_obiect()
    test_concatenare()
    test_pret_max()
    test_ordonare_obiecte()
    test_suma_preturi()
    test_undo_redo()