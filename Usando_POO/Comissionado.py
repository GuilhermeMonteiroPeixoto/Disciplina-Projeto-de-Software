from Empregado import Empregado

class Comissionado(Empregado):

    def __init__(self, nome, endereco, filiado, tipo, porcentagem, vendas):
        super().__init__(nome, endereco, filiado, tipo)
        self._vendas = vendas
        self._porcentagem = porcentagem

    def mudarVendas(self, vendas):
        self._vendas = vendas

    def mudarPorcentagem(self, porcentagem):
        self._porcentagem = porcentagem
