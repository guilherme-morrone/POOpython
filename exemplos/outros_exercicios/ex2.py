from abc import ABC, abstractmethod

class AparelhoEletronico(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Computador(AparelhoEletronico):
    def iniciar(self):
        print("O computador esta iniciando")

    def desligar(self):
        print("O computador esta encerrando")



pc1 = Computador()
pc1.iniciar()
pc1.desligar()