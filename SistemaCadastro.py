#!/usr/bin/env python
# coding: utf-8

from datetime import datetime
import pandas as pd
import numpy as np
from Empregado import Empregado

class SistemaCadastro:
    
    def __init__(self):
        self.tabela = pd.DataFrame()

    def inserir_funcionario_na_tabela(self, empregado):
        self.tabela = self.tabela.append(empregado.informacao, ignore_index=True)
        self.agrupartipo()

    def remover_funcionario_da_tabela(self, _id):
        if _id in np.array(self.tabela.index):
            self.tabela = self.tabela.drop(_id)
            self.agrupartipo()
        else:
            print('Erro - Funcionario nao encontrado')

    def modificar_dados_da_tabela(self, _id, coluna, valor):
        if _id in np.array(self.tabela.index):
            self.tabela.at[_id, coluna] = valor
            self.agrupartipo()
        else:
            print('Erro - Funcionario nao encontrado')

    def imprimir_dados(self, _id):
        if _id in np.array(self.tabela.index):
            print(self.tabela.loc[_id])
        else:
            print('Erro - Funcionario nao encontrado')

    def agrupartipo(self):
        self.tabelahorista = self.tabela[self.tabela['tipo'] == '0']
        self.tabelaassalariado = self.tabela[self.tabela['tipo'] == '1']
        self.tabelacomissionado = self.tabela[self.tabela['tipo'] == '2']
        
# Para usar essa Class:
# db = SistemaCadastro()

# Criar tabela
# db.criar_tabela_de_funcionarios()

# Inserir Funcionario
# db.inserir_funcionario_na_tabela(Funcionario)

# Remover Funcionario
# db.remover_funcionario_da_tabela(Id_do_funcionario)

# Modificar Dados do Funcionario
# db.modificar_dados_da_tabela(Id_do_funcionario, 'Coluna para modificar', 'valor')

# Imprimir Dados de um Funcionario
# db.imprimir_dados(Id_do_funcionario)