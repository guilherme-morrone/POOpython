class Pessoa:
    def __init__(
            self,
            nome: str,
            idade: str
        ):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("Olá, eu sou uma pessoa") 


class Aluno(Pessoa):
    def estudar(self):
        print("Olá, eu sou um estudante e estou estudando")
   


aluno1 = Aluno("Guilherme", 19)
print(aluno1.nome)
print(aluno1.idade)
aluno1.falar()
aluno1.estudar()   