class Transaction:
    def __init__(self, uid, sender_id, sender_type, receiver_id, receiver_type, date, description, value):
        self._uid = uid
        self._sender_id = sender_id
        self._sender_type = sender_type
        self._receiver_id = receiver_id
        self._receiver_type = receiver_type
        self._date = date
        self._description = description
        self._value = value


    def __init__(self, sender_id, sender_type, receiver_id, receiver_type, date, description, value):
        self._sender_id = sender_id
        self._sender_type = sender_type
        self._receiver_id = receiver_id
        self._receiver_type = receiver_type
        self._date = date
        self._description = description
        self._value = value


    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._uid = uid

    @property
    def _sender_id(self):
        return self._sender_id

    @_sender_id.setter
    def _sender_id(self, _sender_id):
        self._sender_id = _sender_id

    @property
    def sender_type(self):
        return self._sender_type

    @sender_type.setter
    def sender_type(self, sender_type):
        self._sender_type = sender_type

    @property
    def receiver_id(self):
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, receiver_id):
        self._receiver_id = receiver_id

    @property
    def receiver_type(self):
        return self._receiver_type

    @receiver_type.setter
    def receiver_type(self, receiver_type):
        self._receiver_type = receiver_type

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def description(self):
        return self._description

    @receiver_type.setter
    def description(self, description):
        self._description = description

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
