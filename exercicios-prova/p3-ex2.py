class Conta:
    def __init__(
            self, 
            valor_a_ser_pago: float,
            qnt_de_pessoas: int,
            taxa_de_servico: bool
        ):
            self.valor_a_ser_pago = valor_a_ser_pago
            self.qnt_de_pessoas = qnt_de_pessoas
            self.taxa_de_servico = taxa_de_servico

    def calcular_conta(self):
        if self.taxa_de_servico == True:
             valor_final = (self.valor_a_ser_pago * 1.1) / self.qnt_de_pessoas
        else:
            valor_final = self.valor_a_ser_pago / self.qnt_de_pessoas
        
        return valor_final
    

conta1 = Conta(100.00, 4, True)
conta2 = Conta(250, 7, True) 


print(f"O valor que cada um tera que pagar e: {conta1.calcular_conta():.2f}")
print(f"O valor que cada um tera que pagar e: {conta2.calcular_conta():.2f}")
