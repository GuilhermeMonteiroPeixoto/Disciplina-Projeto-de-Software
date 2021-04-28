class Company:
    def __init__(self, uid, name, employee_fks):
        self._uid = uid
        self._name = name
        self._employee_fks = employee_fks

    def __init__(self, name, employee_fks):
        self._name = name
        self._employee_fks = employee_fks

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._uid = uid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def employee_fks(self):
        return self._employee_fks

    @name.setter
    def name(self, employee_fks):
        self._employee_fks = employee_fks
