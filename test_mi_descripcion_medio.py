import unittest
import Quimica

class TestDescripcionMedio(unittest.TestCase):

    def test_aparece_compuesto_agua(self):
        return self.assertTrue(Quimica.miDescripcion.apareceCompuesto(Quimica.agua))

    def test_quienes_aparecen(self):
        return self.assertEqual([Quimica.agua],[Quimica.agua])
    
    """
    def test_aparece_compuesto_co2(self):
    
    def test_aparece_compuesto_nh3(self):
    
    def test_moles_compuesto_agua(self):
    
    def test_moles_compuesto_co2(self):
    
    def test_moles_compuesto_nh3(self):
    
    
    
    
    
    """