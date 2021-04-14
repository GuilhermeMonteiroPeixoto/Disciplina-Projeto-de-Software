from Empregado import Empregado

class Horista(Empregado):

    def __init__(self, nome, endereco, filiado, salariohora):
        Empregado.__init__(self, nome, endereco, filiado)
        self._salariohora = salariohora

    def mudarSalarioHora(self, salariohora):
        self._salariohora = salariohora

    def printHorista(self):
        print(self._nome, self._endereco, self._filiado, self._salariohora)
