class Employee:
    def __init__(self, uid, rg, name, address, types_employee, payment_scheduled, worked_hours, salary,
                 commission_percent, payment_method, paycheck, last_payment, start_date):
        self._uid = uid
        self._rg = rg
        self._name = name
        self._address = address
        self._types_employee = types_employee
        self._payment_scheduled = payment_scheduled
        self._worked_hours = worked_hours
        self._salary = salary
        self._commission_percent = commission_percent
        self._payment_method = payment_method
        self._paycheck = paycheck
        self._last_payment = last_payment
        self._start_date = start_date

    def __iter__(self):
        yield self._uid
        yield self._rg
        yield self._name
        yield self._address
        yield self._types_employee
        yield self._payment_scheduled
        yield self._worked_hours
        yield self._salary
        yield self._commission_percent
        yield self._payment_method
        yield self._paycheck
        yield self._last_payment
        yield self._start_date


    @staticmethod
    def columns_():
        return['Id', 'RG', 'Name', 'Address', 'Types employee', 'Payment Scheduled (in hours)', 'Worked hours', 'Salary',
               'Commission percent', 'Payment method', 'Paycheck', 'Last Payment', 'Start date']

    @staticmethod
    def types_cast_():
        return[True, True, False, False, False, True, True, True, True, False, True, False, False]

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._uid = uid

    @property
    def rg(self):
        return self._rg

    @rg.setter
    def rg(self, rg):
        self._rg = rg

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def types_employee(self):
        return self._types_employee

    @types_employee.setter
    def types_employee(self, types_employee):
        self._types_employee = types_employee

    @property
    def payment_scheduled(self):
        return self._payment_scheduled

    @payment_scheduled.setter
    def payment_scheduled(self, payment_scheduled):
        self._payment_scheduled = payment_scheduled

    @property
    def worked_hours(self):
        return self._worked_hours

    @worked_hours.setter
    def worked_hours(self, worked_hours):
        self._worked_hours = worked_hours

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def commission_percent(self):
        return self._commission_percent

    @commission_percent.setter
    def commission_percent(self, commission_percent):
        self._commission_percent = commission_percent

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        self._payment_method = payment_method

    @property
    def paycheck(self):
        return self.paycheck

    @paycheck.setter
    def paycheck(self, paycheck):
        self._paycheck = paycheck

    @property
    def last_payment(self):
        return self._last_payment

    @last_payment.setter
    def last_payment(self, last_payment):
        self._last_payment = last_payment

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def paycheck(self):
        return self._paycheck

    @paycheck.setter
    def paycheck(self, paycheck):
        self._paycheck = paycheck
