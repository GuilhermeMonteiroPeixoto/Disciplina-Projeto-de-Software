from MetodoPagamento import MetodoPagamento

class ChequeCorreio(MetodoPagamento):

    def __init__(self, valor, idEmpregado, tipo, endereco):
        MetodoPagamento.__init__(self, valor, idEmpregado, tipo)
        self._endereco = endereco
