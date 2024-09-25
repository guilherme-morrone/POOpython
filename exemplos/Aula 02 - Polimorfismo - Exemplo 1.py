from abc import ABC, abstractmethod


# Classe abstrata. Toda Mídia Gravável deve ter o método `gravar` implementado.
class MidiaGravavel(ABC):
    @abstractmethod
    def gravar(self):
        pass


class Pendrive(MidiaGravavel):
    def gravar(self):  # Implementação do método `gravar`.
        print("O arquivo foi gravado no pendrive.")


class ArmazenamentoNuvem(MidiaGravavel):
    def gravar(self):  # Implementação do método `gravar`.
        print("O arquivo foi gravado na nuvem.")


# Esta classe herda de `ArmazenamentoNuvem`, o que significa que também é uma Mídia Gravável.
class GoogleDrive(ArmazenamentoNuvem):
    # Aqui não ocorre a implementação do método, pois isso ocorreu em `ArmazenamentoNuvem.gravar`.
    # Aqui ocorre a sobrecarga, onde o comportamento do método `gravar` será diferente da sua classe-mãe/superclasse.
    def gravar(self):
        print("O documento foi gravado no Google Drive.")


# Esta classe herda de `ArmazenamentoNuvem`, o que significa que também é uma Mídia Gravável.
class OneDrive(ArmazenamentoNuvem):
    # Outra sobrecarga. O comportamento do método foi alterado.
    def gravar(self):
        # O `super()` chama a superclasse, ou seja, `ArmazenamentoNuvem`.
        # Portanto, aqui está sendo chamado o comportamento da classe-mãe.
        # Isso fará com que o print dentro de ArmazenamentoNuvem.gravar seja executado.
        super().gravar()
        # Outra print ocorrerá.
        print("O documento foi gravado no One Drive.")


# Instanciando um objeto do tipo Pendrive.
pendrive_antigo = Pendrive()
pendrive_antigo.gravar()

# Instanciando um objeto do tipo ArmazenamentoNuvem.
outra_nuvem = ArmazenamentoNuvem()
outra_nuvem.gravar()

# Instanciando um objeto do tipo Google Drive, onde ocorre sobrecarga.
google_drive = GoogleDrive()
google_drive.gravar()

# Instanciando um objeto do tipo OneDrive, onde ocorre sobrecarga com chamada da superclasse.
one_drive = OneDrive()
one_drive.gravar()
