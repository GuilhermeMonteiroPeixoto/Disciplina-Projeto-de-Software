class Syndicate:
    def __init__(self, uid, name, union_fee, employees_fks_rg, extra_union_fees_fks):
        self._uid = uid
        self._name = name
        self._union_fee = union_fee
        self._employees_fks_rg = employees_fks_rg
        self._extra_union_fees_fks = extra_union_fees_fks

    def __iter__(self):
        yield self._uid
        yield self._name
        yield self._union_fee
        yield self._employees_fk

    @classmethod
    def columns(cls):
        return ['Id', 'Name', 'Union fee', 'Employees']

    @staticmethod
    def types_cast_():
        return[True, False, True, True]

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
    def employees_fks_rg(self):
        return self._employees_fks_rg

    @employees_fks_rg.setter
    def employees_fks_rg(self, employees_fks_rg):
        self._employees_fks_rg = employees_fks_rg

    @property
    def union_fee(self):
        return self._union_fee

    @union_fee.setter
    def union_fee(self, union_fee):
        self._union_fee = union_fee

    @property
    def extra_union_fees_fks(self):
        return self._extra_union_fees_fks

    @extra_union_fees_fks.setter
    def extra_union_fees_fks(self, extra_union_fees_fks):
        self._extra_union_fees_fks = extra_union_fees_fks


