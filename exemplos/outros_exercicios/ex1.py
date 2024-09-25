from abc import ABC, abstractmethod

class Dispositivo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass    


class Celular(Dispositivo):
    def ligar(self):
        print("O celular está iniciando")

    def desligar(self):
        print("O celular está encerrando")


celular1 = Celular()  
celular1.ligar()     
celular1.desligar()   
