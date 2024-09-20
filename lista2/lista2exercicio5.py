from datetime import date

class MetodoDePagamento:
    def processar_pagamento(self, valor: float):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

# Pagamento via Pix
class PagarComPix(MetodoDePagamento):
    def __init__(self, titular_da_conta: str, chave_pix: str, saldo: float):
        self.titular_da_conta = titular_da_conta
        self.chave_pix = chave_pix
        self.saldo = saldo

    def processar_pagamento(self, valor: float):
        print(f"""Iniciando processo de pagamento no valor de R${valor:.2f} via Pix...\n
        Titular da Conta: {self.titular_da_conta} \n
        Chave Pix: {self.chave_pix}\n
        """)
        if self.saldo >= valor:
            self.saldo -= valor  # desconta o valor do saldo
            resultado = "Pagamento Aprovado"
        else:
            resultado = "Pagamento não aprovado. Saldo Insuficiente."

        return resultado

# Pagamento via Cartão de Débito
class PagarComCartaoDebito(MetodoDePagamento):
    def __init__(self, titular_da_conta: str, numero_do_cartao: int, validade: date, saldo: float):
        self.titular_da_conta = titular_da_conta
        self.numero_do_cartao = numero_do_cartao
        self.validade = validade
        self.saldo = saldo

    def processar_pagamento(self, valor: float):
        print(f"""Iniciando processo de pagamento no valor de R${valor:.2f} via Cartão de Débito...\n
        Titular da Conta: {self.titular_da_conta}\n
        Cartão Número: {self.numero_do_cartao}\n
        """)
        if self.saldo >= valor and date.today() <= self.validade:  # Corrigido: validade do cartão
            self.saldo -= valor  # desconta o valor do saldo
            resultado = "Pagamento Aprovado"
        else:
            resultado = "Pagamento não aprovado. Saldo Insuficiente ou Cartão Expirado."

        return resultado

# Pagamento via Cartão de Crédito
class PagarComCartaoCredito(MetodoDePagamento):
    def __init__(self, titular_da_conta: str, numero_do_cartao: int, limite: float):
        self.titular_da_conta = titular_da_conta
        self.numero_do_cartao = numero_do_cartao
        self.limite = limite

    def processar_pagamento(self, valor: float):
        print(f"""Iniciando processo de pagamento no valor de R${valor:.2f} via Cartão de Crédito...\n
        Titular da Conta: {self.titular_da_conta}\n
        Cartão Número: {self.numero_do_cartao}\n
        """)
        if self.limite >= valor:
            self.limite -= valor  # desconta do limite
            resultado = "Pagamento Aprovado"
        else:
            resultado = "Pagamento não aprovado. Limite Insuficiente."

        return resultado


# Classe Cliente
class Cliente:
    def __init__(self, nome: str):
        self.nome = nome

# Classe Produto
class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco


# Exemplo de uso do sistema de pagamento
cliente1 = Cliente("João")

doce = Produto("Brigadeiro", 5.50)

# Cliente paga com Pix
pagamento_pix = PagarComPix("João", "joao@pix.com", 50.00)
print(pagamento_pix.processar_pagamento(doce.preco))

# Cliente paga com Cartão de Débito
pagamento_debito = PagarComCartaoDebito("João", 1234567890123456, date(2025, 12, 31), 100.00)
print(pagamento_debito.processar_pagamento(doce.preco))

# Cliente paga com Cartão de Crédito
pagamento_credito = PagarComCartaoCredito("João", 1234567890123456, 500.00)
print(pagamento_credito.processar_pagamento(doce.preco))
