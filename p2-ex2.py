class Pessoa:
    def __init__(self, nome: str, idade: int, pai=None, mae=None):
        self.nome = nome
        self.idade = idade
        self.pai = pai  
        self.mae = mae  

    def exibir_detalhes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        print(f"Pai: {self.pai.nome if self.pai else 'Desconhecido'}")
        print(f"Mãe: {self.mae.nome if self.mae else 'Desconhecido'}")

# Criando instâncias de Pessoa
pai = Pessoa("Carlos", 60)
mae = Pessoa("Ana", 58)
filho = Pessoa("João", 30, pai=pai, mae=mae)

# Exibir os detalhes da pessoa e seus pais
filho.exibir_detalhes()
