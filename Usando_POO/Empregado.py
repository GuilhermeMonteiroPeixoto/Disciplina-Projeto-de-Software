import datetime

class Empregado:

    def __init__(self, nome, endereco, filiado, tipo):
        self._nome = nome
        self._endereco = endereco
        self._numid = int(datetime.datetime.now().strftime("%S%f"))
        self._filiado = filiado
        self._tipo = tipo

    def mudarNome(self, nome):
        self._nome = nome

    def mudarEndereco(self, endereco):
        self._endereco = endereco

    def mudarFiliado(self, filiado):
        self._filiado = filiado

    def mudarTipo(self, tipo):
        self._tipo = tipo

