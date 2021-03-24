from datetime import datetime

class CartaoPontoDia:
    def __init__(self, timein, timeout): #datetime(2021, 3, 22, 9)
        diferenca = timeout-timein
        self.horas = diferenca.total_seconds()/3600