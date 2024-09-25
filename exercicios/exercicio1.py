# criar o modelo de classes para pagar um churrasco - já corrigido em sala
class ContaBancaria:
    def __init__( # creiando uma instancia
            self,
            agencia: str,
            titular: str,
            n_conta: str,
            saldo: float,
            chave_pix: str,
    ): 
        self.agencia = agencia
        self.titular = titular
        self.n_conta = n_conta
        self.saldo = saldo
        self.chave_pix = chave_pix 

    def fazer_pix(
            self,
            valor: float,
            destinatario: str,
            ):
        if self.saldo >= valor:
            print(f"A transferencia de {valor} reais foi realizada para a chave {destinatario.chave_pix}.")
            destinatario.saldo += valor
        else:
            print("Transferencia não realizada. Saldo insuficiente")


guilherme = ContaBancaria(
    agencia="123456",
    titular="Guilherme Morrone",
    n_conta="4563123",
    saldo=10000000,
    chave_pix="guilherme@morrone"

)

clovis  = ContaBancaria(
    agencia="54321",
    titular="Clovis Morrone",
    n_conta="564789",
    saldo=10000,
    chave_pix="clovis@morrone"

)

guilherme.fazer_pix(50, clovis)# chama a função e adiciona como o parametro o valor e o destinatário

print(f"O destinatario {clovis.titular} agora possui o saldo de {clovis.saldo} reais.")