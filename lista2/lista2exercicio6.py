from abc import ABC, abstractmethod
from datetime import date,datetime

class Veiculo(ABC):
   
    def __init__(
            self    
        ):
        self.marca: str
        self.modelo: str
        self.chegada: datetime
      
    @abstractmethod
    def calcular_taxa(): 
        pass
        
        
class Carro(Veiculo):
    def calcular_taxa(self, saida: datetime):
        taxa = 5.0
        periodo = saida - self.chegada
        horas = periodo.total_seconds() / 3600
        valor_final = horas * taxa
        resultado = f"""
        Calculando taxa do Estacionamento
        O Carro da marca {self.marca}, de modelo {self.modelo}
        Permanesceu estacionado durante {horas:.2f} horas
        Valor total a ser cobrado: R${valor_final:.2f}
        """
        return resultado
    

class Moto(Veiculo):
    def calcular_taxa(self, saida: datetime):
        taxa = 2.50
        periodo = saida - self.chegada
        horas = periodo.total_seconds() / 3600
        valor_final = horas * taxa
        resultado = f"""
        Calculando taxa do Estacionamento
        A Moto da marca {self.marca}, de modelo {self.modelo}
        Permanesceu estacionado durante {horas:.2f} horas
        Valor total a ser cobrado: R${valor_final:.2f}
        """
        return resultado

class Caminhao(Veiculo):
    def calcular_taxa(self, saida: datetime):
        taxa = 12.0
        periodo = saida - self.chegada
        horas = periodo.total_seconds() / 3600
        valor_final = horas * taxa
        resultado = f"""
        Calculando taxa do Estacionamento
        O Caminhao da marca {self.marca}, de modelo {self.modelo}
        Permanesceu estacionado durante {horas:.2f} horas
        Valor total a ser cobrado: R${valor_final:.2f}
        """
        return resultado


veiculo1 = Carro("DMC", "DeLorean", datetime(2024,9,20,8,0,0))
v1_saida = veiculo1.calcular_taxa(datetime(2024,9,20,12,30,0))
print(v1_saida)


veiculo2 = Moto("Honda", "Biz", datetime(2024,9,20,8,0,0))
v2_saida = veiculo2.calcular_taxa(datetime(2024,9,20,12,30,0))
print(v2_saida)

veiculo3 = Caminhao("Mercedez", "Caminhao", datetime(2024,9,20,8,0,0))
v3_saida = veiculo3.calcular_taxa(datetime(2024,9,20,12,30,0))
print(v3_saida)




            






        
