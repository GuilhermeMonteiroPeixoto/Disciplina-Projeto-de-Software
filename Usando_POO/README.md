# Folha de Pagamento

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)

During the first part of the project (AB1) there were some problems that made it impossible to build the system in OOP. During the second part of the project (AB2) the system was made in OOP already following the Model-View-Controller.

---------
 O objetivo do projeto é construir um sistema de folha de pagamento. O sistema consiste do gerenciamento de pagamentos dos empregados de uma empresa. Além disso, o sistema deve gerenciar os dados destes empregados, a exemplo os cartões de pontos. Empregados devem receber o salário no momento correto, usando o método que eles preferem, obedecendo várias taxas e impostos deduzidos do salário.
 + Alguns empregados são horistas. Eles recebem um salário por hora trabalhada. Eles submetem "cartões de ponto" todo dia para informar o número de horas trabalhadas naquele dia. Se um empregado trabalhar mais do que 8 horas, deve receber 1.5 a taxa normal durante as horas extras. Eles são pagos toda sexta-feira.
 + Alguns empregados recebem um salário fixo mensal. São pagos no último dia útil do mês (desconsidere feriados). Tais empregados são chamados "assalariados".
 + Alguns empregados assalariados são comissionados e portanto recebem uma comissão, um percentual das vendas que realizam. Eles submetem resultados de vendas que informam a data e valor da venda. O percentual de comissão varia de empregado para empregado. Eles são pagos a cada 2 sextas-feiras; neste momento, devem receber o equivalente de 2 semanas de salário fixo mais as comissões do período.
 	+ Empregados podem escolher o método de pagamento.
	+ Podem receber um cheque pelos correios.
	+ Podem receber um cheque em mãos.
	+ Podem pedir depósito em conta bancária
 + Alguns empregados pertencem ao sindicato (para simplificar, só há um possível sindicato). O sindicato cobra uma taxa mensal do empregado e essa taxa pode variar entre empregados. A taxa sindical é deduzida do salário. Além do mais, o sindicato pode ocasionalmente cobrar taxas de serviços adicionais a um empregado. Tais taxas de serviço são submetidas pelo sindicato mensalmente e devem ser deduzidas do próximo contracheque do empregado. A identificação do empregado no sindicato não é a mesma da identificação no sistema de folha de pagamento.
 + A folha de pagamento é rodada todo dia e deve pagar os empregados cujos salários vencem naquele dia. O sistema receberá a data até a qual o pagamento deve ser feito e calculará o pagamento para cada empregado desde a última vez em que este foi pago.
---------

## Running the system

```
To run the project, you must run the main.py file
```

The system menu includes 9 features: 1 - Add employee, 2 - Employee removal, 3 - Add a card, 4 - Add sales, 5 - Apply service fee, 6 - Change details, 7 - Payroll for today, 8 - Show Employees and 9 - Change payment period

```
PAYROLL

Menu:
1 - Add employee
2 - Employee removal
3 - Add a card
4 - Add sales
5 - Apply service fee
6 - Change details
7 - Payroll for today
8 - Show Employees
9 - Change payment period
Options:
```
Showing some examples:

**Add employee**

When option 1 (Add employee) is selected, the user must provide the following data: RG, Name, Address, Types employee [0: Salaried, 1: Hourly, 2: Commissioned], Salary, Select method payment [0: Bank account deposit, 1: Check card in hand, 2: Check card by post] and Start date

The Star_date input refers to the employee's registration date, to facilitate testing. After the employee is added to the system, a registration table is shown containing all employees.

```
Add employee

RG: 9786

Name: Guilherme Monteiro

Address: Maceio

Types employee :
 0: Salaried
 1: Hourly
 2: Commissioned
Option: 0

Salary: 3000

Select method payment:
 0: Bank account deposit
 1: Check card in hand
 2: Check card by post
Option: 0

Start date: 2021-05-25

 Id   RG               Name Address Types employee  Payment Scheduled (in hours)  Worked hours  Salary  Commission percent       Payment method  Paycheck Last Payment Start date
  0 1233      Jose Fernando  Maceio       Salaried                           720             0    2000                   0 Bank account deposit         0              2020-10-10
  1 4567   Juliana Fernanda  Recife         Hourly                           144             0      20                   0   Check card in hand         0              2020-10-20
  2 3546        Jenet Alves Aracaju   Commissioned                           336             0    1800                   5   Check card by post         0              2020-10-20
  3 9786 Guilherme Monteiro  Maceio       Salaried                           336             0    3000                   0 Bank account deposit         0              2021-05-25

Operation performed successfully

Do you want to perform one more operation? (Y/N)
```

**Employee removal**

When option 2 (Employee removal) is selected, the system shows the table with all registered employees and asks for the employee ID that will be removed. Then the table returns (without the employee) and a warning message.

