from Empregado import Empregado

class Assalariado(Empregado):

    def __init__(self, nome, endereco, salario):
        Empregado.__init__(self, nome, endereco)
        self._salario = salario
