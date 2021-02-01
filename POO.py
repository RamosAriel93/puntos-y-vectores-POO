import math


class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print(f"{self} pertenece al primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print(f"{self} pertenece al segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print(f"{self} pertenece al tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print(f"{self} pertenece al cuarto cuadrante")
        elif self.x != 0 and self.y == 0:
            print(f"{self} esta sobre el eje x ")
        elif self.x == 0 and self.y != 0:
            print(f"{self} esta sobre el eje y")
        else:
            print(f"{self} esta sobre el origen de coordenadas.")

    def vector(self, p):
        print(f"el vector que une los puntos {self} y {p} es igual a ({p.x - self.x}, {p.y - self.y})")

    def distancia(self, p):
        mod = math.sqrt(abs((p.x - self.x)**2 - (p.y - self.y)**2))
        print(f"La distancia entre los puntos {self} y {p} es {mod}")


a = Punto(5, 8)
b = Punto(10, -2)
c = Punto(-4, 6)

# Ubicacion del cuadrante
a.cuadrante()
b.cuadrante()
c.cuadrante()

# Vector entre puntos
a.vector(b)
b.vector(c)
c.vector(a)

# Valor de la distancia entre los puntos
a.distancia(b)
b.distancia(c)
c.distancia(a)


