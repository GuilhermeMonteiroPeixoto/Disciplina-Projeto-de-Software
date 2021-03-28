from MetodoPagamento import MetodoPagamento

class Deposito(MetodoPagamento):

    def __init__(self, valor, idEmpregado, tipo, agencia, conta):
        MetodoPagamento.__init__(self, valor, idEmpregado, tipo)
        self._agencia = agencia
        self._conta = conta
