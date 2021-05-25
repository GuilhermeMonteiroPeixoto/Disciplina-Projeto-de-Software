import pandas as pd
from datetime import datetime, timedelta

Metodo_Pagamento = pd.DataFrame(columns=['_id','Forma','Valor'])

def ValorPagamento(num_id, Metodo_Pagamento, Cad_Funcionario, Func_Assalariado, Func_Comissionado, Func_Horista, Taxas_Servicos, Resultado_Vendas, Cartao_de_Ponto):
    if (Cad_Funcionario._id == num_id).any():
        
        Aux = Cad_Funcionario.loc[Cad_Funcionario['_id'] == num_id, 'Nome'].item()
        
        if (Func_Assalariado._id == num_id).any():
            Valor = int(Func_Assalariado.loc[Func_Assalariado['_id'] == num_id, 'SalarioMes'].item())

            
        if (Func_Horista._id == num_id).any():
            salarioHora = int(Func_Horista.loc[Func_Horista['_id'] == num_id, 'SalarioHora'].item())
            Extra = 0
            array = []
            for i in range(len(Cartao_de_Ponto[Cartao_de_Ponto['_id'] == num_id])):
                a = Cartao_de_Ponto[Cartao_de_Ponto['_id'] == num_id].iloc[i]
                b = (datetime.strptime(a['Saida'], '%H:%M') - datetime.strptime(a['Entrada'], '%H:%M')).total_seconds()/3600
                if b > 8:
                    Extra = (b-8)*1.5*salarioHora

                b = 8*salarioHora + Extra
                array.append(b)
            Valor = sum(array)
            
        if (Func_Comissionado._id == num_id).any():
            Valor = Resultado_Vendas[Resultado_Vendas['_id'] == num_id].Valor.sum()
        
        Aux = Cad_Funcionario.loc[Cad_Funcionario['_id'] == num_id, 'Nome'].item()
        if (Taxas_Servicos.Nome == Aux).any():
            Desconto_Fixo = int(Taxas_Servicos.loc[Taxas_Servicos['Nome'] == Aux, 'Taxas'].item())
            Desconto_Adicional = int(Taxas_Servicos.loc[Taxas_Servicos['Nome'] == Aux, 'Adicional'].fillna(0).item())
        else:
            Desconto_Fixo = 0
            Desconto_Adicional = 0
        Valor = Valor - (Desconto_Fixo + Desconto_Adicional)
        
        Metodo_Pagamento.iloc[Metodo_Pagamento[Metodo_Pagamento['_id'] == num_id].index, Metodo_Pagamento.columns.get_loc('Valor')] = str(Valor)
            
    return Metodo_Pagamento

def mudarMetodoPagamento(num_id, Metodo_Pagamento, Deposito):
    if (Metodo_Pagamento._id == num_id).any():
        Metodo_Pagamento = Metodo_Pagamento.drop(Metodo_Pagamento[Metodo_Pagamento['_id'] == num_id].index, axis=0)      
        if (Deposito._id == num_id).any():
            Deposito = Deposito.drop(Deposito[Deposito['_id'] == num_id].index, axis=0)

        Forma = str(input('Forma de Pagamento: '))
        dic = {'_id': num_id,
               'Forma': Forma}
        
        Metodo_Pagamento = Metodo_Pagamento.append(dic, ignore_index=True)
    return Metodo_Pagamento, Deposito
