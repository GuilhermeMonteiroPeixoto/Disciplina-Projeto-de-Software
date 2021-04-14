from Empregado import Empregado

class Assalariado(Empregado):

    def __init__(self, nome, endereco, filiado, salario):
        Empregado.__init__(self, nome, endereco, filiado)
        self._salario = salario

    def mudarSalario(self, salario):
        self._salario = salario

    def printAssalariado(self):
        print(self._nome, self._endereco, self._filiado, self._salario)
