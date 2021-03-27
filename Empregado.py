import datetime

class Empregado:

    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco
        self._numid = int(datetime.datetime.now().strftime("%S%f"))

    
