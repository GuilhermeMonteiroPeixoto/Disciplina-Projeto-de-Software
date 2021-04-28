class ExtraUnionFees:
    def __init__(self, uid, name, description, value):
        self._uid = uid
        self._name = name
        self._description = description
        self._value = value

    def __init__(self, name, description, value):
        self._name = name
        self._description = description
        self._value = value

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
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
