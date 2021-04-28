class Employee:
    def __init__(self, uid, name, address, hourly_wage, payment_method, types_employee, start_date, transactions_fks):
        self._uid = uid
        self._name = name
        self._address = address
        self._hourly_wage = hourly_wage
        self._payment_method = payment_method
        self._types_employee = types_employee
        self.start_date = start_date
        self.transactions_fks = transactions_fks

    def __init__(self, uid, name, address, hourly_wage, payment_method, types_employee, start_date):
        self._uid = uid
        self._name = name
        self._address = address
        self._hourly_wage = hourly_wage
        self._payment_method = payment_method
        self._types_employee = types_employee
        self.start_date = start_date

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._uid = uid

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def hourly_wage(self):
        return self._hourly_wage

    @hourly_wage.setter
    def hourly_wage(self, hourly_wage):
        self._hourly_wage = hourly_wage

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        self._payment_method = payment_method

    @property
    def types_employee(self):
        return self._types_employee

    @types_employee.setter
    def types_employee(self, types_employee):
        self._types_employee = types_employee

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def transactions_fks(self):
        return self._transactions_fks

    @transactions_fks.setter
    def transactions_fks(self, transactions_fks_id):
        self._transactions_fks.append(transactions_fks_id)
