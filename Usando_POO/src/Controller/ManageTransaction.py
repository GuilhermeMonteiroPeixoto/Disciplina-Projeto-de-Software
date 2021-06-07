from ..Model import Transaction
import pandas as pd
from datetime import date


class ManageTransaction:
    def __init__(self, type_manage):
        self._type_manage = type_manage
        self._transactions = []
        self._manages = {}

    def add_manages(self, manage):
        self._manages[manage.get_type_manage] = manage

    def add(self, transaction: Transaction):
        transaction.uid = len(self._transactions)
        self._transactions.append(transaction)

    def update(self, transaction: Transaction):
        self._transactions[transaction.uid] = transaction

    def get(self, uid):
        return self._transactions[uid]

    def get_list_sender(self, sender_type, sender_id):
        t_result = []
        for t in self._transactions:
            if t.sender_type == sender_type and t.sender_id == sender_id:
                t_result.append(t)
        return t_result

    def get_list_receive(self, receive_type, receive_id):
        t_result = []
        for t in self._transactions:
            if t.receive_type == receive_type and t.receive_id == receive_id:
                t_result.append(t)
        return t_result

    def get_list(self, sender_type, sender_id, receive_type, receive_id):
        t_result = []
        for t in self._transactions:
            if t.sender_type == sender_type and t.sender_id == sender_id and t.receive_type == receive_type \
                    and t.receive_id == receive_id:
                t_result.append(t)
        return t_result

    def get_all(self):
        return self._transactions

    def payroll(self):
        actual_date = '{}/{}/{}'.format(date.today().day, date.today().month, date.today().year)
        t_today = []

        for t in self._transactions:
            if actual_date == t.date:
                t_today.append(t)

        for t in t_today:
            if t.sender_type == "Employee":
                manage = self._manages[t.sender_type]

            if t.receive_type == "Employee":
                manage = self._manages[t.sender_type]

            if t.sender_type == "Syndicate":
                manage = self._manages[t.sender_type]

            if t.receive_type == "Syndicate":
                manage = self._manages[t.sender_type]

    def show_all(self):
        if len(self._transactions) == 0:
            return 'There is no value recorded in '+self.type_manage
        frame = pd.DataFrame(list(self._transactions), columns=self._transactions[0].columns_())
        print(frame.to_string(index=False))

    def get_type_manage(self):
        return self._type_manage

    def delete(self, uid):
        del self._transactions[uid]
