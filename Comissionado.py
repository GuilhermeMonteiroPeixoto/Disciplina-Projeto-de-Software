from Empregado import Empregado

class Comissionado(Empregado):

    def __init__(self, nome, endereco, porcentagem):
        Empregado.__init__(self, nome, endereco)
        self._porcentagem = porcentagem
