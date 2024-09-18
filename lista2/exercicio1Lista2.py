#exercicio 1 - sistema de gerenciamento de hotel
from datetime import date
from datetime import datetime

class Hospede:
    def __init__(
            self,
            nome:str,
            cpf: str,
            data_de_nascimento: date,):
        
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento


    def idade_hospede(self): # criar um método é basicamente uma função que se associa à uma classe
        nasc_hospede = datetime.strptime(self.data_de_nascimento, '%d/%m/%Y')
        dia_hoje = datetime.today()
        idade_hospede = dia_hoje - nasc_hospede
        
        if (dia_hoje.month, dia_hoje.day) < (nasc_hospede.month, nasc_hospede.day): # essa parte do código serve para verificar se o hóspede ja fez aniversório no ano atual
            idade_hospede -=1

        return idade_hospede


class Reserva:
    def __init__(
            self,
            hospede: Hospede,
            n_quarto: int,
            valor_diaria: float,
            duracao_estadia: int
        ):

        self.hospede = hospede
        self.n_quarto = n_quarto
        self.valor_diaria = valor_diaria
        self.duracao_estadia = duracao_estadia
        

    def calcular_valor_estadia(self):
        return self.valor_diaria * self.duracao_estadia # não esquecer de usar o "self." antes de chamar a variável
    

    def exibir_detalhes_reserva(self):
        return{
            "nome_hospede": self.hospede.nome,
            "numero_do_quarto": self.n_quarto,
            "duracao_estadia": self.duracao_estadia
        }


#criando as instâncias da reserva

hospede1 = Hospede("Guilherme Viana", "123456789", "22/12/2004")
reserva1 = Reserva(hospede1, 4, 198.50, 5)

#nessa parte, chamamos os métodos para exibir os valores baseados na instância "hóspede 1"
detalhes = reserva1.exibir_detalhes_reserva()
custo_total = reserva1.calcular_valor_estadia()
idade_hospede1 = hospede1.idade_hospede()


print(f"Exibindo detalhes: {detalhes}")
print(f"exibindo custo total: {custo_total}")
print(f"Exibindo a idade do hospede: {idade_hospede1}")