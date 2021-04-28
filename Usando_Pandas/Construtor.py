import Cad_Empregado as CE
import Horista
import Assalariado
import Comissionado
import Cartao_de_Ponto as CP
import Agenda_Pagamento as AP
import Metodo_Pagamento as MP
import Deposito
import Resultado_Vendas as RV
import Taxas_Servicos as TS
import Change
import os


def Add():
    CE.Cad_Funcionario, Horista.Func_Horista, Assalariado.Func_Assalariado, Comissionado.Func_Comissionado, TS.Taxas_Servicos, MP.Metodo_Pagamento, Deposito.Deposito, AP.Agenda_Pagamento = CE.addEmpregado(CE.Cad_Funcionario, Horista.Func_Horista, Assalariado.Func_Assalariado, Comissionado.Func_Comissionado, TS.Taxas_Servicos, MP.Metodo_Pagamento, Deposito.Deposito, AP.Agenda_Pagamento)

def Remove():
    num_id = str(input('ID do usuario: '))
    CE.Cad_Funcionario, Horista.Func_Horista, Assalariado.Func_Assalariado, Comissionado.Func_Comissionado, TS.Taxas_Servicos, CP.Cartao_de_Ponto, RS.Resultado_Vendas, MP.Metodo_Pagamento, Deposito.Deposito, AP.Agenda_Pagamento = CE.removerEmpregado(num_id ,CE.Cad_Funcionario, Horista.Func_Horista, Assalariado.Func_Assalariado, Comissionado.Func_Comissionado, TS.Taxas_Servicos, CP.Cartao_de_Ponto, RS.Resultado_Vendas, MP.Metodo_Pagamento, Deposito.Deposito, AP.Agenda_Pagamento)

def AddCartao():
    num_id = str(input('ID do usuario: '))
    CP.Cartao_de_Ponto = CP.addCartaodePonto(num_id, CP.Cartao_de_Ponto, Horista.Func_Horista)

def AddVenda():
    num_id = str(input('ID do usuario: '))
    RV.Resultado_Vendas = RV.addResultadoVendas(num_id, RV.Resultado_Vendas, Comissionado.Func_Comissionado)

def AddTaxa():
    Nome = str(input('Nome do Empregado: '))
    new = int(input('Taxa adicional: '))
    TS.Taxas_Servicos = TS.addTaxaAdicional(Nome, TS.Taxas_Servicos, CE.Cad_Funcionario, new)

def Pagamento():
    for a in range(len(MP.Metodo_Pagamento)):
        num_id = MP.Metodo_Pagamento['_id'].iloc[a]
        MP.Metodo_Pagamento = MP.ValorPagamento(str(num_id) , MP.Metodo_Pagamento, CE.Cad_Funcionario, Assalariado.Func_Assalariado, Comissionado.Func_Comissionado, Horista.Func_Horista, TS.Taxas_Servicos, RV.Resultado_Vendas, CP.Cartao_de_Ponto)

def ChangeNome():
    num_id = str(input('ID do usuario: '))
    CE.Cad_Funcionario, TS.Taxas_Servicos = Change.mudarNome(num_id, CE.Cad_Funcionario, TS.Taxas_Servicos)

def ChangeEndereco():
    num_id = str(input('ID do usuario: '))
    CE.Cad_Funcionario = Change.mudarEndereco(num_id, CE.Cad_Funcionario)

def ChangeTipo():
    num_id = str(input('ID do usuario: '))
    CE.Cad_Funcionario, Assalariado.Func_Assalariado, Horista.Func_Horista, Comissionado.Func_Comissionado, AP.Agenda_Pagamento, CP.Cartao_de_Ponto, RV.Resultado_Vendas = Change.mudarTipo(num_id, CE.Cad_Funcionario, Assalariado.Func_Assalariado, Horista.Func_Horista, Comissionado.Func_Comissionado, AP.Agenda_Pagamento, CP.Cartao_de_Ponto, RV.Resultado_Vendas)

def ChangeMetodoPagamento():
    num_id = str(input('ID do usuario: '))
    MP.Metodo_Pagamento, Deposito.Deposito = MP.mudarMetodoPagamento(num_id, MP.Metodo_Pagamento, Deposito.Deposito)

def MostrarTabela():
    print(CE.Cad_Funcionario)
    print(AP.Agenta_Pagamento)
    print(MP.Metodo_Pagamento)

def Folha():
    folhinha = AP.RodarFolha(AP.Agenda_Pagamento, MP.Metodo_Pagamento, Deposito.Deposito)
    return folhinha

def Menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('FOLHA DE PAGAMENTO\n')

    print('Menu:')
    print("1 - Adicionar empregado") 
    print("2 - Remoção empregado") 
    print("3 - Lançar um cartão") 
    print("4 - Lançar resultado venda")
    print("5 - Lançar taxa serviço")
    print("6 - Alterar detalhes")
    print("7 - Folha de pagamento para hoje")
    print("8 - Mostrar Funcionarios")
    print("9 - Agendar pagamento")
    print("10 - Criar novas agendas")

    opcao = int(input('Opção: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if opcao == 1:
        print('\nCadastro de Empregado')
        Add()

    if opcao == 2:
        print('\nRemoção de Empregado')
        Remove()

    if opcao == 3:
        print('\nAdicionando Cartão de Ponto')
        AddCartao()

    if opcao == 4:
        print('\nAdicionando Venda')
        AddVenda()

    if opcao == 5:
        print('\nAdicionando Taxa Sindical')
        AddTaxa()

    if opcao == 6:
        print('\nModificação de Empregado:')
        print('1. Mudar Nome')
        print('2. Mudar Endereço')
        print('3. Mudar Tipo de Contrato')
        print('4. Mudar Metodo de Pagamento')
        opcao2 = int(input('Opção: '))
        os.system('cls' if os.name == 'nt' else 'clear')
        if opcao2 == 1:
            ChangeNome()

        if opcao2 == 2:
            ChangeEndereco()

        if opcao2 == 3:
            ChangeTipo()

        if opcao2 == 4:
            ChangeMetodoPagamento()

    if opcao == 7:
        Pagamento()
        la = Folha()
        print(la)
        input('Enter - para continuar')

    if opcao == 8:
        MostrarTabela()
        input('Enter - para continuar')
