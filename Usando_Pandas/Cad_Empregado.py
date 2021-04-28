import pandas as pd
from random import randint
from datetime import datetime, timedelta

Cad_Funcionario = pd.DataFrame(columns=['Nome','_id','Endereco','Tipo','Sindicato'])

def addEmpregado(Cad_Funcionario, Func_Horista, Func_Assalariado, Func_Comissionado, Taxas_Servicos, Metodo_Pagamento, Deposito, Agenda_Pagamento):
    nome = str(input('Nome: '))
    num_id = str(randint(1000, 9999)) #str(input('Num ID: '))
    endereco = str(input('Endereço: '))
    tipo = str(input('Tipo de Contrato: '))
    sindicato = str(input('Sindicato: '))
    
    dic = {'Nome':nome,
           '_id': num_id,
           'Endereco': endereco,
           'Tipo': tipo,
           'Sindicato': sindicato}
    
#Cadastro na Tabela de Funcionario
    Cad_Funcionario = Cad_Funcionario.append(dic, ignore_index=True)
    
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
    
#Cadastro na Tabela do Sindicato
    if sindicato == 'S':
        taxa = int(input('Taxa: '))
        
        dic = {'Nome': nome,
               'Taxas': taxa}
        
        Taxas_Servicos = Taxas_Servicos.append(dic, ignore_index=True)

#Cadastro na Tabela Metodo de Pagamento
    Forma = str(input('Forma de Pagamento: '))
    dic = {'_id': num_id,
           'Forma': Forma}
    
    Metodo_Pagamento = Metodo_Pagamento.append(dic, ignore_index=True)

#Cadastro na Tabela Deposito
    if Forma == 'Deposito':
        Conta = str(input('Conta Bancaria: '))
        dic = {'_id': num_id,
               'Conta': Conta}     
        Deposito = Deposito.append(dic, ignore_index=True)

#Cadastro na Tabela Agenda_Pagamento
    dic = {'_id': num_id,
           'Tipo': periodo_pagamento,
           'Data': data_pagamento.strftime('%Y-%m-%d')}
    
    Agenda_Pagamento = Agenda_Pagamento.append(dic, ignore_index=True)
        
    return Cad_Funcionario, Func_Horista, Func_Assalariado, Func_Comissionado, Taxas_Servicos, Metodo_Pagamento, Deposito, Agenda_Pagamento


def removerEmpregado(num_id ,Cad_Funcionario, Func_Horista, Func_Assalariado, Func_Comissionado, Taxas_Servicos, Cartao_de_Ponto, Resultado_Vendas, Metodo_Pagamento, Deposito, Agenda_Pagamento):
    if (Cad_Funcionario._id == num_id).any():
        
        if (Func_Horista._id == num_id).any():
            Func_Horista = Func_Horista.drop(Func_Horista[Func_Horista['_id'] == num_id].index, axis=0)
            
            if (Cartao_de_Ponto._id == num_id).any():#CartaodePonto
                Cartao_de_Ponto = Cartao_de_Ponto.drop(Cartao_de_Ponto[Cartao_de_Ponto['_id'] == num_id].index, axis=0)

        if (Func_Assalariado._id == num_id).any():
            Func_Assalariado = Func_Assalariado.drop(Func_Assalariado[Func_Assalariado['_id'] == num_id].index, axis=0)

        if (Func_Comissionado._id == num_id).any():
            Func_Comissionado = Func_Comissionado.drop(Func_Comissionado[Func_Comissionado['_id'] == num_id].index, axis=0)
            
            if (Resultado_Vendas._id == num_id).any():#ResultadoVendas
                Resultado_Vendas = Resultado_Vendas.drop(Resultado_Vendas[Resultado_Vendas['_id'] == num_id].index, axis=0)
        
        Aux = Cad_Funcionario.loc[Cad_Funcionario['_id'] == num_id, 'Nome'].item()
        if (Taxas_Servicos.Nome == Aux).any():
            Taxas_Servicos = Taxas_Servicos.drop(Taxas_Servicos[Taxas_Servicos['Nome'] == Aux].index, axis=0)
            
        if (Metodo_Pagamento._id == num_id).any():#MetodoPagamento
            Metodo_Pagamento = Metodo_Pagamento.drop(Metodo_Pagamento[Metodo_Pagamento['_id'] == num_id].index, axis=0)
            
            if (Deposito._id == num_id).any():
                Deposito = Deposito.drop(Deposito[Deposito['_id'] == num_id].index, axis=0)
            
        if (Agenda_Pagamento._id == num_id).any():#AgendaPagamento
            Agenda_Pagamento = Agenda_Pagamento.drop(Agenda_Pagamento[Agenda_Pagamento['_id'] == num_id].index, axis=0)
            
        Cad_Funcionario = Cad_Funcionario.drop(Cad_Funcionario[Cad_Funcionario['_id'] == num_id].index, axis=0)
        
    return Cad_Funcionario, Func_Horista, Func_Assalariado, Func_Comissionado, Taxas_Servicos, Cartao_de_Ponto, Resultado_Vendas, Metodo_Pagamento, Deposito, Agenda_Pagamento
