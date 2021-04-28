from datetime import datetime
import pandas as pd
import numpy as np

class Empregado:
    def __init__(self):
        dicionario = dict()
        dicionario['nome'] = str(input('Nome: '))
        dicionario['endereco'] = str(input('Endereço: '))
        dicionario['metodo'] = str(input('metodo: '))
        
        if dicionario['metodo'] == '2':
            dicionario['Conta'] = str(input('Conta do Banco:'))
        
        dicionario['tipo'] = str(input('tipo: '))
        
        if dicionario['tipo'] == '0':
            dicionario['salarioHora'] = str(input('salarioHora: '))
        elif dicionario['tipo'] == '1':
            dicionario['salario'] = str(input('salario: '))
        elif dicionario['tipo'] == '2':
            dicionario['salarioFixo'] = str(input('salarioFixo: '))
            
        dicionario['sindicalista'] = str(input('sindicalista: '))
        
        if dicionario['sindicalista'] == 'S':
            dicionario['taxaFixa'] = str(input('taxaFixa: '))
            
        self.informacao = pd.Series(dicionario)

#Para usar essa Class:
#Cadfucionario = Empregado()