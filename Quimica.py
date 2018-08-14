import re

class Elemento:
    def __init__(self, simbolo, numeroAtomico, cantNeutrones, valencia):
        self._simbolo = simbolo
        self._numeroAtomico = numeroAtomico
        self._cantNeutrones = cantNeutrones
        self._valencia = valencia

    def cantProtones(self):
        return self._numeroAtomico

    def cantNeutrones(self):
        return self._cantNeutrones

    def cantElectrones(self):
        return self._numeroAtomico

    def numeroAtomico(self):
        return self._numeroAtomico

    def pesoAtomico(self):
        peso = self._numeroAtomico + self._cantNeutrones
        return peso

    def valencia(self):
        return self._valencia

    def simbolo(self):
        return self._simbolo


class TablaPeriodica:
    def __init__(self):
        self.elementosatributo = []

    def elementos(self):
        return self.elementosatributo

    def agregarElemento(self, elemento_x):
        if self.elementoS(elemento_x.simbolo()) is None:
            self.elementosatributo.append(elemento_x)

    def elementoS(self, simbolo):
        return self.findElemento(simbolo, lambda elemento: elemento.simbolo())

    def elementoN(self, numero):
        return self.findElemento(numero, lambda elemento: elemento.numeroAtomico())

    def findElemento(self, atributo, mensaje):
        return next((elemento for elemento in self.elementos() if mensaje(elemento) == atributo), None)


class Compuesto:
    def __init__(self, formula):
        self.formula = formula
        self.elementosConAtomo = []
        self.enlaces = []


    def agregarAtomo(self, elemento, nombreAtomo):
        if self.findelemento(elemento) is None:
            self.elementosConAtomo.append(ElementoConAtomo(elemento, nombreAtomo))
        else:
            self.findelemento(elemento).agregarAtomo(nombreAtomo)

    def findelemento(self, elementobuscar):
        return next((elemento for elemento in self.elementosConAtomo if elemento.getelemento() == elementobuscar), None)

    def enlazar(self, atomo1, atomo2):
        enlace = Enlace(atomo1, atomo2)
        self.agregarEnlace(enlace)

    def agregarEnlace(self, enlace):
        self.enlaces.append(enlace)

    def getEnlaces(self):
        return self.enlaces

    def getElementoConAtomo(self):
        return self.elementosConAtomo

    def cantAtomos(self):
        return sum((map(lambda elementoConAtomo: elementoConAtomo.cantAtomos(), self.elementosConAtomo)))

    def atomosDe(self, elemento):
        return self.findelemento(elemento).getAtomo()

    def incluyeAtomo(self, atomo):
        return any(map(lambda elementoConAtomo: atomo in elementoConAtomo.getAtomo(), self.elementosConAtomo))

    def incluyeElemento(self, elemento):
        return any(map(lambda elementoConAtomo: elemento == elementoConAtomo.getelemento(), self.elementosConAtomo))

    def elementosPresentes(self):
        return list(map(lambda elemento: elemento.getelemento(), self.elementosConAtomo))

    def cantEnlaces(self):
        return len(self.enlaces)

    def cantEnlacesAtomo(self, atomo):
        return len(list(self.findenlaceatomo(atomo)))

    def findenlaceatomo(self, atomo):
        return (enlace for enlace in self.enlaces if enlace.tieneAtomo(atomo))

    def masaElemento(self,elemento):
        elementoBuscado = self.findelemento(elemento)
        if elementoBuscado != None:
            return elementoBuscado.masaElemento()
        return 0

    def masaMolar(self):
        return sum(map(lambda elemento: elemento.masaElemento(), self.elementosConAtomo))

    def proporcionElementoSobreMasa(self, elemento):
        return elemento.pesoAtomico()/ self.masaMolar()

    def getFormula(self):
        return self.formula


class CompuestoAux:
    def __init__(self, compuesto, moles):
        self.compuesto = compuesto
        self.moles = moles

    def getmoles(self):
        return self.moles

    def getcompuesto(self):
        return self.compuesto

    def aniadirmoles(self, cantidadMoles):
        self.moles = self.moles + cantidadMoles

    def masaCompuesto(self, compuesto):
        if compuesto == self.compuesto:
            return compuesto.masaMolar()
        else:
            return 0


    def masaMolarCompuesto(self,compuesto):
        if compuesto == self.compuesto:
            return compuesto.masaMolar()*self.moles
        else:
            return 0



class ElementoConAtomo:
    def __init__(self, elemento, nombreAtomo):
        self.elemento = elemento
        self.listaAtomo = [nombreAtomo]

    def getelemento(self):
        return self.elemento

    def agregarAtomo(self, atomo):
        self.listaAtomo.append(atomo)

    def getAtomo(self):
        return self.listaAtomo

    def cantAtomos(self):
        return len(self.listaAtomo)

    def masaElemento(self):
       return self.elemento.pesoAtomico()*self.cantAtomos() #issue

class Enlace:
    def __init__(self, atomo1, atomo2):
        self.atomo1 = atomo1
        self.atomo2 = atomo2

    def tieneAtomo(self, atomo):
        return (atomo == self.atomo1) or (atomo == self.atomo2)

    def getEnlace(self):
        return self.atomo1+self.atomo2

