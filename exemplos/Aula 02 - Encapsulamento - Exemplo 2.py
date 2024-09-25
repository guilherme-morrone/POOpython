class ContaCorrenteSemRegraEncapsulada:
    def __init__(self, saldo: float):
        self._saldo = saldo

    def sacar(self, valor: float):
        # Ao sacar o dinheiro da conta corrente, a validação do saldo disponível e do débito em si
        # fica sob responsabilidade do próprio método sacar. Com isso, esse método tem 3 responsabilidades:
        # 1) verificar disponibilidade de saldo;
        # 2) fazer o débito, se houver saldo disponível; e
        # 3) exibir a mensagem de sucesso ou falha do saque.
        if self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de {valor} realizado. Saldo restante: {self._saldo:.2f}")
        else:
            print("Saldo indisponível")

    def transferir(self, valor: float, cpf: str):  # Aqui temos um segundo argumento, o `cpf` é do tipo str.
        # Mesma situação do método sacar. O método possui 3 responsabilidades.
        if self._saldo >= valor:
            self._saldo -= valor
            print(f"Transferência de {valor} realizado para o CPF {cpf}. Saldo restante: {self._saldo:.2f}")
        else:
            print("Saldo indisponível")

    def exibir_saldo(self):
        print(f"O saldo da conta corrente é de R$ {self._saldo:.2f}")


class ContaCorrenteComRegraEncapsulada:
    def __init__(self, saldo: float):
        self._saldo = saldo

    # O método `verificar_saldo` recebe `valor` como argumento e tem como retorno (->) um valor booleano.
    def verificar_saldo(self, valor: float) -> bool:
        # O return é uma palavra especial que indica que o método/função deverá retornar
        # o que estiver à sua direita para aquele que o chamou.
        # Com SOMENTE o uso do return NENHUM valor será exibido em tela (print).
        return self._saldo >= valor  # A expressão devolverá um valor booleano (True ou False) devido o operador `>=`.

    # O método `debitar_saldo` subtrairá o `valor` de `self._saldo`. Essa é a sua única responsabilidade.
    def debitar_saldo(self, valor: float):
        self._saldo -= valor

    def sacar(self, valor: float):
        if self.verificar_saldo(valor):  # Se o resultado retornado pelo método `verificar_saldo` for verdadeiro...
            self.debitar_saldo(valor)  # ... Debite `valor` do saldo da conta corrente.
            print(f"Saque de {valor} realizado. Saldo restante: {self._saldo:.2f}")
        else:
            print("Saldo indisponível")

    def transferir(self, valor: float, cpf: str):
        # Mesma situação do método `sacar`, porém na situação de transferência de dinheiro.
        # É necessário verificar o saldo e, havendo disponibilidade, fazer o débito e confirmar a transferência.
        # As duas primeiras ações são de responsabilidade de outros métodos (`verificar_saldo` e `debitar_saldo`, respectivamente),
        # enquanto nesse método existe somente a regra de negócio da transferência
        # reutilizando a regra de negócio da verificação e débito.
        if self.verificar_saldo(valor):
            self.debitar_saldo(valor)
            print(f"Transferência de {valor} realizado para o CPF {cpf}. Saldo restante: {self._saldo:.2f}")
        else:
            print("Saldo indisponível")


# Teste a execução abaixo e observe o comportamento.
conta_sem_regra_encapsulada = ContaCorrenteSemRegraEncapsulada(saldo=100)
conta_sem_regra_encapsulada.sacar(50)
conta_sem_regra_encapsulada.transferir(50, "12345678901")

conta_com_regra_encapsulada = ContaCorrenteComRegraEncapsulada(saldo=100)
conta_com_regra_encapsulada.sacar(50)
conta_com_regra_encapsulada.transferir(50, "12345678901")
