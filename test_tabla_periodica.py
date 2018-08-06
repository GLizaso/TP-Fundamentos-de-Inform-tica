import unittest
import Quimica

class TestTabla(unittest.TestCase):
    def test_tabla_periodica_tamanio(self):
        self.assertEqual(4, len(Quimica.tabla.elementos()))
