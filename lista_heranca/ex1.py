class Ingresso:
    def __init__(self, valor: float):
        self.valor = valor

    def retornar_valor_ingresso(self):
        return self.valor


class VIP(Ingresso):
    def __init__(self, valor):
        self.valor = valor  

    def retornar_valor_ingresso(self):
        return self.valor * 1.075 


class Normal(Ingresso):
    def __init__(self, valor):
        self.valor = valor 

    def retornar_valor_ingresso(self):
        return self.valor  


class CamaroteInferior(VIP):
    def __init__(self, valor, localizacao: str):
        self.valor = valor  
        self.localizacao = localizacao 

    def retornar_localizacao(self):
        return self.localizacao  


class CamaroteSuperior(VIP):
    def __init__(self, valor):
        self.valor = valor  

    def retornar_valor_ingresso(self):
        return self.valor * 1.075 * 1.025  


ingresso_normal = Normal(100.00)
print(f"Valor do ingresso normal: R${ingresso_normal.retornar_valor_ingresso():.2f}")


ingresso_vip = VIP(100.00)
print(f"Valor do ingresso VIP: R${ingresso_vip.retornar_valor_ingresso():.2f}")

camarote_inferior = CamaroteInferior(100.00, "Frente ao palco")
print(f"Valor do ingresso Camarote Inferior: R${camarote_inferior.retornar_valor_ingresso():.2f}")
