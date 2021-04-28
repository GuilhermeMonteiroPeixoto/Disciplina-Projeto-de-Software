from Empregado import Empregado
from Horista import Horista
from Comissionado import Comissionado
from Assalariado import Assalariado
import pandas as pd

def addEmpregado(df1):
    nome = str(input('Nome: '))
    endereco = str(input('Endereço: '))
    filiado = str(input('Filiado: '))
    tipo = str(input('Tipo de Contrato: '))

    if tipo == 'Horista':
        salariohora = int(input('Salário por Hora: '))
        Empregado = Horista(nome, endereco, filiado, tipo, salariohora)
        dic = {'Nome': Empregado._nome,
               'Endereco': Empregado._endereco,
               'Filiado': Empregado._filiado,
               'Tipo': Empregado._tipo,
               'SalarioHora': Empregado._salariohora}
        df1 = df1.append(dic, ignore_index=True)
            
    if tipo == 'Comissionado':
        vendas = int(input('Numero de Vendas: '))
        porcentagem = int(input('Porcentagem na venda: '))
        Empregado = Comissionado(nome, endereco, filiado, tipo, vendas, porcentagem)
        dic = {'Nome': Empregado._nome,
               'Endereco': Empregado._endereco,
               'Filiado': Empregado._filiado,
               'Tipo': Empregado._tipo,
               'vendas': Empregado._vendas,
               'porcentagem': Empregado._porcentagem}
        df1 = df1.append(dic, ignore_index=True)

    if tipo == 'Assalariado':
        salariomes = int(input('Salario Mensal: '))
        Empregado = Assalariado(nome, endereco, filiado, tipo, salariomes)
        dic = {'Nome': Empregado._nome,
               'Endereco': Empregado._endereco,
               'Filiado': Empregado._filiado,
               'Tipo': Empregado._tipo,
               'SalarioMensal': Empregado._salario}
        df1 = df1.append(dic, ignore_index=True)
        
    return df1

def deletarEmpregado(df1, indexx):
    df1 = df1.drop(df1.index[indexx])
    return df1
