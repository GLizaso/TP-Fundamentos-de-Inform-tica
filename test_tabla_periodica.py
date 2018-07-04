import unittest
import Quimica

class TestTabla(unittest.TestCase):
    Quimica.tabla.agregarElemento(Quimica.oxigeno)
    Quimica.tabla.agregarElemento(Quimica.hidrogeno)
    Quimica.tabla.agregarElemento(Quimica.carbono)
    Quimica.tabla.agregarElemento(Quimica.nitrogeno)

    def test_tabla_periodica_tamanio(self):
        self.assertEqual(4, len(Quimica.tabla.elementos()))
