from Empregado import Empregado

class Comissionado(Empregado):

    def __init__(self, nome, endereco, filiado, porcentagem, vendas):
        Empregado.__init__(self, nome, endereco, filiado)
        self._vendas = vendas
        self._porcentagem = porcentagem

    def mudarVendas(self, vendas):
        self._vendas = vendas

    def mudarPorcentagem(self, porcentagem):
        self._porcentagem = porcentagem

    def printComissionado(self):
        print(self._nome, self._endereco, self._filiado, self._vendas, self._porcentagem)
