#desenhar o modelo de classes de um paralelepípedo
class Paralelepipedo:
    def __init__(
            self,
            alt: int,
            larg: int,
            compr:int             
        ):

        self.altura = alt
        self.largura = larg
        self.comprimento = compr

    def calculo_volume(self) -> int:
        return self.comprimento * self.altura * self.largura
        
    def calculo_area(self) -> int:
        return 2 * ((self.altura * self.largura) + (self.altura * self.comprimento) + (self.largura * self.comprimento))


compr = int(input("Por favor, digite o comprimento do paralelepíppedo: "))
alt = int(input("Por favor, digie a altura do paralelepípedo: "))
larg = int(input("Por favor, digite a largura do paralelepípedo: "))
prllpd = Paralelepipedo(alt, larg, compr)

print(f"O volume do paralelepípedo é {prllpd.calculo_volume()}")
print(f"A areá do paralelepípedo é: {prllpd.calculo_area()}")