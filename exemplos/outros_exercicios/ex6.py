class Funcionario:
    def __init__(
            self,
            nome:str,
            salario: float
            ):
            self.nome = nome
            self._salario = salario

    
    def calcular_salario(self):
        return self._salario * 12
    

    def exibir_informacoes(
            self,
            genero: str,
            ):
        if genero == "m":
            return f"""O Sr. {self.nome} recebe um salario anual de {self.calcular_salario()}"""
        else:
            return f"""O Sra. {self.nome} recebe um salario anual de {self.calcular_salario()}"""
        
  

funcionario = Funcionario("Guilherme", 970.90)
print(funcionario.calcular_salario())
print(funcionario.exibir_informacoes("m"))  

funcionaria = Funcionario("Leticia", 1450.90)
print(funcionaria.exibir_informacoes("f"))