class Fatura:
    def __init__(
            self,
            numero_do_item: int,
            descricao: str,
            qnt_comprada: int,
            preco_unitario: float
        ):

        self.numero_do_item = numero_do_item
        self.descricao = descricao
        self.qnt_comprada = qnt_comprada if qnt_comprada > 0 else 0
        self.preco_unitario = preco_unitario if preco_unitario > 0 else 0.0


    def calcular_valor_total(self):
        return self.qnt_comprada * self.preco_unitario


compra1 = Fatura(1,"smart tv 55 polegadas", 2, 2500.00)
fatura1 = compra1.calcular_valor_total()

print(f"O valor final da compra do produto {compra1.descricao} e de R${fatura1:.2f}")
        