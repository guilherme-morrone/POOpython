class Funcionario:
    # O construtor da classe receberá 4 argumentos: nome, CPF, idade e salário.
    def __init__(self, nome: str, cpf: str, idade: int, salario: float):
        # `self.nome` e `self.cpf` são atributos públicos (public).
        self.nome = nome
        self.cpf = cpf
        # `self._idade` é um atributo protegido (protected).
        self._idade = idade
        # `self.__salario` é um atributo privado (private).
        self.__salario = salario

    # `exibir_dados` é um método público, todos podem acessá-lo.
    def exibir_dados(self):
        # Aquele que desejar saber o salário de um funcionário, não conseguirá acessar
        # pelo atributo `self.__salario`. Ele deverá chamar este método para que
        # o salário seja apresentado.
        print(f"O nome do funcionário é {self.nome}, CPF {self.cpf}, tem {self._idade} ano(s) e recebe R$ {self.__salario}.")

    # `_verificar_maioridade_idade` é um método protegido.
    def _verificar_maioridade_idade(self):
        # Independente do seu modificador de acesso, a classe (self) sempre terá acesso
        # a todos os seus objetos, sejam eles atributos ou métodos. Por isso, `self._idade`
        # é acessível dentro deste método.
        if self._idade >= 18:
            print("O funcionário é maior de idade, pode trabalhar.")
        else:
            print("Menor de idade, analisar contrato junto aos responsáveis.")

    # `__atualizar_salario` é um método privado, ou seja, somente a classe `Funcionario` tem acesso.
    def __atualizar_salario(self, valor_aumento: float):
        self.__salario += valor_aumento

    # `promover` é um método público que consegue acessar seu próprio (self) método privado `__atualizar_salario`.
    def promover(self):
        aumento = self.__salario * 0.1  # Aumento de 10%.
        self.__atualizar_salario(aumento)


# `Gerente` é uma subclasse de `Funcionario`.
# Esta classe terá acesso aos seguintes atributos e métodos:
# Atributos: nome, cpf, _idade
# Métodos: exibir_dados, promover, _verificar_maioridade_idade
class Gerente(Funcionario):
    def gerenciar_acao(self):
        print("Os dados serão mostrados novamente:")
        print(self.nome)  # O nome do funcionário seja exibido. Usa um modificador público.
        print(self._idade)  # A idade será exibida. Usa um modificador protegido, por isso essa classe consegue acessar.
        self.exibir_dados()
        self._verificar_maioridade_idade()
        # A chamada abaixo dará um erro, pois `__atualizar_salario` é privado e não pode ser acessado
        # por ninguém além de `Funcionario`.
        self.__atualizar_salario()


micalateia = Funcionario("Micalatéia", "00011122233", 30, 5000)
print(micalateia.nome)
print(micalateia.cpf)
micalateia.exibir_dados()
micalateia.promover()
micalateia.exibir_dados()
# Retire o # da linha abaixo para ver o comportamento de erro.
# micalateia.__atualizar_salario()

chirlei = Gerente("Chirlei", "11122233344", 48, 12000)
print(chirlei.nome)
print(chirlei.cpf)
chirlei.exibir_dados()
chirlei.promover()
chirlei.exibir_dados()
chirlei.gerenciar_acao()
