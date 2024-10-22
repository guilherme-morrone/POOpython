class Produto:
    def __init__(
            self,
            nome_produto: str,
            preco_unitario: float,
            qnt_comprada: int
        ):

        self.nome_produto = nome_produto
        self.preco_unitario = preco_unitario
        self.qnt_comprada = qnt_comprada

    def calcular_desconto(self):     
        if self.qnt_comprada < 10:
            desconto = 0.0
        elif self.qnt_comprada >= 11 and self.qnt_comprada <= 20:
            desconto = 0.10
        elif self.qnt_comprada >= 21 and self.qnt_comprada <= 50:
            desconto = 0.15   
        else:
            desconto = 0.20

        preco_final = self.preco_unitario * self.qnt_comprada * (1 - desconto)
        return preco_final
    

produtos = [
    Produto("Mouse", 90.00, 30),
    Produto("Teclado", 130.00, 55),
    Produto("Monitor", 1000.00, 3), 
    Produto("Headset", 200.00, 23),
    Produto("Computador", 3000.00, 300)
]


print(f" {'Preco unitario': <15} {'Preco unitario': <15} {'Quantidade': <15} {'Valor com desconto': <15}")
print("-" * 60)

for produto in produtos:
    valor_com_desconto = produto.calcular_desconto()

    print(f"{produto.nome_produto:<15} R${produto.preco_unitario:<14} {produto.qnt_comprada: <10} R${valor_com_desconto:.2f}")
