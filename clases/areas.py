import numpy as np

class Areas:
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.radio = 0
        self.resultado = 0

    def leerDatos(self, figura):
        """
        Pide los datos según la figura seleccionada.
        - Triángulo y Rectángulo: base y altura
        - Círculo: radio
        """
        if figura in ["triángulo", "rectángulo"]:
            while True:
                try:
                    self.base = float(input(f"Ingrese la base del {figura}: "))
                    break
                except Exception:
                    print("Número inválido")
            while True:
                try:
                    self.altura = float(input(f"Ingrese la altura del {figura}: "))
                    break
                except Exception:
                    print("Número inválido")
        elif figura == "círculo":
            while True:
                try:
                    self.radio = float(input("Ingrese el radio del círculo: "))
                    break
                except Exception:
                    print("Número inválido")

    def areaTriangulo(self):
        self.resultado = (self.base * self.altura) / 2
        return f"El área del triángulo es {self.resultado}"

    def areaRectangulo(self):
        self.resultado = self.base * self.altura
        return f"El área del rectángulo es {self.resultado}"

    def areaCirculo(self):
        self.resultado = np.pi * (self.radio ** 2)
        return f"El área del círculo es {self.resultado:.2f}"
