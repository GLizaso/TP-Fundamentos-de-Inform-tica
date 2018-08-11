import unittest
import Quimica

class TestMedioRaro(unittest.TestCase):
    def test_masa_total(self):
        self.assertEqual(3093, Quimica.medioRaro.masaTotal())

    def test_elementos_presentes(self):
        self.assertEqual([Quimica.hidrogeno, Quimica.oxigeno, Quimica.nitrogeno, Quimica.carbono], Quimica.medioRaro.elementosPresentes())

    def test_compuestos_presentes(self):
        self.assertEqual([Quimica.agua, Quimica.amoniaco, Quimica.metano, Quimica.co2], Quimica.medioRaro.compuestosPresentes())

#    def cantidad_de_moles_elemento(self):
# no pude hacer el metodo

    def test_masa_por_compuesto_agua(self):
        self.assertEqual(1800, Quimica.medioRaro.masaDeCompuesto(Quimica.agua))

    def test_masa_por_compuesto_amoniaco(self):
        self.assertEqual(357, Quimica.medioRaro.masaDeCompuesto(Quimica.amoniaco))

    def test_masa_por_elemento_oxigeno(self):
        self.assertEqual(2048, Quimica.medioRaro.masaDeElemento(Quimica.oxigeno))

    #def test_masa_por_elemento_carbono(self):
    #    self.assertEqual(408, Quimica.medioRaro.masaDeElemento(Quimica.carbono))



