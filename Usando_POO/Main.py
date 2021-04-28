from Empregado import Empregado
from Horista import Horista
from Comissionado import Comissionado
from Assalariado import Assalariado
from ConfigCadastro import addEmpregado, deletarEmpregado
import pandas as pd

tabela = pd.DataFrame()
tabela = addEmpregado(tabela)
tabela = addEmpregado(tabela)
tabela = addEmpregado(tabela)
tabela = addEmpregado(tabela)
tabela = addEmpregado(tabela)
tabela = addEmpregado(tabela)
print('\n\n',tabela)

tabela = deletarEmpregado(tabela, 1)
print('\n\n',tabela)
