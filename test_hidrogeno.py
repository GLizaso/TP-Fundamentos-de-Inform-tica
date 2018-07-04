import unittest
import Quimica

class TestHidrogeno(unittest.TestCase):
    def test_cant_protones(self):
        self.assertEqual(1, Quimica.hidrogeno.cantProtones())
    def test_cant_electrones(self):
        self.assertEqual(1, Quimica.hidrogeno.cantElectrones())
    def test_peso_atomico(self):
        self.assertEqual(2, Quimica.hidrogeno.pesoAtomico())