class Medio:
    def __init__(self):
        self.listacompuestos = []

    def inicializar(self,lista):
        self.listacompuestos = lista

    def agregarComponente(self, compuesto, cantMoles):
        if self.findcompuesto(compuesto) is None:
            self.listacompuestos.append(CompuestoAux(compuesto, cantMoles))
        else:
            self.findcompuesto(compuesto).aniadirmoles(cantMoles)

    def findcompuesto(self, compuesto):
        return next((compuesto for compuesto in self.listacompuestos if compuesto.getcompuesto == compuesto), None)

    def masaTotal(self):
        return self.sumaMasa(lambda compuesto: compuesto.masaMolarCompuesto(compuesto))

    def elementosPresentes(self):
        elementosP = []
        for compuestoAux in self.listacompuestos:
            listaElementos = compuestoAux.getcompuesto().getElementoConAtomo()
            self.agregarElemento(elementosP,listaElementos)
        return elementosP

    def agregarElemento(self, lista1, lista2):
        for elemento in lista2:
            if elemento.getelemento() not in lista1:
                lista1.append(elemento.getelemento())

    def agregarCompuesto(self, lista1, lista2):
        for compuesto in lista2:
            if compuesto not in lista1:
                lista1.append(compuesto)

    def compuestosPresentes(self):
        compuestosP = []
        listaCompuesto = map(lambda compuesto: compuesto.getcompuesto(), self.listacompuestos)
        self.agregarCompuesto(compuestosP, listaCompuesto)
        return compuestosP

    def masaDeCompuesto(self, comp):
        return self.sumaMasa(lambda compuesto: compuesto.masaMolarCompuesto(comp))

    def masaDeElemento(self, elemento):
        return self.sumaMasa(lambda compuesto: compuesto.getcompuesto().masaElemento(elemento) * compuesto.getmoles())

    def proporcionElementoSobreMasa(self, elemento):
        return self.masaDeElemento()/self.masaTotal()

    def proporcionCompuestoSobreMasa(self,compuesto):
        return self.masaDeCompuesto() / self.masaTotal()

    def masaMolar(self):
        return self.sumaMasa(lambda compuesto: compuesto.masaMolarCompuesto())

    def sumaMasa(self, unaLambda):
        return sum(map(unaLambda, self.listacompuestos))

    def getlistacompuesto(self):
        return self.listacompuestos


def descripcionMedioRE(string):
    return re.findall('\[(.*?)\]', string)


class DescripcionMedio:
    def __init__(self, stringcompuestos):
        self.lista = descripcionMedioRE(stringcompuestos)
        self.listaCompuestos = list(set(self.lista))
        self.medio = Medio()
        self.medio.inicializar([])

    def apareceCompuesto(self, comp):
        return comp.getFormula() in self.listaCompuestos

    def molesCompuesto(self, comp):
        print(comp.getFormula())
        return self.lista.count(comp.getFormula())

    def quienesAparecen(self, listaDeCompuestos):
        return list(set(map(lambda comp: comp.getcompuesto(),
                   self.medio.getlistacompuesto())) & set(listaDeCompuestos))

    def agregarAMedio(self, medio, compuesto):
        medio.agregarComponente(compuesto, self.molesCompuesto(compuesto))

    def getMedio(self):
        return self.medio



oxigeno = Elemento('O', 8, 8, 4)
hidrogeno = Elemento('H', 1, 0, 1)
carbono = Elemento('C', 6, 6, 2)
nitrogeno = Elemento('N', 7, 7, 4)

tabla = TablaPeriodica()
tabla.agregarElemento(hidrogeno)
tabla.agregarElemento(oxigeno)
tabla.agregarElemento(nitrogeno)
tabla.agregarElemento(carbono)

agua = Compuesto("H2O")
agua.agregarAtomo(hidrogeno, "H1")
agua.agregarAtomo(hidrogeno, "H2")
agua.agregarAtomo(oxigeno, "O1")
agua.enlazar("H1", "O1")
agua.enlazar("H2", "O1")

amoniaco = Compuesto("NH3")
amoniaco.agregarAtomo(hidrogeno, "H1")
amoniaco.agregarAtomo(hidrogeno, "H2")
amoniaco.agregarAtomo(hidrogeno, "H3")
amoniaco.agregarAtomo(nitrogeno, "N1")
amoniaco.enlazar("H1", "N1")
amoniaco.enlazar("H2", "N1")
amoniaco.enlazar("H3", "N1")

co2 = Compuesto("CO2")
co2.agregarAtomo(carbono, "C1")
co2.agregarAtomo(oxigeno, "O1")
co2.agregarAtomo(oxigeno, "O2")
co2.enlazar("O1" , "C1")
co2.enlazar("O2" , "C1")

metano = Compuesto("CH4")
metano.agregarAtomo(carbono, "C1")
metano.agregarAtomo(hidrogeno, "H1")
metano.agregarAtomo(hidrogeno, "H2")
metano.agregarAtomo(hidrogeno, "H3")
metano.agregarAtomo(hidrogeno, "H4")
metano.enlazar("H1" , "C1" )
metano.enlazar("H2" , "C1" )
metano.enlazar("H3" , "C1" )
metano.enlazar("H4" , "C1" )



medioRaro = Medio()
medioRaro.agregarComponente(agua, 100)
medioRaro.agregarComponente(amoniaco, 6)
medioRaro.agregarComponente(metano, 20)
medioRaro.agregarComponente(co2, 14)
medioRaro.agregarComponente(amoniaco, 15)

miDescripcion = DescripcionMedio("[H2O][CO2][H2O][CH4]")
