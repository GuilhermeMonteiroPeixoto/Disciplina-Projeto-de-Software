from Empregado import Empregado

class Horista(Empregado):

    def __init__(self, nome, endereco, salariohora):
        Empregado.__init__(self, nome, endereco)
        self._salariohora = salariohora
