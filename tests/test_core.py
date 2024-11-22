# Pruebas básicas del sistema

import unittest
from models.cotizante import Cotizante
from logic.validations import BusinessLogic
from structures.linked_list import LinkedList
from structures.priority_queue import PriorityQueue

class TestCoreSystem(unittest.TestCase):
    def test_validar_cotizante(self):
        cotizante_valido = Cotizante(1, "Juan Perez", "123456789", "Porvenix", "Colpensionex", False)
        cotizante_invalido = Cotizante(2, "Ana Gomez", "987654321", "Porvenix", "Porvenix", False)
        self.assertTrue(BusinessLogic.validar_cotizante(cotizante_valido))
        self.assertFalse(BusinessLogic.validar_cotizante(cotizante_invalido))

    def test_validar_embargo(self):
        cotizante_embargo = Cotizante(3, "Luis Martinez", "112233445", "Porvenix", "Colpensionex", True)
        cotizante_no_embargo = Cotizante(4, "Laura Ruiz", "998877665", "Porvenix", "Colpensionex", False)
        self.assertTrue(BusinessLogic.validar_embargo(cotizante_embargo))
        self.assertFalse(BusinessLogic.validar_embargo(cotizante_no_embargo))

    def test_linked_list(self):
        lista = LinkedList()
        lista.append("Elemento 1")
        lista.append("Elemento 2")
        self.assertEqual(list(lista), ["Elemento 1", "Elemento 2"])

    def test_priority_queue(self):
        cola = PriorityQueue()
        cola.push(2, "Elemento 2")
        cola.push(1, "Elemento 1")
        self.assertEqual(cola.pop(), "Elemento 1")
        self.assertEqual(cola.pop(), "Elemento 2")


if __name__ == "__main__":
    unittest.main()
