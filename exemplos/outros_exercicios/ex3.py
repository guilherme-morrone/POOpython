class Instrumento:
    def tocar(self):
        pass


class Violao(Instrumento):
    def tocar(self):
        print("Tocando a abertura do globo rural")


class Piano(Instrumento):
    def tocar(self):
        print("Tocando a abertura dos backyardgans")
