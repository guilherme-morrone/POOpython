from datetime import date

class Tarefa:
    def __init__(self, descricao: str, data_criacao: date):
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.concluida = False  # A tarefa começa como não concluída
        self.data_conclusao = None  # Inicialmente, não há data de conclusão

    def concluir(self):
        """Conclui a tarefa e registra a data de conclusão."""
        self.concluida = True
        self.data_conclusao = date.today()

    def exibir_detalhes(self):
        """Exibe os detalhes da tarefa."""
        status = "Tarefa Concluída" if self.concluida else "Tarefa Pendente"
        detalhes = f"""
        Descrição da Tarefa: {self.descricao}
        Data de Criação: {self.data_criacao}
        Status da Tarefa: {status}
        """  # O status é uma variável local, não precisa de self.

        if self.concluida:
            detalhes += f"Data da Conclusão: {self.data_conclusao}"

        return detalhes

    def esta_atrasada(self, prazo: date):
        """Verifica se a tarefa está atrasada em relação ao prazo."""
        return date.today() > prazo

# Criando uma tarefa
tarefa1 = Tarefa("Finalizar relatório", date(2024, 9, 1))

# Exibindo os detalhes da tarefa
print(tarefa1.exibir_detalhes())

# Concluindo a tarefa
tarefa1.concluir()

# Exibindo os detalhes após a conclusão
print(tarefa1.exibir_detalhes())

# Verificando se a tarefa está atrasada
prazo_limite = date(2024, 9, 5)
print(f"Tarefa está atrasada? {'Sim' if tarefa1.esta_atrasada(prazo_limite) else 'Não'}")
