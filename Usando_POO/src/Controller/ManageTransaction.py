from ..Model import Transaction
from ..Model import Company

# colocar toda a regra de negocio aqui
class ManageTransaction:
    def __init__(self):
        self._transactions = []

    def add(self, transaction: Transaction):
        transaction.uid = len(self._transactions)
        self._transactions.add(transaction)

    def update(self, transaction: Transaction):
        self._transactions.insert(transaction.uid, transaction)

    def get(self, uid):
        return self._transactions[uid]

    def delete(self, uid):
        self._transactions.pop()
