from MetodoPagamento import MetodoPagamento

class ChequeMao(MetodoPagamento):

    def __init__(self, valor, idEmpregado, tipo):
        MetodoPagamento.__init__(self, valor, idEmpregado, tipo)
