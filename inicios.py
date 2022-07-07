# quiero explorar esta nueva herramienta

import numpy as np

def distance(p1, p2):
    """p1 and p2 are ndarray"""
    return np.linalg.norm(p1-p2)

class Triangulo:
    def __init__(self, vertices):
        self.vertices = vertices
    def __str__(self):
        return str(self.vertices)
    def extremosDeLados(self):
        A, B = self.vertices, self.vertices
        B = np.vstack((B[-1], B))[:-1]
        return A, B
    def longDeLados(self):
        A, B = self.extremosDeLados()
        longitudes = [distance(p1, p2) for p1, p2 in zip(A, B)]
        return np.array(longitudes)
    def perimetro(self):
        return self.longDeLados().sum()
    def esIsosceles(self):
        return len(set(self.longDeLados())) < 3
    def esEquilatero(self):
        return len(set(self.longDeLados())) == 1
    def esEscaleno(self):
        return len(set(self.longDeLados())) == 3
    def area(self):
        a, b, c = self.longDeLados()
        s = (a+b+c) / 2
        return np.sqrt(s*(s-a)*(s-b)*(s-c)) 
    def longDeLadosOrd(self):
        return np.sort(self.longDeLados())
    def sonCongruentes(self, otro):
        return (self.longDeLadosOrd() == otro.longDeLadosOrd()).all()
    def sonSemejantes(self, otro):
        return ((self.longDeLadosOrd() / otro.longDeLadosOrd()) == 1).all()

mis_v = np.array([[0,0], [1,0], [1,1]])
mi_t = Triangulo(mis_v)
print(mi_t)
print(mi_t.extremosDeLados())
print(mi_t.longDeLados())
print(mi_t.perimetro())
print(mi_t.esIsosceles())
print(mi_t.esEquilatero())
print(mi_t.esEscaleno())
print(mi_t.area())
print(mi_t.longDeLadosOrd())
print(mi_t.sonCongruentes(mi_t))
print(mi_t.sonSemejantes(mi_t))                     

