class Imovel:
    def __init__(
            self,
            endereco:str,
            preco_base: float
        ):

        self.endereco = endereco
        self.preco_base = preco_base

    def apresentar_preco_base(self):
        return self.preco_base
    
    def apresentar_preco_final(self):
        pass


class Novo(Imovel):
    def __init__(self, endereco, preco_base, adicional: float):
        self.endereco = endereco
        self.preco_base = preco_base
        self.adicional = adicional

    def apresentar_preco_base(self):
        return self.preco_base
    
    def apresentar_preco_final(self):
        return self.preco_base + self.adicional
        
        
        
class Usado(Imovel):
    def __init__(self, endereco, preco_base, desconto: float):
        self.endereco = endereco
        self.preco_base = preco_base
        self.desconto = desconto

    def apresentar_preco_base(self):
        return self.preco_base
    
    def apresentar_preco_final(self):
        return self.preco_base + self.desconto
        

imovel_novo = Novo("Rua A, 123", 300000.00, 50000.00)
print(f"Imóvel Novo - Endereço: {imovel_novo.endereco}, Preço Base: R${imovel_novo.preco_base:.2f}, Preço Final: R${imovel_novo.apresentar_preco_final():.2f}")

imovel_usado = Usado("Rua B, 456", 250000.00, 30000.00)
print(f"Imóvel Novo - Endereço: {imovel_usado.endereco}, Preço Base: R${imovel_usado.preco_base:.2f}, Preço Final: R${imovel_usado.apresentar_preco_final():.2f}")