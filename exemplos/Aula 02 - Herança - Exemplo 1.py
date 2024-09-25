"""Considere que toda conta bancária deve ter um titular e um saldo, além de permitir depósito.
Por sua vez, a conta corrente, que É UMA conta bancária, permite receber Pix e por
convenção do Banco Central ela deve possibilitar a exibição do titular e do saldo.
"""


class ContaBancaria:  # Não existe herança aqui, tampouco abstração.
    def __init__(self, titular: str, saldo: float):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor: float):
        self._saldo += valor  # Soma-se em `self._saldo` o `valor` a ser depositado.
        print(f"O valor de R$ {valor:.2f} foi depositado. Seu saldo atual: R$ {self._saldo:.2f}")


class ContaCorrente(ContaBancaria):  # ContaCorrente herda todos os atributos e métodos de ContaBancaria.
    def receber_pix(self, valor: float):
        # Reuso do método `deposito`, considerando que um recebimento de Pix é considerado um depósito em conta corrente.
        self.depositar(valor)

    def exibir_titular(self):  # Esse método existe somente em ContaCorrente, não foi herdado de ContaBancaria.
        print(f"O titular da conta corrente é {self._titular}")

    def exibir_saldo(self):  # Esse método existe somente em ContaCorrente, não foi herdado de ContaBancaria.
        print(f"Seu saldo atual é de R$ {self._saldo:.2f}")


# Vamos criar uma conta corrente.

# O titular João da Silva possui uma conta corrente com saldo de R$ 1.000,00.
# Essas informações estão armazenadas na instância `conta_corrente`.
conta_corrente = ContaCorrente(titular="João da Silva", saldo=1000)
conta_corrente.exibir_titular()
conta_corrente.exibir_saldo()  # O saldo é de R$ 1.000,00.
conta_corrente.receber_pix(100)  # Método direto da ContaCorrente.
conta_corrente.depositar(400)  # É possível usar o método `deposito` de ContaBancaria, uma vez que ContaCorrente é uma (herda de) ContaBancaria.
conta_corrente.exibir_saldo()  # O saldo é de R$ 1.500,00.

# Também é possível instanciar somente uma ContaBancaria, uma vez que ela não é abstrata.
conta_bancaria = ContaBancaria("Maria Sousa", 650120)
conta_bancaria.depositar(9880)
conta_bancaria.exibir_saldo()  # Esse método não existe em ContaBancaria, então uma exceção será lançada.
