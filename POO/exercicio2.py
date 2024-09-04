#desenhar o modelo de classes de um retângulo e de um círculo
import math

class FormaGeometrica:
    def area(self):
        pass
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(
            self,
            altura: int,
            largura: int,
        ):
            self.altura = altura
            self.largura = largura

    def area(self):
         return self.altura * self.largura
    
    def perimetro(self):
         return 2 * (self.altura + self.largura)

class Circulo(FormaGeometrica):
    def __init__(
            self,
            raio: int
        ):
            self.raio = raio

    def area(self):
         return math.pi * (self.raio ** 2)

    def perimetro(self):
         return 2 * math.pi * self.raio


altura = int(input("Digite a altura do retangulo: "))             
largura = int(input("Digite a largura do retangulo: "))
retangulo = Retangulo(altura, largura)

print(f"A area do retangulo é: {retangulo.area()}\n e o perimetro do retangulo é: {retangulo.perimetro()}")
             

raio = int(input("Digite o valor do raio do círculo: "))
circulo = Circulo(raio)

print(f"A área do círculo é> {circulo.area()}\n e o perimetro do círculo é: {circulo.perimetro()}")



