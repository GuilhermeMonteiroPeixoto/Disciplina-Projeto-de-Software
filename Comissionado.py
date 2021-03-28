from Empregado import Empregado

class Comissionado(Empregado):

    def __init__(self, nome, endereco, porcentagem, vendas):
        Empregado.__init__(self, nome, endereco)
        self._vendas = vendas
        self._porcentagem = porcentagem
