#desafio - criar o sistema de locação de um veículo
from datetime import date
class Veiculo:
    def __init__(
            self,
            marca_veiculo: str,
            modelo_veiculo: str,
            ano_fabric: int,
            tipo_veiculo: str
        ):

        self.marca_veiculo = marca_veiculo
        self.modelo_veiculo = modelo_veiculo
        self.ano_fabric = ano_fabric
        self.tipo_veiculo = tipo_veiculo


class Motorista:
    def __init__(
            self,
            nome_mot: str,
            cpf_mot: str,
            n_cnh: int,
            data_nasc_mot: date,
            tel_mot: str,
            endereco_mot: str
        ):
        
        self.nome_mot = nome_mot
        self.cpf_mot = cpf_mot
        self.n_cnh = n_cnh
        self.data_nasc_mot = data_nasc_mot
        self.tel_mot = tel_mot
        self.endereco_mot = endereco_mot


class Aluguel:
    def __init__(
            self,
            periodo_locacao: int, # nesse caso, o aluguel será cobrado por dia
            motorista_responsavel: Motorista,
            veiculo_alugado: Veiculo
            ):

            self.periodo_locacao = periodo_locacao
            self.motorista_responsavel = motorista_responsavel
            self.veiculo_alugado = veiculo_alugado


motorista1 = Motorista(
    "Guilherme Morrone",
    "123456-78",
    123456,
    (2004,12,22),
    "4002-8922",
    "rua tchurusbango tchurusbago 8000"
)

veiculo1 = Veiculo(
    marca_veiculo="DMC",
    modelo_veiculo="DeLorean",
    ano_fabric=1981,
    tipo_veiculo="máquina-do-tempo"
)

aluguel1 = Aluguel(
    periodo_locacao=3,
    motorista_responsavel= motorista1.nome_mot,
    veiculo_alugado= veiculo1.modelo_veiculo
)

print(f"O veículo {aluguel1.veiculo_alugado} foi alugado para {aluguel1.motorista_responsavel} por um periodo de {aluguel1.periodo_locacao} dias")