#!/usr/bin/env python
# coding: utf-8

from datetime import datetime
import pandas as pd

class CadFuncionario:
    
    def tabela_funcionarios(self):
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

    def inserir_tabela(self):
        self.dados()
        self.tabela = self.tabela.append(self.informacao, ignore_index=True)
        return

    def remover_funcionario(self, _id):
        if _id < len(self.tabela.index):
            self.tabela = self.tabela.drop(_id)
        else:
            print("ERRO! Funcionario não encontrado.")
        return

    def modificar_valor(self, _id, coluna, valor):
        if _id < len(self.tabela.index):
            self.tabela.at[_id, coluna] = valor
        else:
            print("ERRO! Funcionario não encontrado.")
        return

    def imprimir_dados(self, _id):
        if _id < len(self.tabela.index):
            print(self.tabela.loc[_id])
        else:
            print("ERRO! Funcionario não encontrado.")


# Para usar essa Class:
# 
# ```sh
# df_funcionarios = CadFuncionario()
# ```
# Criar tabela
# ```sh
# df_funcionarios.tabela_funcionarios()
# ```
# Inserir Funcionario
# ```sh
# df_funcionarios.inserir_tabela()
# ```
# Remover Funcionario
# ```sh
# df_funcionarios.remover_funcionario(Id_do_funcionario)
# ```
# Modificar Dados do Funcionario
# ```sh
# df_funcionarios.modificar_valor(Id_do_funcionario, 'Coluna para modificar', 'valor')
# ```
# Imprimir Dados de um Funcionario
# ```sh
# df_funcionarios.imprimir_dados(Id_do_funcionario)
# ```
