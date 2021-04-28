class EventHistory:
    def __init__(self, uid, command, data_type, uid_old_data, old_data):
        self._uid = uid
        self._command = command
        self._data_type = data_type
        self._uid_old_data = uid_old_data
        self._old_data = old_data

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._uid = uid

    @property
    def command(self):
        return self.command

    @command.setter
    def command(self, command):
        self._command = command

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        self._data_type = data_type

    @property
    def uid_old_data(self):
        return self._uid_old_data

    @uid_old_data.setter
    def uid_old_data(self, uid_old_data):
        self._uid_old_data = uid_old_data

    @property
    def old_data(self):
        return self.old_data

    @old_data.setter
    def old_data(self, old_data):
        self._old_data = old_data

