import os

from ..Controller.ManageEmployee import ManageEmployee
from ..Controller.ManageTransaction import ManageTransaction
from ..Controller.ManageCommons import ManageCommons

from ..Model.Company import Company
from ..Model.Employee import Employee
from ..Model.ExtraUnionFees import ExtraUnionFees
from ..Model.Syndicate import Syndicate
from ..Model.Transaction import Transaction
from datetime import date
from collections import OrderedDict


class PanelMenu:
    def __init__(self):
        self._menu = []
        self._manageCompany = ManageCommons('Company')
        self._manageCompany.add(Company(0, 'Comp1', [0, 1]))

        self._manageExtraUnionFees = ManageCommons('ExtraUnionFees')
        self._manageExtraUnionFees.add(ExtraUnionFees(0, 'Extra Fees 1', 'Extra Fees 1', 100))
        self._manageExtraUnionFees.add(ExtraUnionFees(1, 'Extra Fees 2', 'Extra Fees 2', 20))

        self._manageSyndicate = ManageCommons('Syndicate')
        self._manageSyndicate.add(Syndicate(0, "One Syndicate", 50, [4567, 1233], [0, 1]))

        self._manageTransaction = ManageTransaction('Transaction')
        self._manageEmployee = ManageEmployee('Employee', self._manageSyndicate, self._manageTransaction)

        self._manageEmployee.add(Employee(0, 1233, 'Jose Fernando', 'Maceio', 'Salaried', 720, 0, 2000, 0, 'Bank account deposit', 0, '',
                                          '2020-10-10'))
        self._manageEmployee.add(Employee(1, 4567, 'Juliana Fernanda', 'Recife', 'Hourly', 144, 0, 20, 0, 'Check card in hand', 0, '',
                                          '2020-10-20'))
        self._manageEmployee.add(Employee(2, 3546, 'Jenet Alves', 'Aracaju', 'Commissioned', 336, 0, 1800, 5, 'Check card by post', 0, '',
                                          '2020-10-20'))

        self._manageTransaction.add_manages(self._manageCompany)
        self._manageTransaction.add_manages(self._manageEmployee)
        self._manageTransaction.add_manages(self._manageSyndicate)

    def ask_new_operation(self):
        if input('Do you want to perform one more operation? (Y/N) ') != 'Y':
            return True
        else:
            return False

    def form_type_employee(self):
        types = ["Salaried","Hourly","Commissioned"]
        print("Types employee : ")
        print(" 0: Salaried")
        print(" 1: Hourly")
        print(" 2: Commissioned")
        return types[self.inputs_id(3, 'Option')]

    def form_payment_method(self):
        types = ["Bank account deposit", "Check card in hand", "Check card by post"]
        label_opt = "Select method payment:"
        count = 0
        print(label_opt)
        for t in types:
            print(" "+str(count)+": "+t)
            count += 1

        return types[self.inputs_id(len(types), 'Option')]

    def inputs_add_update(self, cols, cast, count, others_form):
        values = []
        if count == 1:
            values = [-1]
        while count < len(cols):
            if cols[count] in others_form:
                _input = others_form[cols[count]]()
            else:
                _input = input(cols[count] + ": ")
            if _input.isnumeric() == cast[count]:
                if _input.isnumeric():
                    _input = int(_input)

                values.append(_input)
                count += 1
            else:
                if cast[count]:
                    print("Enter a numeric value\n")
                else:
                    print("Enter a string value\n")
        return values

    def inputs_id(self, l, label):
        while True:
            _input = input(label+": ")
            if _input.isnumeric():
                if int(_input) < l:
                    return int(_input)
                else:
                    print(_input+" Enter a numeric value less than "+str(l)+"\n")
            else:
                if _input == '-1':
                    return _input
                print("Enter a numeric value or -1 to cancel\n")

    def inputs_rg(self, rg_search, id_sy):
        employee = []
        while True:
            employee = self._manageEmployee.get_rg_sy(rg_search, id_sy)
            if employee != -1:
                return employee
            else:
                if rg_search == '-1':
                    return rg_search
                print("Enter a valid rg")
                rg_search = int(input("Rg: "))

    def select_employee(self):
        print("\nSelect employe")
        self._manageEmployee.show_all()
        l = len(self._manageEmployee.get_all())
        uid = self.inputs_id(l, "Id")

    def menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('PAYROLL\n')
        print('Menu:')
        print("1 - Add employee")
        print("2 - Employee removal")
        print("3 - Add a card")
        print("4 - Add sales")
        print("5 - Apply service fee")
        print("6 - Change details")
        print("7 - Payroll for today")
        print("8 - Show Employees")
        print("9 - Change payment period")

        opt = int(input('Options: '))

        if opt == 1:
            print('\nAdd employee')
            manage = self._manageEmployee
            other_forms = OrderedDict()
            other_forms['Types employee'] = self.form_type_employee
            other_forms['Worked hours'] = lambda: '0'
            other_forms['Commission percent'] = lambda: '0'
            other_forms['Paycheck'] = lambda: '0'
            other_forms['Payment Scheduled (in hours)'] = lambda: '0'
            other_forms['Last Payment'] = lambda: ''
            other_forms['Payment method'] = self.form_payment_method

            values = self.inputs_add_update(manage.get(0).columns_(), manage.get(0).types_cast_(), 1, other_forms)
            employee = Employee(*values)

            if employee.types_employee == 'Salaried':
                employee.payment_scheduled = 14*24
            elif employee.types_employee == 'Hourly':
                employee.payment_scheduled = 6*24
            elif employee.types_employee == 'Commissioned':
                employee.payment_scheduled = 30*24
                value = int(input('Commission percent: '))
                employee.commission_percent = value

            manage.add(employee)
            manage.show_all()
            print("Operation performed successfully")

        elif opt == 2:
            print("\nSelect employe")
            manage = self._manageEmployee
            manage.show_all()
            print('\nEmployee removal')
            l = len(manage.get_all())
            uid = self.inputs_id(l, "Id")
            if not uid == -1:
                self._manageEmployee.delete(uid)
            manage.show_all()
            print("Operation performed successfully")

        elif opt == 3:
            print("\nSelect employe")
            self._manageEmployee.show_all()
            l = len(self._manageEmployee.get_all())
            uid = self.inputs_id(l, "Id")
            hours = int(input("Work hours: "))
            self._manageEmployee.add_working_point(uid, hours)
            self._manageEmployee.show_all()
            print("Operation performed successfully")

        elif opt == 4:
            print('\nAdd sales')
            value = int(input('Sale price: '))
            self._manageEmployee.show_all()
            l = len(self._manageEmployee.get_all())
            uid = self.inputs_id(l, "Id")
            employee = self._manageEmployee.get(uid)
            self._manageTransaction.add(Transaction(-1, 0, 'Other', 0, 'Company', 'house sale',
                                                    date.today(), 'percentage of house sale',
                                                    value-value*(employee.commission_percent/100)))

            self._manageTransaction.add(Transaction(-1, 0, 'Company', uid, 'Employee', 'percent', date.today(),
                                                    'percentage of house sale',
                                                    value*(employee.commission_percent/100)))

            print("Operation performed successfully")

        elif opt == 5:
            print("\nSelect Extra union fees")
            self._manageExtraUnionFees.show_all()
            l = len(self._manageExtraUnionFees.get_all())
            uid = self.inputs_id(l, "Id")
            ex_union_fees = self._manageExtraUnionFees.get(uid)

            print("\nSelect employe")
            self._manageEmployee.show_all_rg_sy(0)
            rg = int(input("Rg: "))
            employer = self.inputs_rg(rg, 0)

            self._manageTransaction.add(Transaction(-1, employer.uid, "Employee", 0, "Syndicate",
                                                    "Extra Syndicate Fees", date.today(), "Extra Syndicate Fees",
                                                    ex_union_fees.value))
            self._manageTransaction.show_all()
            print("Operation performed successfully")

        elif opt == 6:
            print('\nEmployee Modification:')

            print("\nSelect employee")
            self._manageEmployee.show_all()
            l = len(self._manageEmployee.get_all())
            uid = self.inputs_id(l, "Id")
            employee = self._manageEmployee.get(uid)

            print('1. Rename')
            print('2. Change Address')
            print('3. Change Contract Type')
            print('4. Change Payment Method')

            if not uid == -1:
                opt2 = int(input('Options: '))
                os.system('cls' if os.name == 'nt' else 'clear')

                if opt2 == 1:
                    value = self.inputs_add_update(['Name'], [False], 0, {})
                    employee.name = value[0]
                elif opt2 == 2:
                    value = self.inputs_add_update(['Address'], [False], 0, {})
                    employee.address = value[0]
                elif opt2 == 3:
                    other_forms = OrderedDict()
                    other_forms['Types employee'] = self.form_type_employee
                    value = self.inputs_add_update(['Types employee'], [False], 0, other_forms)
                    employee.types_employee = value[0]

                    if employee.types_employee == 'Salaried':
                        employee.payment_scheduled = 14 * 24
                    elif employee.types_employee == 'Hourly':
                        employee.payment_scheduled = 6 * 24
                    elif employee.types_employee == 'Commissioned':
                        employee.payment_scheduled = 30 * 24
                        value = int(input('Commission percent: '))
                        employee.commission_percent = value

                elif opt2 == 4:
                    other_forms = OrderedDict()
                    other_forms['Payment method'] = self.form_payment_method
                    value = self.inputs_add_update(['Payment method'], [False], 0, other_forms)
                    employee.payment_method = value[0]

                self._manageEmployee.update(employee)
                self._manageEmployee.show_all()
                print("Operation performed successfully")

        elif opt == 7:
            input_date = input('Enter a date to make payments until it (ex 2020-08-31): ')
            self._manageEmployee.payroll(input_date)
            self._manageEmployee.show_all()

        elif opt == 8:
            print('\nAll Employees')
            self._manageEmployee.show_all()

        elif opt == 9:
            print('\nChange payment scheduled')
            print("\nSelect employee")
            self._manageEmployee.show_all()
            l = len(self._manageEmployee.get_all())
            uid = self.inputs_id(l, "Id")
            employee = self._manageEmployee.get(uid)
            period = int(input("Payment per scheduled (in days): "))
            employee.payment_scheduled = period*24
            employee.salary = 0
            salary = int(input("salary: "))
            employee.salary = salary
            self._manageEmployee.show_all()
            print("Operation performed successfully")

    def start(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.menu()
            if self.ask_new_operation():
                break

