import math

class Avanzadas:
    def __init__(self):
        self.base = 0
        self.exponente = 0
        self.resultado = 0

    def leerNumeros(self):
        self.base = int(input("Ingrese la base: "))
        self.exponente = int(input("Ingrese el exponente: "))

    def elevarPotencia(self):
        self.resultado = self.base ** self.exponente
        print(f"{self.base} elevado a la {self.exponente} es: {self.resultado}")

    def raizCuadrada(self):
        numero = int(input("Ingrese el número para calcular la raíz cuadrada: "))
        resultado = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {resultado}")
