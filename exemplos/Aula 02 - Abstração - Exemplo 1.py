from abc import ABC, abstractmethod  # Importa do pacote abc os objetos ABC e abstractmethod.


class ContaBancaria(ABC):  # Declaração da classe herdando de ABC.
    @abstractmethod  # Decorator abstractmethod, indicando que o comportamento do método exibir_saldo é abstrato.
    def exibir_saldo(self):  # `self` faz referência à própria classe, ela indica que o método pertence à classe.
        pass  # O pass é uma palavra especial do Python e indica que existirá um código futuro ali, nada é executado.

    @abstractmethod
    def sacar(self, valor: float):  # O método sacar, também abstrato, possui um argumento do tipo float chamado `valor`.
        pass


class ContaCorrente(ContaBancaria):  # ContaCorrente herda da classe ContaBancaria.
    def exibir_saldo(self):
        print("mostrar o saldo da conta corrente")  # Implementação do método exibir_saldo.

    def sacar(self, valor: float):
        print(f"R$ {valor:.2f} serão sacados da conta corrente")  # Implementação do método sacar.


# Retire o # da linha abaixo para testar o erro de instanciação de classe abstrata.
# conta_bancaria = ContaBancaria()

# Instanciação do objeto `conta_corrente`. Seu valor é um objeto do tipo `ContaCorrente`.
conta_corrente = ContaCorrente()

# Sendo `conta_corrente` uma instância, é possível usar os métodos da classe a qual ela representa usando ".".
conta_corrente.exibir_saldo()
# É esperado que uma mensagem seja printada na tela.
