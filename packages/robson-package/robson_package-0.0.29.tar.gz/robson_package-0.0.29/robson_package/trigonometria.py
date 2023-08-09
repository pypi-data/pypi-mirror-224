class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_perimetro(self):
        return self.a + self.b + self.c
    
    def calcular_area(self):
        p = self.calcular_perimetro() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        

if __name__ == "__main__":
    a = float(input("Digite o valor do lado a: "))
    b = float(input("Digite o valor do lado b: "))
    c = float(input("Digite o valor do lado c: "))
    triangulo = Triangulo(a, b, c)
    print(f"O perímetro do triângulo é {triangulo.calcular_perimetro()}")
    print(f"A área do triângulo é {triangulo.calcular_area()}")