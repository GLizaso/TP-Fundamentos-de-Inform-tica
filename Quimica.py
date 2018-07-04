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
        self.elementosatributo=[]

    def elementos(self):
        return self.elementosatributo

    def agregarElemento(self, elemento_x):
        if self.elementoS(elemento_x.simbolo()) is None:

            self.elementosatributo.append(elemento_x) #o elementos.append(elemento)

    def elementoS(self,simbolo):
        return self.findElemento(simbolo, lambda elemento: elemento.simbolo())

    def elementoN(self,numero):
        return self.findElemento(numero, lambda elemento: elemento.numeroAtomico())

    def findElemento(self,atributo,mensaje):
        return next ((elemento for elemento in self.elementos() if mensaje(elemento) == atributo), None)




class Compuesto:
    def __init__(self, formula):
        self.formula = formula
        self.elementosConAtomo=[]
        self.enlaces = []

    def agregarAtomo(self, elemento, nombreAtomo):
        if self.findelemento(elemento) is None:
            self.elementosConAtomo.append(ElementoConAtomo(elemento, nombreAtomo))
        else:
            self.findelemento(elemento).agregarAtomo(nombreAtomo)

    def findelemento(self,elementobuscar):
        return next ((elemento for elemento in self.elementosConAtomo if elemento.getelemento == elementobuscar))

    def enlazar(self, atomo1, atomo2):
        enlace = Enlace(atomo1, atomo2)
        self.agregarEnlace(enlace)

    def agregarEnlace(self, enlace):
        self.enlaces.append(enlace)

    def getEnlaces(self):
        return self.enlaces

    def cantAtomos(self):
        return list(map(lambda elementoConAtomo: elementoConAtomo.cantAtomos(), self.elementosConAtomo))

    def atomosDe(self, elemento):
        return self.findelemento(elemento).cantAtomos()

    def incluyeAtomo(atomo):
        return any(list(map(lambda elementoConAtomo: atomo in elementoConAtomo)))

    def incluyeElemento(elemento):
        return any(list(map(lambda elementoConAtomo: elemento in elementoConAtomo )))

    def elementosPresentes(self):
        return list(map(lambda elemento: elemento.getelemento()))

    def cantEnlaces(self):
        return list(map(lambda enlaces: enlaces.cantEnlaces(), self.enlaces))

    def cantEnlacesAtomo(self,atomo):
        return self.findenlaceatomo(atomo).cantEnlaces()

    def findenlaceatomo(self, enlacebuscar):
        return next((enlace for enlace in self.enlaces if enlace.getEnlace == enlacebuscar))



    """" Comento este bloque porque masaElemento y masaCompuesto no las logre definir
    
    def proporcionElementoSobreMasa(elemento):
      prop = self.masaElemento/self.masaCompuesto 

        
    """


class CompuestoAux:
    def __init__(self,compuesto,moles):
        self.compuesto=compuesto
        self.moles=moles

    def getmoles(self):
        return self.moles

    def getcompuesto(self):
        return self.compuesto

    def aniadirmoles(self, cantidadMoles):
        self.moles = self.moles+ cantidadMoles



class ElementoConAtomo: # esta clase esta OK
    def __init__(self, elemento):
        self.elemento=elemento
        self.listaAtomo=[]


    def getelemento(self):
        return self.elemento

    def agregarAtomo(self,atomo):
        self.listaAtomo.append(atomo)

    def getAtomo(self):
        return self.listaAtomo

    def cantAtomos(self):
        return len(self.listaAtomo)

class Enlace:
    def __init__(self,atomo1, atomo2):
        self.atomo1=atomo1
        self.atomo2=atomo2

    def getEnlace(self):
        return self.atomo1+self.atomo2



class Medio:
    def __init__(self):
        self.listacompuestos=[]

    def agregarComponente(self,compuesto, cantMoles):
        if self.findcompuesto(compuesto) is None:
            self.listacompuestos.append(CompuestoAux(compuesto,cantMoles))
        else:
           self.findcompuesto(compuesto).aniadirmoles(cantMoles)

    def findcompuesto(self,compuesto):
         return next ((compuesto for compuesto in self.listacompuestos if compuesto.getcompuesto == compuesto))

    def masaTotal(self): #creo que la suma de las masas molares es la masa total
        return self.sumaMasa(lambda compuesto: compuesto.masaMolar())


    def masaDeCompuesto(self, compuesto):
        return self.sumaMasa(lambda compuesto: compuesto.masaCompuesto(compuesto))

    def masaDeElemento(self,elemento):
        return self.sumaMasa(lambda compuesto: compuesto.masaElemento(elemento))

    def sumaMasa(self,unaLambda):
        return list(sum(list(map(unaLambda, self.listacompuestos))))

    def getlistacompuesto(self):
        return self.listacompuestos

""" No pude resolverlas :(

    def masaMolar(self):
        return sum(list(map((lambda compuestoAux: compuestoAux.getcompuesto().getelemento().masaMolar() * compuestoAux.getmoles()), self.listacompuestos))) # se que me esta devolviendo una lista no un elemento

    def masaCompuesto(self,elemento):
        return self. *self.moles


    def masaElemento(self):
        return 1  # como si fuese un mock
                  # se que es el mismo procedimiento que en masaMolar, pero lo que logré que me retorne no es lo que necesito.
"""

class DescripcionMedio:
    def __init__(self, listadecompuestos):
        medio = Medio(listadecompuestos)

    def apareceCompuesto(self, comp):
        return comp in self.medio.getlistacompuesto()

    #def molesCompuesto(self, comp):
     #   return medio.
    # no la pude resolver
    def quienesAparecen(self,listaDeCompuestos):
        return map(lambda comp: comp.getcompuesto(),self.medio.getlistacompuesto()) & listaDeCompuestos  #busco interseccion con listaDeCompuestos

    def agregarAMedio(self, medio, compuesto):
        medio.agregarComponente(compuesto, self.molesCompuesto(compuesto))




#estas variables las uso para los test

oxigeno = Elemento('O', 8, 8, 4)
hidrogeno = Elemento('H', 1, 1, 1)
carbono= Elemento('C',6, 7, 2)
nitrogeno= Elemento('N', 7, 6, 4)


tabla = TablaPeriodica()


agua= ['H2O']
metano= ['CH4']
nh3= ['NH3']
co2= ['CO2']
