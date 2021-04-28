from Empregado import Empregado
from Comissionado import Comissionado

Empregado1 = Comissionado('Guilherme', 'Maceió', 'Sim', 5, 30)
Empregado1.printComissionado()

Empregado1.mudarVendas(50)
Empregado1.mudarPorcentagem(10)
Empregado1.printComissionado()
