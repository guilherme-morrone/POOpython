class Empregado: 
    def __init__(
            self,
            primeiro_nome: str,
            segundo_nome: str,
            salario_mensal: float
        ):

        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        self.salario_mensal = salario_mensal if salario_mensal > 0 else 0.0

    def calcular_salario_anual(self):
        return self.salario_mensal * 12
    
    
    def conceder_aumento_salarial(self):
        return self.salario_mensal * 1.2 # 100% = * 1 mais 20% = *0.2 
    

colaborador1 = Empregado("Guilherme", "Morrone", 1500.00)
colaborador2 = Empregado("Clovis", "Morrone", -5000.00)

colaborador1_salario_anual = colaborador1.calcular_salario_anual()
colaborador2_salario_anual = colaborador2.calcular_salario_anual()

colaborador1_novo_salario = colaborador1.conceder_aumento_salarial()
colaborador2_novo_salario = colaborador2.conceder_aumento_salarial()


print(f"O funcionario {colaborador1.primeiro_nome} {colaborador1.segundo_nome} possui um salario mensal de R${colaborador1.salario_mensal}, portando, recebe R${colaborador1_salario_anual} por ano. Agora passara a receber R${colaborador1_novo_salario} por mes")
print(f"O funcionario {colaborador2.primeiro_nome} {colaborador2.segundo_nome} possui um salario mensal de R${colaborador2.salario_mensal}, portando, recebe R${colaborador2_salario_anual} por ano. Agora passara a receber R${colaborador2_novo_salario} por mes")