from MetodoPagamento import MetodoPagamento
from ChequeMao import ChequeMao
from ChequeCorreio import ChequeCorreio
from Deposito import Deposito

M1 = ChequeCorreio(3000, 41351263, 'Assalariado', 'Maceió/AL')

print(M1._idEmpregado, M1._tipo, M1._valor, M1._endereco)

M2 = Deposito(2000, 99351263, 'Assalariado', 'BB55', '2645287')

print(M2._idEmpregado , M2._tipo, M2._valor, M2._conta, M2._agencia)
