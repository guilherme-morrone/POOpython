class Carro:
    def __init__(self,
        modelo:str,
        ano: int,
        preco: float):

        self.modelo = modelo # público
        self._ano = ano # protegido 
        self.__preco = preco # privado


    def exibir_informacoes(self):
        return f"""Carro: {self.modelo}, Ano: {self._ano}, Preço {self.__preco}"""
    


carro1 = Carro("Corsa", 2006, 19.9999)
print(carro1.exibir_informacoes())