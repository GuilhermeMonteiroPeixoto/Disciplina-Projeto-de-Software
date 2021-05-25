import pandas as pd
from datetime import datetime, timedelta

def mudarNome(num_id, Cad_Funcionario, Taxas_Servicos):
    if (Cad_Funcionario._id == num_id).any():
        Nome = Cad_Funcionario.loc[Cad_Funcionario['_id'] == num_id, 'Nome'].item()
        new_value = str(input('Novo Nome: '))
        Taxas_Servicos.iloc[Taxas_Servicos[Taxas_Servicos['Nome'] == Nome].index, Taxas_Servicos.columns.get_loc('Nome')] = new_value
        Cad_Funcionario.iloc[Cad_Funcionario[Cad_Funcionario['_id'] == num_id].index, Cad_Funcionario.columns.get_loc('Nome')] = new_value
    else:
        print('Erro! >> Esse empregado não existe!')
    return Cad_Funcionario, Taxas_Servicos

def mudarEndereco(num_id, Cad_Funcionario):
    if (Cad_Funcionario._id == num_id).any():
        new_value = str(input('Novo Endereço: '))
        Cad_Funcionario.iloc[Cad_Funcionario[Cad_Funcionario['_id'] == num_id].index, Cad_Funcionario.columns.get_loc('Endereco')] = new_value
    return Cad_Funcionario

def mudarTipo(num_id, Cad_Funcionario, Func_Assalariado, Func_Horista, Func_Comissionado, Agenda_Pagamento, Cartao_de_Ponto, Resultado_Vendas):
    
    tipo = str(input('Novo Tipo de Contrato: '))
    
    if (Func_Assalariado._id == num_id).any():
        #remover de Func_Assalariado
        Func_Assalariado = Func_Assalariado.drop(Func_Assalariado[Func_Assalariado['_id'] == num_id].index, axis=0)
        
        #remover de Agenda_Pagamento
        Agenda_Pagamento = Agenda_Pagamento.drop(Agenda_Pagamento[Agenda_Pagamento['_id'] == num_id].index, axis=0)
    
    if (Func_Horista._id == num_id).any():
        #remover de Func_Horista
        Func_Horista = Func_Horista.drop(Func_Horista[Func_Horista['_id'] == num_id].index, axis=0)
        #remover de Cartao_de_Ponto   
        if (Cartao_de_Ponto._id == num_id).any():#CartaodePonto
            Cartao_de_Ponto = Cartao_de_Ponto.drop(Cartao_de_Ponto[Cartao_de_Ponto['_id'] == num_id].index, axis=0)
        
        #remover de Agenda_Pagamento
        Agenda_Pagamento = Agenda_Pagamento.drop(Agenda_Pagamento[Agenda_Pagamento['_id'] == num_id].index, axis=0)
        
    
    if (Func_Comissionado._id == num_id).any():
        #remover de Func_Comissionado
        Func_Comissionado = Func_Comissionado.drop(Func_Comissionado[Func_Comissionado['_id'] == num_id].index, axis=0)
        #remover de Resultado_Vendas    
        if (Resultado_Vendas._id == num_id).any():#ResultadoVendas
            Resultado_Vendas = Resultado_Vendas.drop(Resultado_Vendas[Resultado_Vendas['_id'] == num_id].index, axis=0)
        
        #remover de Agenda_Pagamento
        Agenda_Pagamento = Agenda_Pagamento.drop(Agenda_Pagamento[Agenda_Pagamento['_id'] == num_id].index, axis=0)
    
    Cad_Funcionario.iloc[Cad_Funcionario[Cad_Funcionario['_id'] == num_id].index, Cad_Funcionario.columns.get_loc('Tipo')] = tipo
    #Cadastro na Tabela de Horista/Assalariado/Comissionado
    #Cadastro na Tabela de Horista
    if tipo == 'Horista':
        salarioHora = int(input('Salario/Hora: '))
        
        dic = {'_id': num_id,
               'SalarioHora': salarioHora}
        
        Func_Horista = Func_Horista.append(dic, ignore_index=True)
        
        periodo_pagamento = 'semanalmente'
        data_pagamento = datetime.now()+timedelta(days=7)
        
    #Cadastro na Tabela de Comissionado
    if tipo == 'Comissionado':
        comissao = int(input('Comissão (%): '))
        
        dic = {'_id': num_id,
               'Porcentagem': comissao}
        
        Func_Comissionado = Func_Comissionado.append(dic, ignore_index=True)
        
        periodo_pagamento = 'bi- semanalmente'
        data_pagamento = datetime.now()+timedelta(days=14)
        
    #Cadastro na Tabela de Assalariado
    if tipo == 'Assalariado':
        salario = int(input('Salario: '))
        
        dic = {'_id': num_id,
               'SalarioMes': salario}
        
        Func_Assalariado = Func_Assalariado.append(dic, ignore_index=True)
        
        periodo_pagamento = 'mensalmente'
        data_pagamento = datetime.now()+timedelta(days=30)
        
    #Cadastro na Tabela Agenda_Pagamento
    dic = {'_id': num_id,
           'Tipo': periodo_pagamento,
           'Data': data_pagamento.strftime('%Y-%m-%d')}
    
    Agenda_Pagamento = Agenda_Pagamento.append(dic, ignore_index=True)
    
    return Cad_Funcionario, Func_Assalariado, Func_Horista, Func_Comissionado, Agenda_Pagamento, Cartao_de_Ponto, Resultado_Vendas

