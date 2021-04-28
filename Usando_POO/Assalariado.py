from Empregado import Empregado

class Assalariado(Empregado):

    def __init__(self, nome, endereco, filiado, tipo, salario):
        super().__init__(nome, endereco, filiado, tipo)
        self._salario = salario

    def mudarSalario(self, salario):
        self._salario = salario
