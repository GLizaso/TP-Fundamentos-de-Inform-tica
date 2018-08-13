import unittest
import Quimica

class TestDescripcionMedio(unittest.TestCase):

    def test_aparece_compuesto_agua(self):
        return self.assertTrue(Quimica.miDescripcion.apareceCompuesto(Quimica.agua))

    def test_aparece_compuesto_co2(self):
        return self.assertTrue(Quimica.miDescripcion.apareceCompuesto(Quimica.co2))

    def test_aparece_compuesto_nh3(self):
        return self.assertFalse(Quimica.miDescripcion.apareceCompuesto(Quimica.amoniaco))

    def test_quienes_aparecen(self):
        return self.assertEqual([Quimica.agua],[Quimica.agua])

    def test_moles_compuesto_agua(self):
        return self.assertEqual(2, Quimica.miDescripcion.molesCompuesto(Quimica.agua))

    def test_moles_compuesto_co2(self):
        return self.assertEqual(1, Quimica.miDescripcion.molesCompuesto(Quimica.co2))

    def test_moles_compuesto_nh3(self):
        return self.assertEqual(1, Quimica.miDescripcion.molesCompuesto(Quimica.amoniaco))
