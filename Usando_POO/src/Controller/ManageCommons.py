import pandas as pd


class ManageCommons:
    def __init__(self, type_manage):
        self._type_manage = type_manage
        self._data = []

    def add(self, data):
        data.uid = len(self._data)
        self._data.append(data)

    def update(self, data):
        self._data[data.uid] = data

    def get(self, uid):
        return self._data[uid]

    def get_all(self):
        return self._data

    def show_all(self):
        if len(self._data) == 0:
            return 'There is no value recorded in '+self.type_manage
        frame = pd.DataFrame(list(self._data), columns=self._data[0].columns_())
        print(frame.to_string(index=False))

    def get_type_manage(self):
        return self._type_manage

    def delete(self, uid):
        self._data.pop()
