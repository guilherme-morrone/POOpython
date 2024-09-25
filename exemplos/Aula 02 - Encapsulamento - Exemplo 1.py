class ContaCorrente:  # Uma classe "pura", ou seja, não possui nenhuma herança.
    # `__init__` é o construtor do Python, isto significa que quando uma
    # instância for criada é este método que será chamado.
    def __init__(self, saldo: float):  # O construtor possui um argumento chamado `saldo` e seu tipo é `float`.
        # Usamos o `self` para fazer referência à classe ContaCorrente e criar o ATRIBUTO `_saldo`,
        # o qual receberá `saldo` como valor.
        self._saldo = saldo

    # O método possui um argumento chamado `valor` e seu tipo é float. Na instância, ele deverá ser o valor a ser sacado.
    def sacar(self, valor: float):
        # A implementação de sacar deve garantir que toda a regra de negócio esteja encapsulada.
        if self._saldo >= valor:
            # Dentro deste bloco if é verificado se há `self._saldo` disponível comparado ao `valor` que se deseja
            # sacar. Havendo saldo, subtrai-se `valor` de `self._saldo`.
            self._saldo -= valor
            print(f"Saque de {valor} realizado. Saldo restante: {self._saldo:.2f}")
        else:
            print("Saldo indisponível")

    def exibir_saldo(self):
        print(f"O saldo da conta corrente é de R$ {self._saldo:.2f}")


# Cria uma instância de ContaCorrente chamada `conta_corrente1` com o saldo de R$ 1.000,00.
conta_corrente1 = ContaCorrente(10000)
# Saca-se R$ 500,00 da conta corrente.
conta_corrente1.sacar(500)
# Com a execução da linha anterior, `_saldo` de `conta_corrente1` será 500, logo não será possível sacar a quantia de R$ 750,23.
conta_corrente1.sacar(750.23)

# Cria uma segunda instância de ContaCorrente chamada `conta_corrente2` com o saldo de R$ 140.
# Observem que o argumento `saldo` está explícito aqui.
conta_corrente2 = ContaCorrente(saldo=140)
# Saca-se R$ 100 da conta corrente.
conta_corrente2.sacar(100)
# Quanto resta de saldo nessa conta corrente?
conta_corrente2.exibir_saldo()
