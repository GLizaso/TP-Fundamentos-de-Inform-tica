import unittest
import Quimica

class TestCompuesto(unittest.TestCase):
    def test_cant_atomos(self):
        self.assertEqual(4, Quimica.amoniaco.cantAtomos())

    def test_atomosde(self):
        self.assertEqual(["H1", "H2", "H3"], Quimica.amoniaco.atomosDe(Quimica.tabla.elementoS('H')))

    def test_incluye_atomo(self):
        self.assertTrue(Quimica.amoniaco.incluyeAtomo("N1"))

    def test_incluye_atomo_dos(self):
        self.assertFalse(Quimica.amoniaco.incluyeAtomo("N4"))

    def test_incluye_elemento(self):
        self.assertTrue(Quimica.amoniaco.incluyeElemento(Quimica.tabla.elementoS('N')))

    def test_incluye_elemento_dos(self):
        self.assertFalse(Quimica.amoniaco.incluyeElemento(Quimica.tabla.elementoS('O')))

    def test_cant_enlaces(self):
        self.assertEqual(3, Quimica.amoniaco.cantEnlaces())

    def test_cant_enlaces_atomo(self):
        self.assertEqual(1, Quimica.amoniaco.cantEnlacesAtomo("H2"))

    def test_masa_molar(self):
        self.assertEqual(17, Quimica.amoniaco.masaMolar())

    def test_masa_molar_agua(self):
        self.assertEqual(18, Quimica.agua.masaMolar())

    def test_proporcion(self):
        self.assertEqual(0.8235, Quimica.amoniaco.proporcionElementoSobreMasa(Quimica.tabla.elementoS('N')))


