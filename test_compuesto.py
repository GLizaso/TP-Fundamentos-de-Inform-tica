import unittest
import Quimica

class TestCompuesto(unittest.TestCase):
    def test_cant_atomos(self):
        self.assertEqual(4, Quimica.amoniaco.cantAtomos())
    def test_atomosde(self):
        self.assertEqual(["H1", "H2", "H3"], Quimica.amoniaco.atomosDe(Quimica.tabla.elementoS('H')))
    def test_incluye_atomo(self):
        self.assertTrue(Quimica.amoniaco.incluyeAtomo("N1"))
    def test_inclye_atomo_dos(self):
        self.assertTrue(Quimica.amoniaco.incluyeAtomo("N4"))
    def test_inclye_elemento(self):
        self.assertTrue(Quimica.amoniaco.incluyeElemento(Quimica.tabla.elementoS('N')))
    def test_inclye_elemento_dos(self):
        self.assertTrue(Quimica.amoniaco.incluyeElemento(Quimica.tabla.elementoS('O')))
    def test_cant_enlaces(self):
        self.assertEqual(3, Quimica.amoniaco.cantEnlaces())
    def test_cant_enlaces_atomo(self):
        self.assertEqual(1, Quimica.amoniaco.cantEnlacesAtomo("H2"))
    def test_masa_molar(self):
        self.assertEqual(17, Quimica.amoniaco.masaMolar())
#    def test_proporcion(self):
#        self.assertEqual(0,8235, Quimica.amoniaco.proporcionElementoSobreMasa(Quimica.tabla.elementos('N')))


"""
nh3.cantAtomos()	4
nh3.atomosDe(tabla.elementoS('H'))	["H1", "H2", "H3"]
nh3.incluyeAtomo("N1")	True
nh3.incluyeAtomo("N4")	False
nh3.incluyeElemento(tabla.elementoS('N'))	True
nh3.incluyeElemento(tabla.elementoS('O'))	False

[elem.simbolo() for elem in nh3.elementosPresentes()]	["N","H"]


nh3.cantEnlaces()]	3
nh3.cantEnlacesAtomo("H2")]	1
nh3.masaMolar()]	17
nh3.proporcionSobreMasa(tabla.elementoS('N'))
"""