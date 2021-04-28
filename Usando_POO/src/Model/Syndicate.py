class Syndicate:
    def __init__(self, uid, name, employees_fk, union_fee, extra_union_fees_fk):
        self._uid = uid
        self._name = name
        self._employees_fk = employees_fk
        self._union_fee = union_fee
        self._extra_union_fees_fk = extra_union_fees_fk

    def __init__(self, name, employees_fk, union_fee, extra_union_fees_fk):
        self._name = name
        self._employees_fk = employees_fk
        self._union_fee = union_fee
        self._extra_union_fees_fk = extra_union_fees_fk

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._uid = uid

    @property
    def name(self):
        return self._name

    @uid.setter
    def name(self, name):
        self.name = name

    @property
    def employees_fk(self):
        return self._employees_fk

    @employees_fk.setter
    def employees_fk(self, employees_fk):
        self._employees_fk = employees_fk

    @property
    def union_fee(self):
        return self._union_fee

    @uid.setter
    def union_fee(self, union_fee):
        self._union_fee = union_fee

    @property
    def extra_union_fees_fk(self):
        return self._extra_union_fees_fk

    @extra_union_fees_fk.setter
    def extra_union_fees_fk(self, extra_union_fees_fk):
        self._extra_union_fees_fk = extra_union_fees_fk


