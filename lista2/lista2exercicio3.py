from datetime import date

class Projeto:
    def __init__(
        self,
        nome_projeto: str,
        data_inicio: date,
    ):
        self.nome = nome_projeto
        self.data_inicio = data_inicio
        self.membros_envolvidos = []  # Inicializando como uma lista vazia

    #agora devem ser criados os métodos para a classe 'Projeto'
    def exibir_detalhes(self):
        detalhes = f"""
        Nome do Projeto: {self.nome}
        Data de Início do Projeto: {self.data_inicio}
        Membros Envolvidos: 
        """
        if not self.membros_envolvidos:
            detalhes += "\nNenhum membro foi adicionado ao projeto."
        else:
            for membro in self.membros_envolvidos:
                detalhes += f"\n{membro.nome} ({membro.email})"
        return detalhes

    def incluir_membros(self, membro):
        self.membros_envolvidos.append(membro)

    def calcular_duracao_projeto(self, data_termino_projeto):
        duracao = (data_termino_projeto - self.data_inicio).days  # Cálculo em dias
        return duracao  # Retorna a duração em dias


class Membros:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email


# criando as instâncias 

projeto1 = Projeto("Sistema de Delegacia", date(2024, 5, 3))

aluno1 = Membros("Guilherme", "guilherme@guilherme.com")
aluno2 = Membros("Diego Artero", "diego@diego.com")
aluno3 = Membros("Jean Lucas", "jean@jean.com")

projeto1.incluir_membros(aluno1)
projeto1.incluir_membros(aluno2)
projeto1.incluir_membros(aluno3)

print(projeto1.exibir_detalhes())  # Chame a função

data_termino_projeto = date(2025, 9, 1)
print(f"Duracao  do projeto: {projeto1.calcular_duracao_projeto(data_termino_projeto)} dias")
