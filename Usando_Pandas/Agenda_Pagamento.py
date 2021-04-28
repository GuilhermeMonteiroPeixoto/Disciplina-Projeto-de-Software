import pandas as pd
from datetime import datetime, timedelta

Agenda_Pagamento = pd.DataFrame(columns=['_id','Tipo','Data'])

def RodarFolha(Agenda_Pagamento, Metodo_Pagamento, Deposito):
    dia = str(input('Data: '))
    Novoaa = Agenda_Pagamento.loc[Agenda_Pagamento['Data'] == dia, ['_id','Data']]
    Novoaa = pd.merge(Novoaa, Metodo_Pagamento, how = 'inner', on = '_id')
    Novoaa = pd.merge(Novoaa, Deposito, how = 'outer', on = '_id')
    return Novoaa
