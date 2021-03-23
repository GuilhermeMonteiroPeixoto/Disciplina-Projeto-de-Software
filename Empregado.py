from datetime import datetime
import pandas as pd
import numpy as np

class Empregado:
    def __init__(self):
        dicionario = dict()
        dicionario['nome'] = str(input('Nome: '))
        dicionario['endereco'] = str(input('Endereço: '))
        dicionario['metodo'] = str(input('metodo: '))
        dicionario['tipo'] = str(input('tipo: '))
        dicionario['sindicalista'] = str(input('sindicalista: '))
        dicionario['salarioHora'] = str(input('salarioHora: '))
        dicionario['salarioFixo'] = str(input('salarioFixo: '))
        dicionario['percentual'] = str(input('percentual: '))
        dicionario['salario'] = str(input('salario: '))
        dicionario['taxaFixa'] = str(input('taxaFixa: '))
        self.informacao = pd.Series(dicionario)

#Para usar essa Class:
#Cadfucionario = Empregado()