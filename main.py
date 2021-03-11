#!/usr/bin/env python
# coding: utf-8

from funcionario import CadFuncionario
import pandas as pd

#Teste
sis = CadFuncionario()
sis.criar_tabela_de_funcionarios()
sis.inserir_funcionario_na_tabela()
sis.inserir_funcionario_na_tabela()
sis.remover_funcionario_da_tabela(0)
sis.modificar_dados_da_tabela(1, 'endereco', 'Salvador')
print(sis.tabela)