```
Select employe

 Id   RG               Name Address Types employee  Payment Scheduled (in hours)  Worked hours  Salary  Commission percent       Payment method  Paycheck Last Payment Start date
  0 1233      Jose Fernando  Maceio       Salaried                           720             0    2000                   0 Bank account deposit         0              2020-10-10
  1 4567   Juliana Fernanda  Recife         Hourly                           144             0      20                   0   Check card in hand         0              2020-10-20
  2 3546        Jenet Alves Aracaju   Commissioned                           336             0    1800                   5   Check card by post         0              2020-10-20
  3 9786 Guilherme Monteiro  Maceio       Salaried                           336             0    3000                   0 Bank account deposit         0              2021-05-25

Employee removal
Id: 3

 Id   RG             Name Address Types employee  Payment Scheduled (in hours)  Worked hours  Salary  Commission percent       Payment method  Paycheck Last Payment Start date
  0 1233    Jose Fernando  Maceio       Salaried                           720             0    2000                   0 Bank account deposit         0              2020-10-10
  1 4567 Juliana Fernanda  Recife         Hourly                           144             0      20                   0   Check card in hand         0              2020-10-20
  2 3546      Jenet Alves Aracaju   Commissioned                           336             0    1800                   5   Check card by post         0              2020-10-20

Operation performed successfully

Do you want to perform one more operation? (Y/N)
```

**Add a card**

When option 3 (Add a card) is selected, the system shows the table with all registered employees and asks for the ID of the employee who will have a time card added. If the employee is an hourly worker, the number of hours of work will be requested.

```
Select employe

 Id   RG             Name Address Types employee  Payment Scheduled (in hours)  Worked hours  Salary  Commission percent       Payment method  Paycheck Last Payment Start date
  0 1233    Jose Fernando  Maceio       Salaried                           720             0    2000                   0 Bank account deposit         0              2020-10-10
  1 4567 Juliana Fernanda  Recife         Hourly                           144             0      20                   0   Check card in hand         0              2020-10-20
  2 3546      Jenet Alves Aracaju   Commissioned                           336             0    1800                   5   Check card by post         0              2020-10-20

Id: 1

Work hours: 8

 Id   RG             Name Address Types employee  Payment Scheduled (in hours)  Worked hours  Salary  Commission percent       Payment method  Paycheck Last Payment Start date
  0 1233    Jose Fernando  Maceio       Salaried                           720             0    2000                   0 Bank account deposit         0              2020-10-10
  1 4567 Juliana Fernanda  Recife         Hourly                           144             8      20                   0   Check card in hand         0              2020-10-20
  2 3546      Jenet Alves Aracaju   Commissioned                           336             0    1800                   5   Check card by post         0              2020-10-20

Operation performed successfully

Do you want to perform one more operation? (Y/N)
```

**Add sales**

When option 4 (Add sales) is selected, the system shows the table with all registered employees and asks for the Id of the employee who will have an added sale. If the employee is commissioned, the sale price will be requested.

```
Add sales

Sale price: 1200

 Id   RG             Name Address Types employee  Payment Scheduled (in hours)  Worked hours  Salary  Commission percent       Payment method  Paycheck Last Payment Start date
  0 1233    Jose Fernando  Maceio       Salaried                           720             0    2000                   0 Bank account deposit         0              2020-10-10
  1 4567 Juliana Fernanda  Recife         Hourly                           144             8      20                   0   Check card in hand         0              2020-10-20
  2 3546      Jenet Alves Aracaju   Commissioned                           336             0    1800                   5   Check card by post         0              2020-10-20

Id: 2

Operation performed successfully

Do you want to perform one more operation? (Y/N)
```

## Code Smells

It is important to note that the project avoided Rigidity, Fragility, Complexity and Duplication in the code. Therefore, not many limitations were found (bad smells).

**Long Parameter List:** There is no single rule for how many is too many parameters. Usually more than three or four is considered too many. In the code written in PANDAS there were many Long parameter lists but the OOP version of the system has already been built thinking about not building methods with Long Parameter List. But, we have inputs_add_update(self, cols, cast, count, others_form).

**Feature Envy:** One method can access data of another type to do some operation. When this becomes common, it means that the object itself should perform this operation and deliver the result. In this code there is no Feature Envy method because encapsulation and MVC were used.

**Lazy Class:** There is no class that simply has an empty constructor and a getter and setter for each variable. Exactly because the OOP version of the system has already been built thinking about not building Lazy Class.

**Long Method** The only long method in the code is the menu() method present in class PanelMenu.

**Large Class:** refers to the classes that tend to centralize the intelligence of the system. Large Class indicates weaknesses in design that can possibly slow down the development or increase the chance of failures in the future. In addition, it makes the system more difficult to understand, read and develop. PanelMenu is a large class with many methods.

## Refactoring

To refactor is to restructure a software system by applying a series of transformations without modifying its observable behavior, in order to make it easier to understand and modify. However, the previous system was made in pandas without OOP and a new version of the system was made using OOP and MVC. 

1. Replacement of pandas storage for common list (stopped storing data on dataframe) but still left the pandas print feature active through the _iter_ method on each model.

2. The inputs_add_update() method of the PanelMenu class is used to insert values ​​(as a form) in any type of model. This is because two methods are defined within the models: columns_ () and types_cast_ ().

3. Two specific Controllers were made which are ManageEmployee and ManageTransaction. ManageCommons is general and used by all other models that are not specific, avoiding duplication of code.