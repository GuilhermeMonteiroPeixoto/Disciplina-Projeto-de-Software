import pandas as pd
from datetime import datetime, timedelta

Cartao_de_Ponto = pd.DataFrame(columns=['_id','Data','Entrada','Saida'])

def addCartaodePonto(num_id, Cartao_de_Ponto, Func_Horista):
    if (Func_Horista._id == num_id).any():
        Data = str(input('Data: '))
        Entrada = str(input('Entrada: '))
        Saida = str(input('Saida: '))
        '''
        Data = datetime.strptime(str(input('Data: ')) , '%Y-%m-%d')
        Entrada = datetime.strptime(str(input('Entrada: ')) , '%H:%M')
        Saida = datetime.strptime(str(input('Saida: ')) , '%H:%M')
        '''
        dic = {'_id': num_id,
               'Data': Data,
               'Entrada': Entrada,
               'Saida': Saida}
        
        Cartao_de_Ponto = Cartao_de_Ponto.append(dic, ignore_index=True)
    return Cartao_de_Ponto
