import pandas as pd
from datetime import datetime, timedelta

Resultado_Vendas = pd.DataFrame(columns=['_id','Data','Valor'])

def addResultadoVendas(num_id, Resultado_Vendas, Func_Comissionado):
    if (Func_Comissionado._id == num_id).any():
        Data = str(input('Data: '))
        Valor = int(input('Valor: '))
        
        dic = {'_id': num_id,
               'Data': Data,
               'Valor': Valor}
        
        Resultado_Vendas = Resultado_Vendas.append(dic, ignore_index=True)
    return Resultado_Vendas
