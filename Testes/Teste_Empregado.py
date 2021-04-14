from Empregado import Empregado


Empregado1 = Empregado('Guilherme','Maceió','Sim')
Empregado2 = Empregado('Bruno', 'Recife', 'Nao')
Empregado3 = Empregado('Julia', 'Aracaju', 'Sim')

print('\n\n')
Empregado1.printEmpregado()
Empregado2.printEmpregado()
Empregado3.printEmpregado()

Empregado1.mudarNome('Guilherme Monteiro')
Empregado3.mudarNome('Julia Ferreira')

Empregado1.mudarEndereco('Natal')
Empregado2.mudarEndereco('São Paulo')

Empregado2.mudarFiliado('Sim')

print('\n\n')
Empregado1.printEmpregado()
Empregado2.printEmpregado()
Empregado3.printEmpregado()
