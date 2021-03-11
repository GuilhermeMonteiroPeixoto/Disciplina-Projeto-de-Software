#!/usr/bin/env python
# coding: utf-8

from datetime import datetime
import pandas as pd

class CadFuncionario:
    
    def criar_tabela_de_funcionarios(self):
        self.tabela = pd.DataFrame(columns = ['nome','endereco', 'metodo', 'tipo',
                                     'sindicalista', 'salarioHora', 'salarioFixo', 'percentual',
                                    'salario','taxaFixa'])
        return

    def dados(self):
        dicionario = dict()
        dicionario['nome'] = str(input('Nome: '))
        dicionario['endereco'] = str(input('Endereço: '))
        dicionario['metodo'] = str(input('metodo: '))
        dicionario['tipo'] = str(input('tipo: '))
        dicionario['sindicalista'] = str(input('sindicalista: '))
        dicionario['salarioHora'] = str(input('salarioHora: '))
        dicionario['salarioFixo'] = str(input('salarioFixo: '))
        dicionario['percentual'] = str(input('percentual: '))
        dicionario['salario'] = str(input('salario: '))
        dicionario['taxaFixa'] = str(input('taxaFixa: '))
        self.informacao = pd.Series(dicionario)
        return

    def inserir_funcionario_na_tabela(self):
        self.dados()
        self.tabela = self.tabela.append(self.informacao, ignore_index=True)
        return

    def remover_funcionario_da_tabela(self, _id):
        self.tabela = self.tabela.drop(_id)
        return

    def modificar_dados_da_tabela(self, _id, coluna, valor):
        self.tabela.at[_id, coluna] = valor
        return

    def imprimir_dados(self, _id):
        print(self.tabela.loc[_id])



# Para usar essa Class:
# 
# ```sh
# df_funcionarios = CadFuncionario()
# ```
# Criar tabela
# ```sh
# df_funcionarios.criar_tabela_de_funcionarios()
# ```
# Inserir Funcionario
# ```sh
# df_funcionarios.inserir_funcionario_na_tabela()
# ```
# Remover Funcionario
# ```sh
# df_funcionarios.remover_funcionario_da_tabela(Id_do_funcionario)
# ```
# Modificar Dados do Funcionario
# ```sh
# df_funcionarios.modificar_dados_da_tabela(Id_do_funcionario, 'Coluna para modificar', 'valor')
# ```
# Imprimir Dados de um Funcionario
# ```sh
# df_funcionarios.imprimir_dados(Id_do_funcionario)
# ```
