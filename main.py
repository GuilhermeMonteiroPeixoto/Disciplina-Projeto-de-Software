#!/usr/bin/env python
# coding: utf-8

from SistemaCadastro import SistemaCadastro
from Empregado import Empregado

bd = SistemaCadastro()

CadFuncionario = Empregado()

bd.inserir_funcionario_na_tabela(CadFuncionario)

bd.remover_funcionario_da_tabela(0)
bd.modificar_dados_da_tabela(0, 'endereco', 'Rua Salvador')

print(bd.tabela)