from Empregado import Empregado

class Horista(Empregado):

    def __init__(self, nome, endereco, filiado, tipo, salariohora):
        super().__init__(nome, endereco, filiado, tipo)
        self._salariohora = salariohora

    def mudarSalarioHora(self, salariohora):
        self._salariohora = salariohora
