from ..Model import Employee
from ..Controller.ManageCommons import ManageCommons
from ..Controller.ManageTransaction import ManageTransaction
from datetime import date

import pandas as pd


class ManageEmployee:
    def __init__(self, type_manage, manage_syndicate: ManageCommons, manage_transaction: ManageTransaction):
        self._type_manage = type_manage
        self._employees = []
        self._manageSyndicate = manage_syndicate
        self._manage_transaction = manage_transaction

    def add(self, employee: Employee):
        employee.uid = len(self._employees)
        self._employees.append(employee)

    def add_working_point(self, uid, worked_hours):
        self._employees[uid].worked_hours += worked_hours

    def update(self, employee: Employee):
        self._employees[employee.uid] = employee

    def get(self, uid: int):
        return self._employees[uid]

    def get_all(self):
        return self._employees

    def show_all(self):
        if len(self._employees) == 0:
            print('There is no value recorded in em ' + self.type_manage)

        frame = pd.DataFrame(list(self._employees), columns=self._employees[0].columns_())
        print(frame.to_string(index=False))

    def get_rg(self, rg):
        for emp in self._employees:
            if rg == int(emp.rg):
                return emp
        return -1

    def get_rg_sy(self, rg_search: int, id_sy: int):
        syndicate = self._manageSyndicate.get(id_sy)
        for rg in syndicate.employees_fks_rg:
            if rg_search == rg:
                return self.get_rg(rg_search)
        return -1

    def get_all_rg_sy(self, id_sy):
        employees = []
        syndicate = self._manageSyndicate.get(id_sy)
        for rg in syndicate.employees_fks_rg:
            employees.append(self.get_rg(rg))
        return employees

    def show_all_rg_sy(self, id_sy):
        employees = self.get_all_rg_sy(id_sy)
        frame = pd.DataFrame(list(employees), columns=self._employees[0].columns_())
        print(frame.to_string(index=False))

    def get_type_manage(self):
        return self._type_manage

    def payroll(self, date_limit):
        d_limit = date.fromisoformat(date_limit)
        d_last = 0

        for employee in self._employees:
            if employee.last_payment != '':
                d_last = date.fromisoformat(employee.last_payment)
            else:
                d_last = date.fromisoformat(employee.start_date)

            if (d_last - d_limit).days * 24 >= employee.payment_scheduled:
                debts = 0
                gain = 0
                for t in self._manage_transaction.get_list_sender("Employee", employee.uid):
                    debts += t.value
                    self._manage_transaction.delete(t.uid)

                for t in self._manage_transaction.get_list_receive("Employee", employee.uid):
                    gain += t.value
                    self._manage_transaction.delete(t.uid)

                if employee.types_employee == "Salaried":
                    employee.paycheck = employee.salary/2 + gain - debts

                if employee.types_employee == "Hourly":
                    extra_hour = 0
                    if employee.worked_hours > employee.payment_scheduled:
                        extra_hour = (employee.worked_hours - employee.payment_scheduled)

                    employee.paycheck = extra_hour * employee.salary * 1.5  \
                                        + employee.payment_scheduled * employee.salary + gain - debts

                if employee.types_employee == "Commissioned":
                    employee.paycheck = employee.salary + gain - debts

                employee._worked_hours = 0
                employee.last_payment = date.today()

            t_today = []

    def delete(self, uid):
        del self._employees[uid]
