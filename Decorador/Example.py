from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        resultado = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        resultado.unir(self)
        resultado.unir(otro_conjunto)
        return resultado

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_interseccion = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
        nombre_resultado = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        resultado = Conjunto(nombre_resultado)
        resultado.elementos = elementos_interseccion
        return resultado

    def __str__(self):
        elementos_str = ', '.join([elemento.nombre for elemento in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"
#############################################
#############################################

elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")

conjunto1 = Conjunto("Set1")
conjunto2 = Conjunto("Set2")

conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

resultado_union = conjunto1 + conjunto2
resultado_interseccion = Conjunto.intersectar(conjunto1, conjunto2)

print(conjunto1)
print(conjunto2)
print(resultado_union)
print(resultado_interseccion)
