from Empregado import Empregado
from Comissionado import Comissionado
from Assalariado import Assalariado
from Horista import Horista

F = Comissionado('Guilherme', 'Maceió/Tabuleiro', 10)

print(F._numid, F._nome, F._endereco)

G = Horista('Emrehliug', 'Recife/UR', 35)

print(G._numid, G._nome, G._endereco)
