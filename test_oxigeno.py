import unittest
import Quimica


class TestOxigeno(unittest.TestCase):
    def test_cant_protones(self):
        self.assertEqual(8, Quimica.oxigeno.cantProtones())
    def test_cant_electrones(self):
        self.assertEqual(8, Quimica.oxigeno.cantElectrones())
    def test_peso_atomico(self):
        self.assertEqual(16, Quimica.oxigeno.pesoAtomico())